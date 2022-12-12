from flask import Flask
#instance_relative_config=True para poder usar el fichero config.py
app= Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from registros_ig.routes import *
