# Database configuration
import os

class DBConfig(object):
    DB_ON = True
    DB_DRIVER = 'mysql'
    DB_ORM = False

class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'mmh'
    DB_HOST = 'localhost'
    DB_PORT = 3306

    DB_OPTIONS = {
        'unix_socket' : '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

class StagingDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'mydb'
    DB_HOST = 'localhost'
    DB_PORT = 3306

class ProductionDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'mydb'
    DB_HOST = 'localhost'
    DB_PORT = 3306


