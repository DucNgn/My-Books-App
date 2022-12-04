<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">My Books</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">
          Welcome {{ greetedUser }} <br />
          My Genres:
          <span v-for="(item, i) in userFavouriteGenres">
            <v-chip :color="`blue lighten-4`" label small>{{ item }}</v-chip>
          </span>
          <v-btn dark color="primary" to="/main/profile/edit">
            Edit Preferences
          </v-btn>

          <AddBookDialog></AddBookDialog>
          <v-btn color="primary" dark @click="showAddBookDialog">
            Add Book
          </v-btn>
        </div>
      </v-card-text>
    </v-card>
    <v-card
      v-for="(shelf, shelfName) in getShelvesAndBooks"
      class="ma-3 pa-3"
      v-on:drop.prevent="(e) => onDrop(e, shelf)"
      :ondragover="
        shelfName === 'Recommendations' ? 'return true' : 'return false'
      "
    >
      <v-card-title primary-title>
        <div class="headline .text-h4">{{ shelfName }}</div>

        <v-btn
          v-if="shelfName === 'Recommendations'"
          v-on:click="updateRecommendations"
          class="mx-2"
          fab
          dark
          small
          color="pink"
        >
          <v-icon dark>refresh</v-icon>
        </v-btn>
      </v-card-title>
      <v-data-table
        :headers="shelf.headers"
        :items="shelf.books"
        class="elevation-1"
      >
        <template v-slot:items="props">
          <tr
            v-on:click="clickRow(props.item)"
            @dragstart="startDrag($event, props.item, shelf)"
            v-bind:draggable="true"
            :id="props.item.title + '\%/\%' + props.item.isbn"
            @dragover.stop
          >
            <td>{{ props.item.title }}</td>
            <td>{{ props.item.author }}</td>
            <td>{{ props.item.genre }}</td>
            <td>{{ props.item.rating }}</td>
            <td>{{ props.item.num_of_pages }}</td>
            <td style="pointer-events: none">
              <button
                style="pointer-events: auto"
                v-on:click="
                  (e) =>
                    favoriteClick(e, shelf, props.item, props.item.isFavorite)
                "
              >
                <font-awesome-icon
                  v-if="props.item.isFavorite"
                  icon="fa-solid fa-heart"
                />
                <font-awesome-icon v-else icon="fa-regular fa-heart" />
              </button>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { readUserProfile, readPersonalShelves } from '@/store/main/getters';
import {
  dispatchGetPersonalShelvesAndBooks,
  dispatchUpdateRecommendations,
  dispatchUpdateShelves,
  dispatchUpdateRecommendationsSilent,
} from '@/store/main/actions';
import {
  commitChangeCurrentBook,
  commitIsShowingAddBookDialog,
} from '@/store/main/mutations';

import AddBookDialog from './AddBookDialog.vue';

Vue.component('AddBookDialog', AddBookDialog);

@Component
export default class Dashboard extends Vue {
  draggingBook;
  originShelf;
  favoriteShelf;

  public async created() {
    await dispatchGetPersonalShelvesAndBooks(this.$store);
    await dispatchUpdateRecommendationsSilent(this.$store);
  }

  get greetedUser() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.full_name) {
        return userProfile.full_name;
      } else {
        return userProfile.email;
      }
    }
  }

  public favoriteClick(e, fromShelf, book, inFavorites) {
    e.stopPropagation();

    let data = {};
    console.log(this.favoriteShelf);
    let newFavoritesIDs = this.getBookIds(
      this.favoriteShelf,
      book,
      !inFavorites
    );
    console.log('pass');
    data[this.favoriteShelf.api_name] = newFavoritesIDs;

    if (fromShelf.api_name == 'recommendation_shelf') {
      let newRecommendedIDs = this.getBookIds(fromShelf, book, false);
      data[fromShelf.api_name] = newRecommendedIDs;
    }
    console.log(data);
    dispatchUpdateShelves(this.$store, data);
  }

  public startDrag(event, book, shelf) {
    this.draggingBook = book;
    this.originShelf = shelf;
  }

  public getBookIds(shelf, book, addBook) {
    let newdestinationShelfBookIDs: string[] = [];
    shelf.books.forEach((b) => {
      if (addBook || book != b) newdestinationShelfBookIDs.push(b.id);
    });
    if (addBook) newdestinationShelfBookIDs.push(book.id);
    return newdestinationShelfBookIDs;
  }

  public onDrop(event, destinationShelfBooks) {
    if (this.validDrop(destinationShelfBooks)) {
      let data = {};

      if (
        this.originShelf.api_name != 'recommendation_shelf' &&
        this.originShelf.api_name != 'favorite_shelf' &&
        destinationShelfBooks.api_name != 'favorite_shelf'
      ) {
        let newOriginShelfBookIDs = this.getBookIds(
          this.originShelf,
          this.draggingBook,
          false
        );
        data[this.originShelf.api_name] = newOriginShelfBookIDs;
      }
      let newdestinationShelfBookIDs = this.getBookIds(
        destinationShelfBooks,
        this.draggingBook,
        true
      );

      (data[destinationShelfBooks.api_name] = newdestinationShelfBookIDs),
        dispatchUpdateShelves(this.$store, data);
    }
    this.draggingBook = null;
    this.originShelf = '';
  }

  private validDrop(shelf) {
    return shelf != this.originShelf;
  }

  public clickRow(book) {
    commitChangeCurrentBook(this.$store, book);
    this.$router.push({ name: 'bookDetails' });
  }

  public updateRecommendations() {
    dispatchUpdateRecommendations(this.$store);
  }

  public showAddBookDialog() {
    commitIsShowingAddBookDialog(this.$store, true);
  }

  get userFavouriteGenres() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.favorite_genres) {
        return userProfile.favorite_genres;
      }
    }
    return [];
  }

  public updateFavoritesInShelf(shelf, set) {
    shelf.forEach(
      (book, index) => (shelf[index].isFavorite = set.has(book.id))
    );
  }

  public updateFavorites(personalShelvesData) {
    if (personalShelvesData == null) return;
    console.log(personalShelvesData);
    let set = new Set();
    personalShelvesData?.favorite_shelf.forEach((book, index) => {
      personalShelvesData!.favorite_shelf[index].isFavorite = true;
      set.add(book.id);
    });

    this.updateFavoritesInShelf(personalShelvesData?.read_shelf, set);
    this.updateFavoritesInShelf(personalShelvesData?.reading_shelf, set);
    this.updateFavoritesInShelf(personalShelvesData?.toread_shelf, set);
  }

  get getShelvesAndBooks() {
    const personalShelvesData = readPersonalShelves(this.$store);
    const sharedHeaders = [
      { text: 'Title', value: 'title', align: 'left' },
      { text: 'Author', value: 'author' },
      { text: 'Genre', value: 'genre' },
      { text: 'Rating', value: 'rating' },
      { text: 'Number of pages', value: 'num_of_pages' },
      { text: 'Favorite', value: 'isFavorite' },
    ];

    this.updateFavorites(personalShelvesData);

    const formattedData = {
      'To Read': {
        headers: sharedHeaders,
        books: personalShelvesData?.toread_shelf,
        api_name: 'toread_shelf',
        title: 'To Read',
      },
      Reading: {
        headers: sharedHeaders,
        books: personalShelvesData?.reading_shelf,
        api_name: 'reading_shelf',
        title: 'Reading',
      },
      Read: {
        headers: sharedHeaders,
        books: personalShelvesData?.read_shelf,
        api_name: 'read_shelf',
        title: 'Read',
      },
      Favourites: {
        headers: sharedHeaders,
        books: personalShelvesData?.favorite_shelf,
        api_name: 'favorite_shelf',
        title: 'Favourites',
      },
      Recommendations: {
        headers: sharedHeaders,
        books: personalShelvesData?.recommendation_shelf,
        api_name: 'recommendation_shelf',
        title: 'Recommendations',
      },
    };
    this.favoriteShelf = formattedData.Favourites;
    return formattedData;
  }
}
</script>
