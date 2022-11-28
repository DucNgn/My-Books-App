from typing import List


def filter_pertinent_ids(list_users, list_id) -> List:
    to_return = []
    for user in list_users:
        if user.id in list_id:
            to_return.append(user)
    return to_return


def compare_user(user1, user2) -> bool:
    if user1.id != user2.id:
        return False
    if user1.full_name != user2.full_name:
        return False
    if user1.email != user2.email:
        return False
    if user1.hashed_password != user2.hashed_password:
        return False
    if user1.is_active != user2.is_active:
        return False
    if user1.is_superuser != user2.is_superuser:
        return False
    if user1.favorite_genres != user2.favorite_genres:
        return False
    return True
