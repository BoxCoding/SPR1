from umongo import Instance, Document, fields, ValidationError, set_gettext
from db import db

instance = Instance(db)


@instance.register
class UserTypeMaster(Document):
    name = fields.StrField(required=True, unique=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()
    nested = fields.ReferenceField

    class Meta:
        collection = "usertype_master"


class RestrictDate(UserTypeMaster.schema.as_marshmallow_schema()):
    class Meta:
        read_only = ('created_date', "updated_date", 'id')
        load_only = ('created_date', "updated_date", 'id')
