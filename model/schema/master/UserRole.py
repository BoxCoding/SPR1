from umongo import Instance, Document, fields, ValidationError, set_gettext
from db import db

instance = Instance(db)


@instance.register
class UserRoleMaster(Document):
    name = fields.StrField(required=True, unique=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()

    class Meta:
        collection = "userrole_master"
