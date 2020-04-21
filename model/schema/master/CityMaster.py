from umongo import Instance, Document, fields, ValidationError, set_gettext, EmbeddedDocument
from db.mongodb import db

instance = Instance(db)





@instance.register
class CityMaster(Document):
    city_id = fields.IntegerField(required=True, unique=True)
    name = fields.StrField(required=True, unique=True)
    state = fields.IntField(required=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()

    class Meta:
        collection = "city_master"


class CityRestrictDate(CityMaster.schema.as_marshmallow_schema()):
    class Meta:
        read_only = ('created_date', "updated_date", 'id')
        load_only = ('created_date', "updated_date", 'id')