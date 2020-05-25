from umongo import Instance, Document, fields, ValidationError, set_gettext, EmbeddedDocument
from db.mongodb import db

instance = Instance(db)


@instance.register
class SignUpInfo(Document):
    username = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)
    email_id = fields.EmailField(required=True)
    validate = fields.BooleanField(default=False)
    role = fields.ListField(fields.StringField())
    type = fields.StringField()
    phone_number = fields.IntegerField()
    created_date = fields.DateTimeField()
    updated_date = fields.DateTimeField()

    class Meta:
        collection = "signup_info"
