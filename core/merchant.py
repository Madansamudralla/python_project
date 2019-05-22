from core.db_connection import DbConnection

class Merchant:
    CONN = None

    def __init__(self):
        self.CONN = DbConnection()

    # TODO: array [key(column_name), value] returns account information from accounts and accountsettings tables.

    # def get_account_details(self, idAccount):
    #     """
    #     Get information from accounts and accountsettings tables.
    #     :type idAccount: int - Vendor account id.
    #     :return array returns account information from accounts and accountsettings tables.
    #     """
    #     try:
    #         with self.CONN.connect_db().cursor() as cursor:
    #             sql = "SELECT * FROM `accounts` " \
    #                   "INNER JOIN `accountsettings` " \
    #                   "ON accounts.`IdAccount`= `accountsettings`.`IdAccount` " \
    #                   "WHERE accounts.`IdAccount`= " + str(idAccount)
    #             cursor.execute(sql)
    #             result = cursor.fetchall()
    #             print(result)
    #     finally:
    #         self.CONN.connect_db().close()

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

    def get_client_code(self, id_account):
        """
        Get ClientCode from accounts table.
        :type id_account: int - Vendor account id.
        :return array - returns ClientCode from accounts table.
        """
        try:
            with self.CONN.connect_db().cursor() as cursor:
                sql = "SELECT ClientCode FROM `accounts` " \
                      "INNER JOIN `accountsettings` " \
                      "ON accounts.`IdAccount`= `accountsettings`.`IdAccount` " \
                      "WHERE accounts.`IdAccount`= " + str(id_account)
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0]
        finally:
            self.CONN.connect_db().close()
