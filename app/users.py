def add_user(users, name, email):
    busq = search_user_by_email(users, email)
    if len(users) == 0:
            id_user = 1
    else:
        id_user = users[0]["id_user"]
        for b in users:
            if b["id_user"] >= id_user:
                id_user = b["id_user"] + 1
                
    if busq is None:
        user = {
            "id_user" : id_user,
            "name" : name,
            "email" : email
        }
        users.append(user)
        print("Ingreso usuario exitoso")
        return 
    print("El correo ya esta en uso")
    return None


def search_user_by_email(users, email):
    for u in users:
        if u["email"].lower() == email.strip().lower():
            return u
    return None

def list_users(users):
    return users

def search_user_by_id(users, id):
    for u in users:
        if u["id_user"] == id:
            return (u)
    return None