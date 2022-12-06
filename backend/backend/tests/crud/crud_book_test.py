import pytest

from backend.db.session import SessionLocal
from backend import crud, schemas
from backend.tests.utils import book_util

# Variables to use in tests
global base_book
global optional_book
global to_update_session


@pytest.fixture
def db():
    return SessionLocal()


def test_create(db) -> None:
    # Set up
    test_book = schemas.BookCreate(
        title="test_title",
        author="test_author",
        genre="test_genre",
    )
    # Do work
    created = crud.book.create(db, obj_in=test_book)
    global base_book
    base_book = created
    global to_update_session
    to_update_session = db
    # Assert
    assert created.title == "test_title"
    assert created.author == "test_author"
    assert created.genre == "test_genre"


def test_create_optional_parameters(db) -> None:
    # Set up
    test_book = schemas.BookCreate(
        title="test_title",
        author="test_author",
        genre="test_genre",
        isbn="123123",
        publication_year="2022",
        num_of_pages=17,
    )
    # Do work
    created = crud.book.create(db, obj_in=test_book)
    global optional_book
    optional_book = created
    # Assert
    assert created.title == "test_title"
    assert created.author == "test_author"
    assert created.genre == "test_genre"
    assert created.isbn == "123123"
    assert created.publication_year == "2022"
    assert created.num_of_pages == 17
    assert created.cover_image_url is None


def test_get(db) -> None:
    # Do work
    retrieved = crud.book.get(db, base_book.id)
    # Assert
    assert book_util.compare_books(retrieved, base_book)


def test_get_optional_parameters(db) -> None:
    # Do work
    retrieved = crud.book.get(db, optional_book.id)
    # Assert
    assert book_util.compare_books(retrieved, optional_book)


# Note: PLEASE CLEAR DB BEFORE RUNNING TEST TO RUN THIS TEST
# Check if we can retrieve the two we just added in db + start up initial books
def test_get_multi(db) -> None:
    # Do Work
    # Skip the first 100 books since the books we added aren't there
    retrieved = crud.book.get_multi(db, skip=100)
    pertinent = book_util.filter_pertinent_ids(
        retrieved, [base_book.id, optional_book.id]
    )
    # Assert
    # if we did not add any other books by startup script, should only have 3 books in db
    # Length is 77 because we started up db with 175, -100 for skip, +2 for created by tests books
    assert len(retrieved) == 77
    assert book_util.compare_books(pertinent[0], base_book)
    assert book_util.compare_books(pertinent[1], optional_book)


def test_remove(db) -> None:
    # Do work
    deleted = crud.book.remove(db, id=optional_book.id)
    retrieved = crud.book.get(db, deleted.id)
    # Assert
    assert retrieved is None


def test_update(db) -> None:
    # Set Up
    to_update_with = schemas.BookCreate(
        title="changed",
        author="CHANGED",
        genre="test_genre",
    )
    # Do Work
    crud.book.update(to_update_session, db_obj=base_book, obj_in=to_update_with)
    changed = crud.book.get(db, base_book.id)
    # Assert
    assert changed.title == "changed"
    assert changed.author == "CHANGED"
    assert changed.genre == "test_genre"


# Note: PLEASE CLEAR DB BEFORE RUNNING TEST TO RUN THIS TEST
# Check if we can retrieve the two we just added in db + start up initial books
def test_retrieve_suggestions(db) -> None:
    # Set Up
    list_genres = ["test1", "test2", "test3", "test4"]
    list_id = book_util.populate_books(db, list_genres)
    # Do Work
    list_recommended_id = crud.book.get_suggestions(
        db, favorite_genres=[list_genres[0], list_genres[2]]
    )
    # Assert
    # if we did not add any other books by startup script, should only have 10 relevant books in db
    assert len(list_recommended_id) == 10
    for recommended_id in list_recommended_id:
        retrieved = crud.book.get(db, recommended_id)
        assert retrieved.genre == list_genres[0] or list_genres[2]
        assert retrieved.id in list_id


def test_getByTitle(db) -> None:
    # Do Work
    success_retrieved = crud.book.getByTitle(db, "changed")
    # getByTitle searches for exact title
    failed_retrieve = crud.book.getByTitle(db, "chang")
    # Assert
    assert book_util.compare_books(success_retrieved, base_book)
    assert failed_retrieve is None


def test_search_by_title(db) -> None:
    # Do Work
    success_retrieved = crud.book.search_by_title(db, "changed")
    # getByTitle uses fuzzy searches
    success_fuzzy_retrieve = crud.book.search_by_title(db, "chang")
    harry = crud.book.search_by_title(db, "harry")
    # Assert
    assert len(success_retrieved) == 1
    assert book_util.compare_books(success_retrieved[0], base_book)
    assert len(success_fuzzy_retrieve) == 1
    assert book_util.compare_books(success_fuzzy_retrieve[0], base_book)
    assert len(harry) == 6  # There are 6 harry potter books in our start-up db


# this method is used for us to exclude books already in the bookshelves
def test_search_by_title_exclude_ids(db) -> None:
    success_retrieved = crud.book.search_by_title_exclude_ids(
        db, "changed", [base_book.id]
    )
    # getByTitle uses fuzzy searches
    success_fuzzy_retrieve = crud.book.search_by_title_exclude_ids(db, "chang", [])
    # Test on multiple
    to_exclude1 = crud.book.getByTitle(db, "Harry Potter and the Order of the Phoenix")
    to_exclude2 = crud.book.getByTitle(db, "Harry Potter and the Deathly Hallows")
    harry = crud.book.search_by_title_exclude_ids(
        db, "harr", [to_exclude1.id, to_exclude2.id]
    )
    # Assert
    assert len(success_retrieved) == 0
    assert success_retrieved == []
    assert len(success_fuzzy_retrieve) == 1
    assert book_util.compare_books(success_fuzzy_retrieve[0], base_book)
    assert (
        len(harry) == 4
    )  # There are 6 harry potter books in our start-up db, 2 excluded
    assert book_util.book_in_list(harry, to_exclude1) is False
    assert book_util.book_in_list(harry, to_exclude2) is False
