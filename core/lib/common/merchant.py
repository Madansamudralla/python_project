from core.lib.database.db_connection import DbConnection
from core.lib.database.db_utilities import DbUtilities


class Merchant:
    CONN = None

    def __init__(self):
        self.CONN = DbConnection()

    def get_account_details(self, id_account, key_name):
        """
        Get information from accounts and accountsettings tables.
        :type id_account: int - Vendor account id.
        :type key_name: str - Key name for desired value from response.
        :return array returns account information from accounts and accountsettings tables.
        """
        try:
            with self.CONN.connect_db().cursor() as cursor:
                sql = """SELECT * FROM `accounts` """ \
                      """INNER JOIN `accountsettings` """ \
                      """ON accounts.`IdAccount`= `accountsettings`.`IdAccount` """ \
                      """WHERE accounts.`IdAccount`= %s"""
                cursor.execute(sql, (id_account, ))
                row_headers = [x[0] for x in cursor.description]  # this will extract row headers
                results = cursor.fetchall()
                key_value = DbUtilities()
                if key_value.fetch_assoc(key_name, results, row_headers) is None:
                    raise Exception("Incorrect or None IdAccount, search for ths Id in Database.")
                else:
                    return key_value.fetch_assoc(key_name, results, row_headers)
        finally:
            self.CONN.connect_db().close()
