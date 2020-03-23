from marshmallow import Schema,fields
from model.schema.masterschema import LocalityMaster,CityMaster,StateMaster,PropertyType
from model.schema.user import UserSchema


class BasicFilter(Schema):
    customer_id = fields.Nested(UserSchema,only=['name', 'phone', 'email'],required=True)
    property_type = fields.Nested(PropertyType,only=['name'], many=True)
    location = fields.Nested(LocalityMaster,only=['name'], many=True)
    city = fields.Nested(CityMaster,only=['name'],default=None)
    min_budget = fields.Integer(required=True, default=100000)
    max_budget = fields.Integer(required=True,default=999999999)
    bedrooms = fields.Integer(required=False, default=1)
    description = fields.Str(default=None)
    purpose = fields.Str( default='L')
    created_date = fields.DateTime(default="Now()",required=False)
    updated_date = fields.DateTime(default="Now()", required=False)


