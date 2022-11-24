import pytest

from backend.db.session import SessionLocal
from backend import crud, schemas, db


# how do I run these test automatically? can't get anything to run
@pytest.fixture
def db():
    return SessionLocal()


@pytest.mark.book
def test_create(db) -> None:
    test_book = schemas.BookCreate(
        title="test_title",
        author="test_author",
        genre="test_genre",
    )
    # Not sure if asserting on return value is good enough
    created = crud.book.create(db, obj_in=test_book)
    # Is this how I use get on book? (Id being title)
    # created = crud.book.get(db, "1")
    assert created["title"] == "test_title"
    assert created["author"] == "test_author"
    assert created["genre"] == "test_genre"

# @pytest.mark.book
# def test_delete(db) -> None:

# How would I test suggestion? Create mock books and then call get preferences on arbitrary list of genres?
