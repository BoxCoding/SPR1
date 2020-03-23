from marshmallow import Schema, fields


class StateMaster(Schema):
    name = fields.Str(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class CityMaster(Schema):
    name = fields.Str(required=True)
    state = fields.Nested(StateMaster, only=['name'], many=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class LocalityMaster(Schema):
    name = fields.Str(required=True)
    city = fields.Nested(CityMaster, only=['name'], many=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class PropertyType(Schema):
    name = fields.Str(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class AmenityMaster(Schema):
    name = fields.Str(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class BuilderMaster(Schema):
    name = fields.Str(required=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


"""class ProjectMaster(Schema):
    name = fields.Str(required=True)
    builder_master = fields.Nested(BuilderMaster,only=['name'],many=True)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()"""
