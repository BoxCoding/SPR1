from marshmallow import Schema, fields
from model.schema.masterschema import LocalityMaster,CityMaster,StateMaster
from model.schema.Address import AddressSchema


class BuilderSchema(Schema):
    builder_name = fields.Str(required=True)
    builder_description = fields.Str(default=None, required=False)
    projects_locations = fields.Nested(LocalityMaster, only=['name'], many=True)
    builder_address = fields.Nested(AddressSchema, many=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()
