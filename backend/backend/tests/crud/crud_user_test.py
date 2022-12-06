import pytest

from backend.db.session import SessionLocal
from backend import crud, schemas
from backend.core.security import verify_password
from backend.tests.utils import user_util

global test_user
test_password = "test_password1"
global optional_test_user
global to_update_session


@pytest.fixture
def db():
    return SessionLocal()


def test_create(db) -> None:
    # Set Up
    user_in = schemas.UserCreate(
        email="test_email@email.com",
        password=test_password,
    )
    # Do Work
    user = crud.user.create(db, obj_in=user_in)
    global test_user
    test_user = user
    global to_update_session
    to_update_session = db
    # Assert
    assert user.email == "test_email@email.com"
    assert verify_password(test_password, user.hashed_password)
    assert user.is_superuser is False


def test_create_optional_parameters(db) -> None:
    # Set Up
    user_in = schemas.UserCreate(
        email="test_email_optional@email.com",
        password=test_password,
        full_name="John Doe",
        is_superuser=True,
        favorite_genres=["fantasy", "comedy"],
    )
    # Do Work
    global optional_test_user
    user = crud.user.create(db, obj_in=user_in)
    optional_test_user = user
    # Assert
    assert user.email == "test_email_optional@email.com"
    assert verify_password(test_password, user.hashed_password)
    assert user.is_superuser
    assert user.favorite_genres == ["fantasy", "comedy"]


def test_get(db) -> None:
    # Do Work
    retrieved = crud.user.get(db, test_user.id)
    # Assume
    assert user_util.compare_user(retrieved, test_user)


def test_get_optional_parameters(db) -> None:
    # Do Work
    retrieved = crud.user.get(db, optional_test_user.id)
    # Assume
    assert user_util.compare_user(retrieved, optional_test_user)


def test_get_by_email(db) -> None:
    # Do Work
    retrieved = crud.user.get_by_email(db, email=test_user.email)
    # Assume
    assert user_util.compare_user(retrieved, test_user)


def test_get_multi(db) -> None:
    # Do Work
    retrieved = crud.user.get_multi(db)
    pertinent = user_util.filter_pertinent_ids(
        retrieved, [test_user.id, optional_test_user.id]
    )
    # Assert
    # Can't actually assert length of all users since we create users in test crud_shelf
    # retrieved is for sure > pertinent though because of default user
    assert len(retrieved) > len(pertinent)
    assert user_util.compare_user(pertinent[0], test_user)
    assert user_util.compare_user(pertinent[1], optional_test_user)


def test_update(db) -> None:
    # Set Up
    to_update_with = schemas.UserCreate(
        email="changed@email.com",
        password="changed1",
        full_name="John Doe",
        favorite_genres=["fantasy", "comedy", "horror"],
    )
    # Do Work
    crud.user.update(to_update_session, db_obj=test_user, obj_in=to_update_with)
    changed = crud.user.get(db, test_user.id)
    global test_password
    test_password = "changed1"
    # Assert
    assert changed.email == "changed@email.com"
    assert verify_password("changed1", changed.hashed_password)
    assert changed.favorite_genres == ["fantasy", "comedy", "horror"]


def test_authenticate(db) -> None:
    # Do Work
    retrieved = crud.user.authenticate(
        db, email=test_user.email, password=test_password
    )
    # Assert
    assert user_util.compare_user(retrieved, test_user)


# A newly created user should be active
def test_is_active(db) -> None:
    # Set Up
    user_in = schemas.UserCreate(
        email="test_active@email.com",
        password=test_password,
    )
    # Do Work
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    # Assert
    assert is_active


def test_is_superuser(db) -> None:
    # Do Work
    default_is_superuser = crud.user.is_superuser(crud.user.get(db, 1))
    optional_is_superuser = crud.user.is_superuser(optional_test_user)
    # Assert
    assert default_is_superuser
    assert optional_is_superuser


def test_remove(db) -> None:
    # Do work
    deleted = crud.user.remove(db, id=test_user.id)
    retrieved = crud.user.get(db, deleted.id)
    # Assert
    assert retrieved is None
