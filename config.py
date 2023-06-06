import os


class Config:
    class DataBase:
        PASSWORD = 'qwerty'
        HOST = "db" if 'DOCKER_CONTAINER' in os.environ else "localhost"
        DB = "postgres"
        USERNAME = "postgres"
        PORT = 5432

    class Web:
        PORT = 5000
        HOST = "0.0.0.0"
        DEBUG = True

    class ResponseStatusCode:
        OK = 200
        NOT_FOUND = 404
        BAD_REQUEST = 400

    BASE_URL = f"http://{Web.HOST}:{Web.PORT}"


class Appication:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{Config.DataBase.USERNAME}:{Config.DataBase.PASSWORD}@{Config.DataBase.HOST}:{Config.DataBase.PORT}/{Config.DataBase.DB}"
