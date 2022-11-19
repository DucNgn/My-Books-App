<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">My Books</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">Welcome {{greetedUser}}</div>
      </v-card-text>
    </v-card>
    <v-card v-for="(shelf, shelfName) in getShelvesAndBooks" class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline .text-h4">{{shelfName}}</div>
      </v-card-title>
      <v-card-text>
      {{shelf}}
      </v-card-text>
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

  get getShelvesAndBooks() {
    const mockData = {
      "id": 1,
      "owner_id": 1,
      "Reading": [
        "1",
        "2",
        "3"
      ],
      "To Read": [
        "5",
        "6",
        "7",
        "8"
      ],
      "Read": [
        "9",
        "10",
        "11",
        "12"
      ],
      "Favorite": [
        "100",
        "111",
        "112"
      ],
      "Recommendation": []
    }
    const data = Object.fromEntries(Object.entries(mockData).filter(([key]) => !["id", "owner_id"].includes(key)))
    return data
  }
}
</script>
