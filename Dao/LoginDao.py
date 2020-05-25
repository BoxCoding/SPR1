from model.schema.LoginDTO import SignUpInfo


def get_by_username(username):
    user = SignUpInfo.find_one({'username': username})
    print("check user")
    return user


def update_user_detail(username, user):
    query = {"username": username}
    return SignUpInfo.update(user)
