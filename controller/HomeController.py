#from app import app
from flask import Flask, jsonify, request,Blueprint

home_api = Blueprint('home_api',__name__)


@home_api.route('/home', methods=['GET'])
def get_home():
    return jsonify({"response": "Hello Word"}), 201
