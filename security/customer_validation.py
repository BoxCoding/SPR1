from werkzeug.security import safe_str_cmp
from model.user import UserModel


def authentication_email(email, password):
    user = UserModel.find_by_email(email)
    if user and safe_str_cmp(user.password, password):
        return user


def authentication_phone(phone, password):
    user = UserModel.find_by_phone(phone)
    if user and safe_str_cmp(user.password, password):
        return user