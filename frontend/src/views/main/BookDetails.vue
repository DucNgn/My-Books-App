<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary-text">
                    {{ bookTitle }}
                </div>
            </v-card-title>
            <v-card-text>
                <v-container>
                    <div class="d-flex justify-center ma-4"> 
                        <v-img :src=coverPageUrl max-height="400" contain max-width="250" justify="center" class="ml-auto"></v-img>               
                        <div style="display:inline-block;width: 50%; margin-left: 25px;padding:10px;">
                            <h2>Description</h2>
                            <p>{{ bookDescription }}</p>
                        </div>
                        
                    </div>

                </v-container>

                <br />
                <v-divider></v-divider>
                <v-expansion-panel>
                    <v-expansion-panel-content>
                        <template v-slot:header>
                            <div><strong>Book Details</strong></div>
                        </template>
                        <v-card>
                            <v-card-text>
                                <ul>
                                    <li><strong>Author:</strong> {{ bookAuthor }}</li>
                                    <li><strong>Genre:</strong> {{ bookGenre }}</li>
                                    <li><strong>ISBN:</strong> {{ bookISBN }}</li>
                                    <li><strong>Rating:</strong> {{ bookRating }}</li>
                                    <li><strong>Publisher:</strong> {{ bookPublisher }}</li>
                                    <li><strong>Date Published:</strong> {{ bookPublicationYear }}</li>
                                    <li><strong>Number of pages:</strong> {{ bookNumOfPages }}</li>
                                </ul>
                            </v-card-text>
                        </v-card>
                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readCurrentBookInfo } from '@/store/main/getters';
import { IBookInfo } from '@/interfaces';

@Component
export default class Main extends Vue {
    private bookData!: IBookInfo | null;

    public created() {
        this.bookData = readCurrentBookInfo(this.$store);
    }

    get bookDetails() {
        return this.bookData;
    }

    get bookTitle() {
        return this.bookData?.title;
    }

    get bookAuthor() {
        return this.bookData?.author;
    }
    
    get bookRating() {
        return this.bookData?.rating;
    }
    
    get bookDescription() {
        return this.bookData?.description;
    }
    
    get bookPublisher() {
        return this.bookData?.publisher;
    }
    
    get bookPublicationYear() {
        return this.bookData?.publication_year;
    }

    get bookGenre() {
        return this.bookData?.genre;
    }

    get bookISBN() {
        return this.bookData?.isbn;
    }

    get bookNumOfPages() {
        return this.bookData?.num_of_pages;
    }

    get coverPageUrl() {
        return this.bookData?.cover_image_url;
    }

}

</script>