<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit User Profile</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form
            v-model="valid"
            ref="form"
            lazy-validation
          >
            <v-text-field
              label="Full Name"
              v-model="fullName"
              required
            ></v-text-field>
            <v-text-field
              label="E-mail"
              type="email"
              v-model="email"
              v-validate="'required|email'"
              data-vv-name="email"
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="resetUserProfile">Reset</v-btn>
        <v-btn
          @click="submitUserProfile"
          :disabled="!valid"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>

    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Genre Preferences</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form">
            <input class="checkbox" type="checkbox" id="Childrens" value="Childrens" v-model="userFavouriteGenres">
            <label class="container" for="Childrens">Childrens</label><br/>
            <input class="checkbox" type="checkbox" id="Classics" value="Classics" v-model="userFavouriteGenres">
            <label class="container" for="Classics">Classics</label><br/>
            <input class="checkbox" type="checkbox" id="Fantasy" value="Fantasy" v-model="userFavouriteGenres">
            <label class="container" for="Fantasy">Fantasy</label><br/>
            <input class="checkbox" type="checkbox" id="Fiction" value="Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Fiction">Fiction</label><br/>
            <input class="checkbox" type="checkbox" id="Graphic Novels" value="Graphic Novels" v-model="userFavouriteGenres">
            <label class="container" for="Graphic Novels">Graphic Novels</label><br/>
            <input class="checkbox" type="checkbox" id="Historical Fiction" value="Historical Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Historical Fiction">Historical Fiction</label><br/>
            <input class="checkbox" type="checkbox" id="Horror" value="Horror" v-model="userFavouriteGenres">
            <label class="container" for="Horror">Horror</label><br/>
            <input class="checkbox" type="checkbox" id="Mystery" value="Mystery" v-model="userFavouriteGenres">
            <label class="container" for="Mystery">Mystery</label><br/>    
            <input class="checkbox" type="checkbox" id="Nonfiction" value="Nonfiction" v-model="userFavouriteGenres">
            <label class="container" for="Nonfiction">Nonfiction</label><br/>
            <input class="checkbox" type="checkbox" id="Picture Books" value="Picture Books" v-model="userFavouriteGenres">
            <label class="container" for="Picture Books">Picture Books</label><br/>
            <input class="checkbox" type="checkbox" id="Plays" value="Plays" v-model="userFavouriteGenres">
            <label class="container" for="Plays">Plays</label><br/>
            <input class="checkbox" type="checkbox" id="Romance" value="Romance" v-model="userFavouriteGenres">
            <label class="container" for="Romance">Romance</label><br/>
            <input class="checkbox" type="checkbox" id="Science Fiction" value="Science Fiction" v-model="userFavouriteGenres">
            <label class="container" for="Science Fiction">Science Fiction</label><br/>
            <input class="checkbox" type="checkbox" id="Young Adult" value="Young Adult" v-model="userFavouriteGenres">
            <label class="container" for="Young Adult">Young Adult</label><br/>            
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="resetUserGenres">Reset</v-btn>
        <v-btn @click="submitUserGenres">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IUserProfileUpdate } from '@/interfaces';
import { readUserProfile } from '@/store/main/getters';
import { dispatchUpdateRecommendations, dispatchUpdateUserProfile } from '@/store/main/actions';

@Component
export default class UserProfileEdit extends Vue {
  public valid = true;
  public fullName: string = '';
  public email: string = '';
  public userFavouriteGenres: string[] = [];

  public created() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.fullName = userProfile.full_name;
      this.email = userProfile.email;
      this.userFavouriteGenres = userProfile.favorite_genres;
    }
  }

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public resetUserProfile() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.fullName = userProfile.full_name;
      this.email = userProfile.email;
    }
  }

  public resetUserGenres() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.userFavouriteGenres = userProfile.favorite_genres;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submitUserProfile() {
    if ((this.$refs.form as any).validate()) {
      const updatedProfile: IUserProfileUpdate = {};
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      await dispatchUpdateUserProfile(this.$store, updatedProfile);
      this.$router.push('/main/profile');
    }
  }

  public async submitUserGenres() {
    const updatedProfile: IUserProfileUpdate = {};
    if (this.userFavouriteGenres) {
      updatedProfile.favorite_genres = this.userFavouriteGenres;
    }
    await dispatchUpdateUserProfile(this.$store, updatedProfile);
    await dispatchUpdateRecommendations(this.$store);

    this.$router.push('/main/profile');
  }
}
</script>
<style>
.container{ /* label */
  padding:3.5px!important; /* adds area where you can misclick but is still recognized, set this low, too much and it overlaps with other labels */ 
  font-size:15px;
}
.checkbox { /* input type checkbox */ 
  padding:0px!important;
  margin-top:5px;
  margin-right: 3px;
}
</style>
