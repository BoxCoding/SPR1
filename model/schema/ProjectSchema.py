from marshmallow import Schema, fields
from model.schema.masterschema import LocalityMaster, PropertyType,AmenityMaster,BankMaster
from model.schema.Address import AddressSchema
from model.schema.BuilderSchema import BuilderSchema
from model.schema.Specification_master import SpecificationSchema


class ProjectSchema(Schema):
    project_name = fields.String(required=True)
    project_description = fields.String(default=None)
    project_details = fields.String(default=None)
    project_type = fields.Nested(PropertyType, only=['name'], many=True, default=True)
    project_builder = fields.Nested(BuilderSchema,only=['name'])
    project_address = fields.Nested(AddressSchema, many=False,default=True)
    project_location = fields.Nested(LocalityMaster, only=['name'],many=False)
    project_latitude = fields.Float(default=None)
    project_longitude = fields.Float(default=None)
    no_floor = fields.Float(default=None)
    no_tower = fields.Integer(default=None)
    project_area = fields.Float(default=None)
    approved_by = fields.Nested(BankMaster,only=['name'],many=True)
    specifications = fields.Nested(SpecificationSchema, many=True)
    project_highlights = fields.List(fields.String())
    project_usp = fields.List(fields.String())
    amenities = fields.Nested(AmenityMaster, only=['name'], many=True)
    construction_date = fields.Date()
    possession_on = fields.Date()
    construction_status = fields.String(default="Ready to Move")
    booking_percent = fields.Float(default=0, required=True)
    handover_period = fields.Integer(default=45)
    payment_plan = fields.List(fields.String())
    payment_time = fields.Integer()
    near_by = fields.List(fields.String())
    created_date = fields.DateTime()
    updated_date = fields.DateTime()

