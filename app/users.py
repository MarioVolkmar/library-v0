def add_user(users, name, email):
    if search_user_by_email(users, email) == None:
        id = len(users) + 1
        user = {
            "id" : int(id),
            "name" : name,
            "email" : email
        }
        users.append(user)
        return
    return None


def search_user_by_email(users, email):
    for u in users:
        if u["email"] == email.strip():
            return u
    return None

def list_users(users):
    return users

def search_user_by_id(users, id):
    for u in users:
        if u["id"] == id:
            return (u)
    return None