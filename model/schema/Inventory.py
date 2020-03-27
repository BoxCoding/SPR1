from marshmallow import Schema, fields
from marshmallow.fields import Integer

from model.schema.masterschema import DimensionSchema,FlooringTypeMaster,PaintCategoryMaster,PaintTypeMaster,PropertyType,FacingMaster
from model.schema.BuilderSchema import BuilderSchema


class InventorySchema(Schema):
    flat_id = fields.Integer(required=True)
    bedroom = fields.Integer(required=True)
    bathroom = fields.Integer(required=True)
    extra_room = fields.Boolean(default=False)
    servant_room = fields.Boolean(default=False)
    floor_size = fields.Integer(required=True)
    size_unit = fields.Nested(DimensionSchema, only=['name'], required=True)
    carpet_area = fields.Integer(default=0)
    balcony_area = fields.Integer(default=0)
    floor_number = fields.Integer()
    facing = fields.Nested(FacingMaster, only=['name'])
    parking = fields.Integer()
    cover_parking = fields.Integer()
    open_parking = fields.Integer()
    guest_parking = fields.Bool(default=False)
    tower_name = fields.String()
    total_flat_in_floor: Integer = fields.Integer(default=1)
    builder_name = fields.Nested(BuilderSchema, many=False)
    flooring_type = fields.Nested(FlooringTypeMaster, only=['name'], many=True)
    paint_type = fields.Nested(PaintTypeMaster, only=['name'])
    paint_category = fields.Nested(PaintCategoryMaster, only=['name'], many=False)
    property_type = fields.Nested(PropertyType, only=['name'])
    society_images_url = fields.List(fields.String())
    bedroom_images_url = fields.List(fields.String())
    bathroom_images_url = fields.List(fields.String())
    floor_plan_url = fields.List(fields.String())
    other_images_url = fields.List(fields.String())
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


    



