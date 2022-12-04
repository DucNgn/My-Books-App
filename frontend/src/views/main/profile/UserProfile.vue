<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">User Profile</div>
      </v-card-title>
      <v-card-text>
        <div class="my-4">
          <div class="subheading secondary--text text--lighten-3">Full Name</div>
          <div class="title primary--text text--darken-2" v-if="userProfile && userProfile.full_name">{{userProfile.full_name}}</div>
          <div class="title primary--text text--darken-2" v-else>-----</div>
        </div>
        <div class="my-3">
          <div class="subheading secondary--text text--lighten-3">Email</div>
          <div class="title primary--text text--darken-2" v-if="userProfile && userProfile.email">{{userProfile.email}}</div>
          <div class="title primary--text text--darken-2" v-else>-----</div>
        </div>
        <div>
          <div class="subheading secondary--text text--lighten-3">Genre Preferences</div>
          <v-form ref="form">
            <input class="checkbox" disabled="true" type="checkbox" id="Childrens" value="Childrens" v-model="userFavouriteGenres">
            <label class="container" for="Childrens">Childrens</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Classics" value="Classics" v-model="userFavouriteGenres">
            <label class="container" for="Classics">Classics</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Fantasy" value="Fantasy" v-model="userFavouriteGenres">
            <label class="container" for="Fantasy">Fantasy</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Fiction" value="Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Fiction">Fiction</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Graphic Novels" value="Graphic Novels" v-model="userFavouriteGenres">
            <label class="container" for="Graphic Novels">Graphic Novels</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Historical Fiction" value="Historical Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Historical Fiction">Historical Fiction</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Horror" value="Horror" v-model="userFavouriteGenres">
            <label class="container" for="Horror">Horror</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Mystery" value="Mystery" v-model="userFavouriteGenres">
            <label class="container" for="Mystery">Mystery</label><br/>    
            <input class="checkbox" disabled="true" type="checkbox" id="Nonfiction" value="Nonfiction" v-model="userFavouriteGenres">
            <label class="container" for="Nonfiction">Nonfiction</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Picture Books" value="Picture Books" v-model="userFavouriteGenres">
            <label class="container" for="Picture Books">Picture Books</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Plays" value="Plays" v-model="userFavouriteGenres">
            <label class="container" for="Plays">Plays</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Romance" value="Romance" v-model="userFavouriteGenres">
            <label class="container" for="Romance">Romance</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Science Fiction" value="Science Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Science Fiction">Science Fiction</label><br/>
            <input class="checkbox" disabled="true" type="checkbox" id="Young Adult" value="Young Adult" v-model="userFavouriteGenres">
            <label class="container" for="Young Adult">Young Adult</label><br/>            
          </v-form>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/edit">Edit</v-btn>
        <v-btn to="/main/profile/password">Change password</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';

@Component
export default class UserProfile extends Vue {
  public userFavouriteGenres: string[] = [];

  public created() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.userFavouriteGenres = userProfile.favorite_genres;
    }
  }

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public goToEdit() {
    this.$router.push('/main/profile/edit');
  }

  public goToPassword() {
    this.$router.push('/main/profile/password');
  }
}
</script>
<style>
.container{ /* label */
  padding:0px!important;
}
.checkbox { /* input type checkbox */ 
  padding:0px!important;
  margin-top:5px;
  margin-right: 3px;
}
</style>


