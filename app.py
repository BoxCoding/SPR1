import os
from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt import JWT
#from db.mongodb import MongoDb
import os
import settings
from controller.HomeController import home_api
from controller.MasterController import master_api
from controller.LoginController import login_api
from flask_swagger_ui import get_swaggerui_blueprint



app = Flask(__name__)
app.register_blueprint(home_api)
app.register_blueprint(master_api)
app.register_blueprint(login_api)



SWAGGER_URL='/spec'
API_URL='/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SPR -Magical Recommendation Using AI"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

"""@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Magical Property Recommendation"
    return jsonify(swag)
"""

if __name__ == '__main__':
    settings.config_logs()
    print(settings.MONGO_URI.strip())
    #app.config["mongo"] = MongoDb()
    app.run(debug=True, port=settings.APP_PORT)