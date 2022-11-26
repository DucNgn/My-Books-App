import pytest

from backend.db.session import SessionLocal
from backend import crud, schemas, db

# Variables to use in tests
global base_book_id
global optional_book_id


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
    global base_book_id
    base_book_id = created.id
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
        isbn=123123,
        publication_year=2022,
        num_of_pages=17
    )
    # Do work
    created = crud.book.create(db, obj_in=test_book)
    global optional_book_id
    optional_book_id = created.id
    # Assert
    assert created.title == "test_title"
    assert created.author == "test_author"
    assert created.genre == "test_genre"
    assert created.isbn == 123123
    assert created.publication_year == 2022
    assert created.num_of_pages == 17
    assert created.cover_image_url is None


def test_get(db) -> None:
    # Do work
    retrieved = crud.book.get(db, base_book_id)
    print(f"this:{retrieved.id}")
    # Assert
    assert retrieved.title == "test_title"
    assert retrieved.author == "test_author"
    assert retrieved.genre == "test_genre"


def test_get_optional_parameters(db) -> None:
    # Do work
    retrieved = crud.book.get(db, optional_book_id)
    print(f"this:{retrieved.id}")
    # Assert
    assert retrieved.title == "test_title"
    assert retrieved.author == "test_author"
    assert retrieved.genre == "test_genre"
    assert retrieved.isbn == 123123
    assert retrieved.publication_year == 2022
    assert retrieved.num_of_pages == 17
    assert retrieved.cover_image_url is None
# How would I test suggestion? Create mock books and then call get preferences on arbitrary list of genres?
