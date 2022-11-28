import os
import csv

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
            full_name="John Doe",
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            favorite_genres=["Mystery", "Thriller", "Fiction"],
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    shelves = crud.shelves.get_by_owner_id(db, owner_id=user.id)
    if not shelves:
        shelves_in = schemas.ShelvesCreate(
            reading_shelf=['1', '2', '3', '4', '5'], 
            toread_shelf=['6', '7', '8', '9', '10'], 
            read_shelf=['11','12','13','14','15'], 
            favorite_shelf=['1','16'],
            recommendation_shelf=[],
        )
        shelves = crud.shelves.create_with_owner(
            db, obj_in=shelves_in, owner_id=int(user.id)
        )

    instantiate_books(db)


def instantiate_books(db: Session):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'books_data.csv'), mode='r', encoding='utf8') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            does_book_exist = crud.book.getByTitle(db, title=row[0])
            if not does_book_exist:
                book_insert = schemas.Book(
                    title=row[0],
                    author=row[1],
                    rating=row[2],
                    description=row[3],
                    isbn=row[4],
                    genre=row[5],
                    num_of_pages=row[6],
                    publisher=row[7],
                    publication_year=row[8],
                    cover_image_url=row[9]
                )
                book = crud.book.create(db, obj_in=book_insert)
