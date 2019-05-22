import pymysql
import config_automation
import automation_conf


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
        if self.DB != automation_conf.DATABASE['AUTOMATION']['dbname']:
            raise ValueError("Couldn't not find DB with given name.")
        conn = pymysql.connect(host=automation_conf.DATABASE['AUTOMATION']['host'],
                               user=automation_conf.DATABASE['AUTOMATION']['user'],
                               password=automation_conf.DATABASE['AUTOMATION']['password'],
                               db=automation_conf.DATABASE['AUTOMATION']['dbname'],
                               charset='utf8')
        return conn
