import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#from db.mongodb import MongoDb
import os
import settings
from controller.HomeController import home_api
from controller.MasterController import master_api


app = Flask(__name__)
app.register_blueprint(home_api)
app.register_blueprint(master_api)
#app.config['MONGOALCHEMY_DATABASE']='SPR'
#app.config['MONGOALCHEMY_CONNECTION_STRING']="mongodb+srv://boxcodingtech:motoe1234@spr-0vq0j.gcp.mongodb.net/test?retryWrites=true&wß=majority"
#api = Api(app)




if __name__ == '__main__':
    settings.config_logs()
    print(settings.MONGO_URI.strip())
    #app.config["mongo"] = MongoDb()
    app.run(debug=True, port=settings.APP_PORT)