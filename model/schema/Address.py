from marshmallow import Schema, fields
from model.schema.masterschema import LocalityMaster,CityMaster,StateMaster


class AddressSchema(Schema):
    address_1 = fields.Str(required=True)
    address_2 = fields.Str(required=False)
    address_3 = fields.Str(required=False)
    landmark = fields.Str(required=False)
    locality = fields.Nested(LocalityMaster,only=['name'])
    city = fields.Nested(CityMaster,only=['name'])
    state = fields.Nested(StateMaster,only=['name'])
    created_date = fields.DateTime()
    updated_date = fields.DateTime()
