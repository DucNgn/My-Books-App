import pytest

from backend.db.session import SessionLocal
from backend import crud, schemas
from backend.tests.utils import shelf_util

global first_shelf
global test_user
global test_shelf
global to_update_session


@pytest.fixture
def db():
    return SessionLocal()


# did not do base create() since would never be called
def test_create(db) -> None:
    created = schemas.ShelvesCreate(
        owner_id=2,
        reading_shelf=["1"],
        toread_shelf=["1"],
        read_shelf=["1"],
        favorite_shelf=["1"],
        recommendation_shelf=["1"],
    )
    global first_shelf
    first_shelf = crud.shelves.create(db, obj_in=created)
    # Assert
    assert first_shelf.id == 4  # 2 since there already exist 3 shelf from db startup
    assert first_shelf.reading_shelf == ["1"]
    assert first_shelf.toread_shelf == ["1"]
    assert first_shelf.read_shelf == ["1"]
    assert first_shelf.favorite_shelf == ["1"]
    assert first_shelf.recommendation_shelf == ["1"]


def test_create_with_owner(db) -> None:
    # Set Up
    global test_user
    test_user = shelf_util.create_user(db, "first@email.com")
    shelves_in = schemas.ShelvesCreate(
        reading_shelf=["1"],
        toread_shelf=[],
        read_shelf=[],
        favorite_shelf=[],
        recommendation_shelf=[]
    )
    # Do Work
    global test_shelf
    test_shelf = crud.shelves.create_with_owner(db, obj_in=shelves_in, owner_id=test_user.id)
    global to_update_session
    to_update_session = db
    # Assert
    assert test_shelf.id == 5  # 5 since there already exist shelves created from db startup
    assert test_shelf.reading_shelf == ["1"]
    assert test_shelf.toread_shelf == []
    assert test_shelf.read_shelf == []
    assert test_shelf.favorite_shelf == []
    assert test_shelf.recommendation_shelf == []


def test_get_by_owner_id(db) -> None:
    # Do Work
    retrieved = crud.shelves.get_by_owner_id(db, test_user.id)
    # Assert
    assert shelf_util.compare_shelf(retrieved, test_shelf)


def test_get(db) -> None:
    # Do Work
    retrieved = crud.shelves.get(db, test_shelf.id)
    # Assert
    assert shelf_util.compare_shelf(retrieved, test_shelf)


# get multi has no query for shelves, did not write test for it

def test_update(db) -> None:
    # Set Up
    to_update_with = schemas.ShelvesCreate(
        reading_shelf=["1"],
        toread_shelf=["2"],
        read_shelf=["3"],
        favorite_shelf=["4"],
        recommendation_shelf=["5", "6", "7"],
    )
    # Do Work
    crud.shelves.update(to_update_session, db_obj=test_shelf, obj_in=to_update_with)
    changed = crud.shelves.get(db, test_shelf.id)
    # Assert
    assert changed.reading_shelf == ["1"]
    assert changed.toread_shelf == ["2"]
    assert changed.read_shelf == ["3"]
    assert changed.favorite_shelf == ["4"]
    assert changed.recommendation_shelf == ["5", "6", "7"]


def test_remove(db) -> None:
    # Do work
    deleted = crud.shelves.remove(db, id=test_shelf.id)
    retrieved = crud.shelves.get(db, deleted.id)
    # Assert
    assert retrieved is None

# TODO: test update where going from reading to to read removes from reading
