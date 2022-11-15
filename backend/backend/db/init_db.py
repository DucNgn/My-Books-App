from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.core.config import settings

from backend.db.base import Base
from backend.db.session import engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    shelves = crud.shelves.get_by_owner_id(db, owner_id=user.id)
    if not shelves:
        shelves_in = schemas.ShelvesCreate(
            reading_shelf=["1", "2", "3"],
            toread_shelf=["5", "6", "7", "8"],
            read_shelf=["9", "10", "11", "12"],
            favorite_shelf=["100", "111", "112"],
        )
        shelves = crud.shelves.create_with_owner(
            db, obj_in=shelves_in, owner_id=int(user.id)
        )

    print(shelves.id)
