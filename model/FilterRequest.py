from db.Dbconnection import db
from datetime import datetime, timedelta


class ContentFiltering(db.Model):
    __tablename__ = 'content_filter'
    filter_id=db.Column()
    customer_id=db.Column(db.Integer,db.ForegienKey('users.user_id'))
    property_type=db.Column(db.Integer, db.ForeignKey('property_type_master.id'))
    location = db.Column(db.String)
    min_budget = db.Column(db.Interger,default=100000)
    max_budget = db.column(db.Integer,default=999999999)
    bedrooms = db.Column(db.Integer, default=1)
    description = db.Column(db.String(1000),default=None)
    purpose = db.Column(db.String(1),default='L')
    created_date = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_date = db.Column(db.DateTime(), default=datetime.utcnow())


        



