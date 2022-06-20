from flask import Flask, session, render_template
import pymysql
from flask_sqlalchemy import SQLAlchemy
from Config import Config
pymysql.install_as_MySQLdb()


class App:
    __app = None
    __db = None

    @classmethod
    def initialize(cls):
        # initialize the app, add configuration, make connection to mysql database
        app = Flask(__name__)

        app.config.from_object(Config)

        db = SQLAlchemy(app)

        App.__app = app
        App.__db = db

    @classmethod
    def get_flask_instance(cls):
        return cls.__app

    @classmethod
    def get_db(cls):
        return cls.__db

    @classmethod
    def run_instance(cls):
        app = cls.__app
        print(app.url_map)
        return app.run(host='0.0.0.0', port=8080)
