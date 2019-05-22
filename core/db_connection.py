import peewee
import config_automation
import automation_cnf


class DbConnection:
    DB = None

    def __init__(self):
        self.DB = config_automation.Config.DB_ENVIRONMENT
        self.connect_db()

    def connect_db(self):
        """
        Establishing database connection.
        :return: Connection to automation DB.
        """
        if self.DB != automation_cnf.DATABASE['AUTOMATION']['dbname']:
            raise ValueError("Couldn't not find DB with given name.")
        mysql = peewee.mysql.connect(host=automation_cnf.DATABASE['AUTOMATION']['host'],
                                     user=automation_cnf.DATABASE['AUTOMATION']['user'],
                                     password=automation_cnf.DATABASE['AUTOMATION']['password'],
                                     db=automation_cnf.DATABASE['AUTOMATION']['dbname'],
                                     charset='utf8', )
        return mysql
