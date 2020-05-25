import base64
import re
import datetime as dt

from Dao.LoginDao import get_by_username, update_user_detail
from model.schema.LoginDTO import SignUpInfo

regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"


def get_hash_password(password, **kwargs):
    pw_hash = base64.b64encode(password.encode("utf-8"))
    return pw_hash


def get_password(hash_paswword, **kwargs):
    password = base64.b64decode(hash_paswword).decode("utf-8")
    return password


def check_email(email):
    # pass the regualar expression
    # and the string in search() method
    if re.search(regex, email):
        return True
    else:
        return False


def update_user_info(signup):
    username = signup['username']
    user = get_by_username(username)
    if not user:
        return "No Record found"
    signup['updated_date'] = dt.datetime.utcnow()
    userInfo = signup
    result = update_user_detail(username, userInfo)
    print(result)
    return result
