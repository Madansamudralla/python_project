from core.lib.database.db_connection import DbConnection
from core.lib.database.db_utilities import DbUtilities
import os
from core import load_yaml


class Merchant:
    CONN = None
    DB_CONFIG_PATH = os.path.join(os.getcwd(), os.sep.join(['core', 'lib', 'database', 'db_query.yaml']))
    DB_CONFIG = load_yaml(DB_CONFIG_PATH)

    def __init__(self):
        self.CONN = DbConnection()

    def get_account_details(self, id_account, key_name):
        """ Get information from accounts and accountsettings tables.

            args:
                :id_acccount: vendor account id
                :key_name: the table headers name returned by the query

            :return array returns account information from accounts and accountsettings tables.

        """
        try:
            with self.CONN.connect_db().cursor() as cursor:
                cursor.execute(self.DB_CONFIG['merchant']['get_account_details'], (id_account, ))
                row_headers = [x[0] for x in cursor.description]  # this will extract row headers
                results = cursor.fetchall()
                key_value = DbUtilities()
                if key_value.fetch_assoc(key_name, results, row_headers) is None:
                    raise Exception("Incorrect or None IdAccount, search for ths Id in Database.")
                else:
                    return key_value.fetch_assoc(key_name, results, row_headers)
        finally:
            self.CONN.connect_db().close()
