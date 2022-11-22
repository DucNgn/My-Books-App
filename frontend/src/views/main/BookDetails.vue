<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary-text">
                    {{ bookTitle }}
                </div>
            </v-card-title>
            <v-card-text>
                <v-img :src=coverPageUrl max-height="400" max-width="250"></v-img>
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
import { BookInfo } from '@/store/main/state';

@Component
export default class Main extends Vue {
    private bookData!: BookInfo | null;

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