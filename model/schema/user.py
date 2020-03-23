from marshmallow import Schema, fields
from model.schema.masterschema import CityMaster, LocalityMaster


class UserSchema(Schema):
    first_name=fields.Str(required=False)
    last_name = fields.Str(required=False)
    age = fields.Int(required=False)
    gender = fields.Str(required=False)
    phone = fields.Integer(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    locality = fields.Nested(LocalityMaster,only=['name'])
    city = fields.Nested(CityMaster,only=['name'])
    is_active = fields.Boolean(default=True)
    created_date = fields.DateTime(default="Now()")
    updated_date = fields.DateTime(default="Now()")






