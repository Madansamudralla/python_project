import os

import peewee

from core import load_yaml


class DbConnection:
    DB = None
    DB_CONFIG_PATH = os.path.join(os.getcwd(), os.sep.join(['core', 'lib', 'database', 'config.yaml']))
    DB_CONFIG = load_yaml(DB_CONFIG_PATH)

    def __init__(self):
        self.DB = 'automation'
        self.connect_db()

    def connect_db(self):
        """
        Establishing database connection.
        :return: Connection to automation DB.
        """
        if self.DB not in self.DB_CONFIG:
            raise ValueError("Couldn't not find DB with given name.")
        mysql = peewee.mysql.connect(host=self.DB_CONFIG[self.DB]['host'],
                                     user=self.DB_CONFIG[self.DB]['user'],
                                     password=self.DB_CONFIG[self.DB]['password'],
                                     db=self.DB_CONFIG[self.DB]['dbname'],
                                     charset='utf8', )
        return mysql
