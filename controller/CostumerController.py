import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, idendity
