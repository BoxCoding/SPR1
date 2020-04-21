from umongo import Instance, Document, fields, ValidationError, set_gettext
from umongo.marshmallow_bonus import SchemaFromUmongo
from db.mongodb import db

instance = Instance(db)


@instance.register
class LocalityMaster(Document):
    locality_id = fields.IntField(unique=True, required=True)
    name = fields.StringField(required=True)
    city = fields.IntField(required=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()

    class Meta:
        collection = "locality_master"
