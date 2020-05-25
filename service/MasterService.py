

from Dao.MasterDao import save_user_role,get_user_role_by_id,get_all_user_role,get_role_by_name
from model.schema.master.UserRole import UserRoleMaster
import datetime as dt


def post_user_role(master):
    print(master)
    user_master = UserRoleMaster()
    user_master['name'] = master['name']
    user_master['created_date'] = dt.datetime.utcnow()
    response = save_user_role(user_master)
    return response


def get_user_role_service(_id):

    if not _id:
        print(_id)
        return None
    result = None
    if _id.isnumeric():
        result = get_user_role_by_id(_id)
    elif _id == 'all':
        result = get_all_user_role(_id)
    else:
        print("name")
        result = get_role_by_name(_id)
    return result






