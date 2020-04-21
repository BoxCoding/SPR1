from marshmallow import Schema, fields
from model.schema.ProjectSchema import ProjectSchema
from model.schema.user import UserSchema
from model.schema.masterschema import MartialStatusMaster,ProfessionMaster,IncomeSlabMaster, ReligionMaster,LocalityMaster,CityMaster,FurnishingMaster


class CustomerSchema(Schema):
    user_info = fields.Nested(UserSchema,many=False)
    martial_status = fields.Nested(MartialStatusMaster,only=['name'])
    profession = fields.Nested(ProfessionMaster,only=['name'])
    income = fields.Nested(IncomeSlabMaster, only=['name'])
    total_family_numbers = fields.Integer()
    married_members = fields.Integer()
    unmarried_members = fields.Integer()
    female_members = fields.Integer()
    male_members = fields.Integer()
    child_members = fields.Integer()
    religion = fields.Nested(ReligionMaster,only=['name'])
    created_date = fields.DateTime()
    updated_date = fields.DateTime()


class RequirementSchema(Schema):
    project = fields.Nested(ProjectSchema, only=['name'])
    locality = fields.Nested(LocalityMaster, only=['name'])
    city = fields.Nested(CityMaster, only=['name'])
    min_budget = fields.Integer(required=True, default=100000)
    max_budget = fields.Integer(required=True, default=100000000)
    min_bedrooms = fields.Integer(required=True, default=1)
    max_bedrooms = fields.Integer(required=True, default=10)
    min_covered_area = fields.Integer(required=True, default=500)
    parking = fields.Boolean()
    facing = fields.String()
    furnishing_status = fields.Nested(FurnishingMaster,only=['name'],default='Unfurnished',many=True)
    construction_status = fields.String()
    servant_room = fields.Boolean(default=False)
    extra_room = fields.Boolean(default=False)
    created_date = fields.DateTime()
    updated_date = fields.DateTime()









