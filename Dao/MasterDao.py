from umongo import ValidationError

from model.schema.master.UserRole import UserRoleMaster


def save_user_role(userRole):
    if not userRole:
        return None
    try:
        name = userRole['name']
        userrole = UserRoleMaster.find_one({'name':name})
        if userrole is not None:
            return f"{name} already exist"
        resp = userRole.commit()
        
    except ValidationError as ve:
        resp.message=ve.args[0]
        resp.status_code = 400
        return resp
    return resp


def get_user_role_by_id(_id):
    role =  UserRoleMaster.find_one({'id': int(_id)})
    return UserRoleMaster.dump(role)


def get_all_user_role(_id):
    result = []
    roles = UserRoleMaster.find()
    for role in roles:
        result.append(UserRoleMaster.dump(role))
    return result


def get_role_by_name(name):
    role = UserRoleMaster.find_one({'name': name})
    print(role)
    return UserRoleMaster.dump(role)
