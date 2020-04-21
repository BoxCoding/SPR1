from umongo import Instance, Document, fields, ValidationError, set_gettext,EmbeddedDocument
from umongo.marshmallow_bonus import SchemaFromUmongo
from db.mongodb import db

instance = Instance(db)


@instance.register
class StateMaster(Document):
    state_id = fields.IntField(required=True, unique=True)
    name = fields.StrField(required=True, unique=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()

    class Meta:
        collection = "state_master"


class StateRestrictDate(StateMaster.schema.as_marshmallow_schema()):
    class Meta:
        read_only = ('created_date', "updated_date", 'id')
        load_only = ('created_date', "updated_date", 'id')
