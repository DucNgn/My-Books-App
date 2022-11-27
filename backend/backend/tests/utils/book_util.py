from backend import crud, schemas
from typing import List


def populate_books(db, list_genres) -> List:
    list_id = []
    for genre in list_genres:
        for count in range(5):
            test_book = schemas.BookCreate(
                title=f"title{count}",
                author=f"test_author{count}",
                genre=f"{genre}",
            )
            if genre == list_genres[0] or genre == list_genres[2]:
                list_id.append(crud.book.create(db, obj_in=test_book).id)
            else:
                crud.book.create(db, obj_in=test_book)
    return list_id


def filter_pertinent_ids(list_books, list_id) -> List:
    to_return = []
    for book in list_books:
        if book.id in list_id:
            to_return.append(book)
    return to_return


def compare_books(book1, book2) -> bool:
    if book1.id != book2.id:
        return False
    if book1.title != book2.title:
        return False
    if book1.author != book2.author:
        return False
    if book1.genre != book2.genre:
        return False
    if book1.isbn != book1.isbn:
        return False
    if book1.publication_year != book2.publication_year:
        return False
    if book1.num_of_pages != book2.num_of_pages:
        return False
    return True
