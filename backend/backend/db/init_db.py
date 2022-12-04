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

    instantiate_users(db)
    instantiate_shelves(db)
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

def instantiate_users(db: Session):
    user1 = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user1:
        user_in = schemas.UserCreate(
            full_name="Admin John Doe",
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            favorite_genres=["Mystery", "Fiction"],
        )
        user1 = crud.user.create(db, obj_in=user_in)  # noqa: F841
    user2 = crud.user.get_by_email(db, email="william.arbour@gmail.com")
    if not user2:
        user_in = schemas.UserCreate(
            full_name="William Arbour",
            email="william.arbour@gmail.com",
            password="costion",
            is_superuser=False,
            favorite_genres=["Romance"],
        )
        user2 = crud.user.create(db, obj_in=user_in)  # noqa: F841
    user3 = crud.user.get_by_email(db, email="ana.miranda@gmail.com")
    if not user3:
        user_in = schemas.UserCreate(
            full_name="Ana Miranda",
            email="ana.miranda@gmail.com",
            password="teranda",
            is_superuser=False,
            favorite_genres=["Graphic Novels", "Horror", "Mystery", "Classics"],
        )
        user3 = crud.user.create(db, obj_in=user_in)  # noqa: F841


def instantiate_shelves(db: Session):
    # USER ID 1
    shelves1 = crud.shelves.get_by_owner_id(db, owner_id=1)
    if not shelves1:
        shelves_in = schemas.ShelvesCreate(
            reading_shelf=['1', '2', '3', '4', '5', '20', '100'], 
            toread_shelf=['6', '7', '8', '9', '10'], 
            read_shelf=['11','12','13','14','15'], 
            favorite_shelf=['12','13'],
            recommendation_shelf=[],
        )
        shelves1 = crud.shelves.create_with_owner(
            db, obj_in=shelves_in, owner_id=int(1)
        )
    # USER ID 2 
    shelves2 = crud.shelves.get_by_owner_id(db, owner_id=2)
    if not shelves2:
        shelves_in = schemas.ShelvesCreate(
            reading_shelf=['16', '17', '18'], 
            toread_shelf=['20'], 
            read_shelf=['19','21','22','23','24', '25','26','27'], 
            favorite_shelf=['22','23','24'],
            recommendation_shelf=[],
        )
        shelves2 = crud.shelves.create_with_owner(
            db, obj_in=shelves_in, owner_id=int(2)
        )
    shelves2 = crud.shelves.get_by_owner_id(db, owner_id=3)
    if not shelves2:
        shelves_in = schemas.ShelvesCreate(
            reading_shelf=['107', '108'], 
            toread_shelf=['100','121','122','123','124','125','127'], 
            read_shelf=['126','27'], 
            favorite_shelf=['126','27'],
            recommendation_shelf=[],
        )
        shelves2 = crud.shelves.create_with_owner(
            db, obj_in=shelves_in, owner_id=int(3)
        )