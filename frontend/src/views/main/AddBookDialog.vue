<template>
    <v-dialog v-model="isShowingDialog" persistent max-width="1000px">
        <v-card>
            <v-card-title>
                <span class="text-h5">Add New Book</span>
            </v-card-title>
            <v-card-text>
                <v-container>
                    <v-text-field v-model="queryInput" ref="queryInput" @keyup="performSearch($event)"
                        label="Book's Name" hint="Type in the exact name of the book for better results">
                    </v-text-field>
                </v-container>
                <vue-good-table ref="table" :columns="headers" :rows="searchResults" :select-options="{ enabled: true }"
                    @on-selected-rows-change="selectionChanged">
                    <div slot="selected-row-actions">
                        <button @click="addBooksToShelf">Add to Library</button>
                    </div>
                </vue-good-table>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click.stop="closeDialog">
                    Close
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IBookInfo } from '@/interfaces';
import { readPersonalShelves, readShowAddBookDialog, readBookSearchResults } from '@/store/main/getters';
import { commitIsShowingAddBookDialog, commitRemoveBookSearchResults } from '@/store/main/mutations';
import { dispatchUpdateShelves, dispatchSearchBooksByTitle } from '@/store/main/actions';
import { VueGoodTable } from 'vue-good-table';
import 'vue-good-table/dist/vue-good-table.css';


Vue.component('vue-good-table', VueGoodTable);


@Component
export default class AddBookDialog extends Vue {
    public queryInput: string = '';
    public rowSelection: IBookInfo[] = [];

    public timer: number | undefined;
    public performSearch(e) {
        clearTimeout(this.timer);
        this.timer = setTimeout(() => {
            const bookTitle = e.srcElement._value;
            dispatchSearchBooksByTitle(this.$store, { book_title: bookTitle });
        }, 500);
    }

    get headers() {
        return [
            { label: 'Title', field: 'title' },
            { label: 'Author', field: 'author' },
            { label: 'Genre', field: 'genre' },
            { label: 'ISBN', field: 'isbn' },
            { label: 'Number of pages', field: 'num_of_pages' },
        ];
    }

    public selectionChanged(params) {
        this.rowSelection = params.selectedRows;
    }

    get searchResults() {
        return readBookSearchResults(this.$store);
    }

    public addBooksToShelf() {
        const newBookIDs: string[] = [];
        this.rowSelection.forEach((element) => newBookIDs.push(element.id));
        const personalShelves = readPersonalShelves(this.$store);
        const toReadBookIDs: string[] = [];
        personalShelves?.toread_shelf.forEach((book) => toReadBookIDs.push(book.id));
        const newToReadBookIDs = toReadBookIDs.concat(newBookIDs);
        dispatchUpdateShelves(this.$store, { toread_shelf: newToReadBookIDs });
        this.closeDialog();
    }

    get isShowingDialog() {
        return readShowAddBookDialog(this.$store);
    }

    public closeDialog() {
        commitRemoveBookSearchResults(this.$store);
        commitIsShowingAddBookDialog(this.$store, false);
        this.queryInput = '';
    }
}
</script>