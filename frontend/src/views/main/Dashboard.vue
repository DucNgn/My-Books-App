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
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';
import router from '@/router';
import { commitChangeCurrentBook } from '@/store/main/mutations';

@Component
export default class Dashboard extends Vue {
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
    const userGenres = ["Mystery", "Dark", "Fiction"];
    return userGenres;
  }

  get getShelvesAndBooks() {
    const sharedHeaders = [
      { text: 'Title', value: 'title', align: 'left' },
      { text: 'Author', value: 'author' },
      { text: 'Genre', value: 'genre' },
      { text: 'ISBN', value: 'isbn' },
      { text: 'Number of pages', value: 'num_of_pages' }
    ];
    const mockData = {
      "id": 1,
      "owner_id": 1,
      "Reading": {
        headers: sharedHeaders,
        books: [
          {
            "id": 1,
            "title": "PHP 1",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2015/3/27/1427451436337/c75efc44-41b0-452a-8858-0811c0fd9978-401x600.jpeg?width=300&quality=45&auto=format&fit=max&dpr=2&s=b37753a8032188c743bab10405ad9508",
            "num_of_pages": 200
          },
          {
            "id": 2,
            "title": "Did Harry speak Python 2",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2015/3/27/1427451436337/c75efc44-41b0-452a-8858-0811c0fd9978-401x600.jpeg?width=300&quality=45&auto=format&fit=max&dpr=2&s=b37753a8032188c743bab10405ad9508",
            "num_of_pages": 200
          },
          {
            "id": 3,
            "title": "JS 3",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          }]
      },
      "To Read": {
        headers: sharedHeaders,
        books: [
          {
            "id": 4,
            "title": "PHP 1",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 5,
            "title": "Did Harry speak Python 2",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 6,
            "title": "JS 3",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          }]
      },
      "Read": {
        headers: sharedHeaders,
        books: [
          {
            "id": 7,
            "title": "PHP 1",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 8,
            "title": "Did Harry speak Python 2",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 9,
            "title": "JS 3",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          }]
      },
      "Favorite": {
        headers: sharedHeaders,
        books: [
          {
            "id": 10,
            "title": "PHP 1",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 11,
            "title": "Did Harry speak Python 2",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
          {
            "id": 12,
            "title": "JS 3",
            "author": "JK Rowling",
            "genre": "Mystery",
            "isbn": "12345",
            "cover_image_url": "https://somthing",
            "num_of_pages": 200
          },
        ]
      },
      "Recommendation": {
        headers: sharedHeaders,
        books: []
      }
    }
    const data = Object.fromEntries(Object.entries(mockData).filter(([key]) => !["id", "owner_id"].includes(key)))
    return data
  }
}
</script>
