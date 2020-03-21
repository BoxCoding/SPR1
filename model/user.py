from db.Dbconnection import db
from datetime import datetime, timedelta


class UserModel(db.Model):
    __tablename__= 'users'
    user_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    email = db.Column(db.String(50),unique=True)
    phone=db.Column(db.String(30),unique=True)
    password = db.Column(db.String(30))
    locality_id = db.Column(db.Integer,db.ForeignKey('locality_master.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city_master.id'))
    is_active=db.Column(db.Integer)
    created_date=db.Column(db.DateTime(),default=datetime.utcnow())


    def __init__(self,user_id, first_name, last_name, age, gender,email,password, locality_id,city_id):
        self.user_id=user_id
        self.first_name=first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.password = password
        self.locality_id = locality_id
        self.city_id = city_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
        # 使用sqlite3連結sqlite資料庫
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     # user = cls(row[0], row[1], row[2])
        #     # cls(*row,)會自動擴展成上面格式
        #     user = cls(*row,)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()