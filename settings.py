import logging
import logzero
import os

APP_PORT = "5000"
MONGO_URI = "mongodb+srv://boxcodingtech:YAJvz4Utj28soeBj@spr-0vq0j.gcp.mongodb.net/test?retryWrites=true&w=majority"


def config_logs():
    logzero.logfile("logfile.log", maxBytes=1000000, backupCount=3, loglevel=logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    logzero.formatter(formatter)