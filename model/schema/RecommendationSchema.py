from marshmallow import Schema, fields
from model.schema.ProjectSchema import ProjectSchema
from model.schema.user import UserSchema
from model.schema.masterschema import MartialStatusMaster,ProfessionMaster,IncomeSlabMaster, ReligionMaster,LocalityMaster,CityMaster


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
    project = fields.Nested(ProjectSchema,only=['name'])
    locality = fields.Nested(LocalityMaster, only=['name'])
    city = fields.Nested(CityMaster, only=['name'])
    min_bedrooms = fields.Integer(required=True,default=1)
    max_bedrooms = fields.Integer(required=True,default=10)





