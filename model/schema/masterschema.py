from marshmallow import Schema, fields


class StateMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class CityMaster(Schema):
    name = fields.String(required=True)
    state = fields.Nested(StateMaster, only=['name'], many=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class LocalityMaster(Schema):
    name = fields.String(required=True)
    city = fields.Nested(CityMaster, only=['name'], many=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class PropertyType(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class AmenityMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class BuilderMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class BankMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class DimensionSchema(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class FlooringTypeMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class PaintTypeMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class PaintCategoryMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class FacingMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class MartialStatusMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class ProfessionMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class IncomeSlabMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class ReligionMaster(Schema):
    name = fields.String(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()

