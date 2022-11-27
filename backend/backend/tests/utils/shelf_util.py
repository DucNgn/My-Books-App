from backend import crud, schemas
from typing import List


def create_user(db, email):
    # Set Up
    user_in = schemas.UserCreate(
        email=email,
        password="pwd",
    )
    return crud.user.create(db, obj_in=user_in)


def compare_shelf(shelf1, shelf2) -> bool:
    if shelf1.id != shelf2.id:
        return False
    if shelf1.owner_id != shelf2.owner_id:
        return False
    if shelf1.reading_shelf != shelf2.reading_shelf:
        return False
    if shelf1.toread_shelf != shelf2.toread_shelf:
        return False
    if shelf1.read_shelf != shelf2.toread_shelf:
        return False
    if shelf1.favorite_shelf != shelf2.favorite_shelf:
        return False
    if shelf1.recommendation_shelf != shelf2.recommendation_shelf:
        return False
    return True


def filter_pertinent_ids(list_shelves, shelf_id) -> List:
    to_return = []
    for shelf in list_shelves:
        if shelf.id in shelf_id:
            to_return.append(shelf)
    return to_return
