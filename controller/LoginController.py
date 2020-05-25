from flask import jsonify, request, Blueprint, abort
import datetime as dt
from bson import ObjectId
from model.schema.master.UserTypeMaster import UserTypeMaster, RestrictDate
from model.schema.LoginDTO import SignUpInfo
from umongo import ValidationError
from service import get_hash_password, get_password, check_email
from service.signupService import update_user_info

login_api = Blueprint('login_api', __name__)


@login_api.route('/l/signup', methods=['POST','PUT'])
def add_usertype():
    payload = request.get_json()
    if payload is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    try:
        pwd = payload['password']
        hash_pwd = get_hash_password(pwd)
        payload['password'] = hash_pwd
        payload['validate'] = False
        payload['created_date'] = dt.datetime.utcnow()
        email = payload['email_id']
        sign_up = SignUpInfo.find_one({'email_id' : email})
        if sign_up:
            return jsonify({'response':f'{email} already registered please login'})

        phone_number = payload['phone_number']
        sign_up = SignUpInfo.find_one({'phone_number': phone_number})
        if sign_up:
            return jsonify({'response':f'{phone_number} already registered please login'})
        payload['username'] = get_hash_password(str(phone_number))

        if check_email(email) is False:
            return jsonify({"response": "Invalid email id"})
        signup = SignUpInfo(**payload)
        signup.commit()
    except ValidationError as ve:
        resp = jsonify(message=ve.args[0])
        resp.status_code = 400
        return resp
    return jsonify({"response": f"User {payload['emailid']} has been successfully created"}), 201


@login_api.route('/l/signup/<string:username>', methods=['PUT'])
def update_user_roles(username):
    payload = request.get_json()
    signupinfo = SignUpInfo(**payload)
    print(signupinfo)
    result = update_user_info(signupinfo)
    return jsonify({'response': result})

