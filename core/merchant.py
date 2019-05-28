from core.db_connection import DbConnection
from core.common.db_utilities import DbUtilities


class Merchant:
    CONN = None

    def __init__(self):
        self.CONN = DbConnection()

    def get_account_details(self, id_account, key_name):
        """
        Get information from accounts and accountsettings tables.
        :type id_account: int - Vendor account id.
        :type key_name: string - Key name for desired value from response.
        :return array returns account information from accounts and accountsettings tables.
        """
        try:
            with self.CONN.connect_db().cursor() as cursor:
                sql = "SELECT * FROM `accounts` " \
                      "INNER JOIN `accountsettings` " \
                      "ON accounts.`IdAccount`= `accountsettings`.`IdAccount` " \
                      "WHERE accounts.`IdAccount`= " + str(id_account)
                cursor.execute(sql)
                row_headers = [x[0] for x in cursor.description]  # this will extract row headers
                results = cursor.fetchall()
                key_value = DbUtilities()
                return key_value.fetch_assoc(key_name, results, row_headers)

        finally:
            self.CONN.connect_db().close()

    def get_ipn_key(self, id_account):
        """
        Get IpnKey from accountsettings table.
        :type id_account: int - Vendor account id.
        :return array - returns IpNKey from accountsettings table.
        """
        try:
            with self.CONN.connect_db().cursor() as cursor:
                sql = "SELECT IpNKey FROM `accounts` " \
                      "INNER JOIN `accountsettings` " \
                      "ON accounts.`IdAccount`= `accountsettings`.`IdAccount` " \
                      "WHERE accounts.`IdAccount`= " + str(id_account)
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0]
        finally:
            self.CONN.connect_db().close()
