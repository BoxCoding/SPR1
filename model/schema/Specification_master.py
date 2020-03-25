from marshmallow import Schema, fields


class SpecificationSchema(Schema):
    specification = fields.List(fields.String(required=True))
    flooring = fields.List(fields.String())
    walls = fields.List(fields.String())
    kitchen = fields.String()
    windows = fields.List(fields.String())
    doors = fields.List(fields.String())
    floor_to_ceilling = fields.List(fields.String())

