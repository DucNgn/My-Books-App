<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">My Books</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">
          Welcome {{greetedUser}} <br />
          My Genres: 
          <span v-for="(item, i) in userFavouriteGenres">
            <v-chip :color="`blue lighten-4`" label small>{{item}}</v-chip>
          </span>
        </div>
      </v-card-text>
    </v-card>
    <v-card v-for="(shelf, shelfName) in getShelvesAndBooks" class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline .text-h4">{{shelfName}}</div>
      </v-card-title>
          <v-data-table
            :headers="shelf.headers"
            :items="shelf.books"
            class="elevation-1"
          >
          <template v-slot:items="props">
          <td>{{ props.item.title }}</td>
          <td>{{ props.item.author }}</td>
          <td>{{ props.item.genre }}</td>
          <td>{{ props.item.isbn }}</td>
          <td>{{ props.item.num_of_pages }}</td>
          </template>
        </v-data-table>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';

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
          { text: 'Number of pages', value: 'num_of_pages' },
        ];
    const mockData = {
      "id": 1,
      "owner_id": 1,
      "Reading": {
        headers: sharedHeaders,
        books: [
        {
          "title": "PHP 1",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "Did Harry speak Python 2",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
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
          "title": "PHP 1",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "Did Harry speak Python 2",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "JS 3",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        }]},
      "Read": {
        headers: sharedHeaders,
        books: [
        {
          "title": "PHP 1",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "Did Harry speak Python 2",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
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
          "title": "PHP 1",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "Did Harry speak Python 2",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        {
          "title": "JS 3",
          "author": "JK Rowling",
          "genre": "Mystery",
          "isbn": "12345",
          "cover_image_url": "https://somthing",
          "num_of_pages": 200
        },
        ]},
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
