from flask_restful import Resource, reqparse
from model.user import UserModel


class CustomerRegistration(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str
    )
    parser.add_argument(
        'phone',
        type=str,
        required=True
    )
    parser.add_argument(
        'password',
        type=str,
        required=True
    )

    def post(self):

        data=CustomerRegistration.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"response":"email is duplicate"},400
        elif UserModel.find_by_id(data['phone']):
            return{
                "response" : "phone number is duplicate"
            },400
        else:
            user=UserModel(**data)
            user.save_to_db()
            return {
                "response":"User created successfully"
            },201
