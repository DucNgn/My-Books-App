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
        </div>
      </v-card-text>
    </v-card>
    <v-card v-for="(shelf, shelfName) in getShelvesAndBooks" class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline .text-h4">{{ shelfName }}</div>
      </v-card-title>
      <v-data-table :headers="shelf.headers" :items="shelf.books" class="elevation-1">
        <template v-slot:items="props">
          <tr v-on:click="clickRow(props.item)">
            <td>{{ props.item.title }}</td>
            <td>{{ props.item.author }}</td>
            <td>{{ props.item.genre }}</td>
            <td>{{ props.item.isbn }}</td>
            <td>{{ props.item.num_of_pages }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { readUserProfile, readPersonalShelves } from '@/store/main/getters';
import { commitChangeCurrentBook } from '@/store/main/mutations';
import { dispatchGetPersonalShelvesAndBooks } from '@/store/main/actions';

@Component
export default class Dashboard extends Vue {
  public async created() {
    await dispatchGetPersonalShelvesAndBooks(this.$store);
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

  public clickRow(book) {
    console.log("You clicked a book! ID:" + book.id);
    commitChangeCurrentBook(this.$store, book);
    this.$router.push({ name: "bookDetails" })
  }

  get userFavouriteGenres() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.favorite_genres) {
        return userProfile.favorite_genres
      }
    }
    return []
  }

  get getShelvesAndBooks() {
    const personalShelvesData = readPersonalShelves(this.$store);
    const sharedHeaders = [
      { text: 'Title', value: 'title', align: 'left' },
      { text: 'Author', value: 'author' },
      { text: 'Genre', value: 'genre' },
      { text: 'ISBN', value: 'isbn' },
      { text: 'Number of pages', value: 'num_of_pages' }
    ];
    const realData = {
      "To Read": {
        headers: sharedHeaders,
        books: personalShelvesData?.toread_shelf
      },
      "Reading": {
        headers: sharedHeaders,
        books: personalShelvesData?.reading_shelf
      },
      "Read": {
        headers: sharedHeaders,
        books: personalShelvesData?.read_shelf
      },
      "Favourite": {
        headers: sharedHeaders,
        books: personalShelvesData?.favorite_shelf
      },
      "Recommendation": {
        headers: sharedHeaders,
        books: personalShelvesData?.recommendation_shelf
      }
    };
    return realData;
  }
}
</script>
