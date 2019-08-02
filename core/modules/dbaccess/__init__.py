import json


from core.modules import GenericFeature


class Dbaccess(GenericFeature):
    """Dbaccess defines the interface to execute actions on a SQL server.
    """
    def get_records(self, query):
        """ Get information from accounts and accountsettings tables.

            args:
                :query (str): MySQL query to update records.

            returns
                An array contains headers table.
                An array contains query result.

        """
        self._res.db.cursor.execute(query)
        row_headers = [x[0] for x in self._res.db.cursor.description]  # this will extract row headers
        results = self._res.db.cursor.fetchall()
        return row_headers, results

    def update_records(self, query):
        """ Get information from accounts and accountsettings tables.

            args:
                :query (str): MySQL query to update records.

        """
        self._res.db.cursor.execute(query)
        self._res.db.cursor.connection.commit()

    def get_account_details(self, id_account, key_name):
        """ Get information from accounts and accountsettings tables.

            args:
                :id_acccount (int): Vendor ID account.
                : key_name (str): The table headers name returned by the query.

            returns
                An array contains account information from accounts and accountsettings tables.

        """

        query = f"SELECT * FROM `accounts` INNER JOIN `accountsettings` ON accounts.`IdAccount`= " \
                f"`accountsettings`.`IdAccount` WHERE accounts.`IdAccount`= {id_account}"
        row_headers, results = self.get_records(query)

        if self.fetch_assoc(key_name, results, row_headers) is None:
            raise Exception("Incorrect or None IdAccount, search for ths Id in Database.")
        else:
            return self.fetch_assoc(key_name, results, row_headers)

    def get_product_status(self, id_account, product_code, key_name):
        """ Get product status from products table.

            args:
                :id_acccount (int): Vendor ID account.
                :product_code (str): Product code
                : key_name (str): The table headers name returned by the query.

            returns
                An string contains product status.

        """

        query = f"SELECT ProductStatus FROM `products` WHERE IdAccount = " \
            f"{id_account} AND ProductCode = '{product_code}'"

        row_headers, results = self.get_records(query)

        if self.fetch_assoc(key_name, results, row_headers) is None:
            raise Exception("Incorrect or None IdAccount, search for ths Id in Database.")
        else:
            return self.fetch_assoc(key_name, results, row_headers)

    def get_subscription_reference(self, licence_code, key_name):
        """ Get subscription reference from licences table.

            args:
                :licence_code (str): Licence code
                : key_name (str): The table headers name returned by the query.

            returns
                An string contains product status.

        """
        query = f"SELECT LicenceCode FROM `licences` WHERE LicenceCode = '{licence_code}'"

        row_headers, results = self.get_records(query)

        if self.fetch_assoc(key_name, results, row_headers) is None:
            raise Exception("Incorrect or None LicenseCode, search for ths Id in Database.")
        else:
            return self.fetch_assoc(key_name, results, row_headers)

    def fetch_assoc(self, key_name, results, row_headers):
        """ Convert DB query response to dictionary object and return specific key value from it.

                args:
                    :key_name: the table headers name returned by the query
                    :results: list of db query response
                    :row_headers: list of db query headers

                :return string value from dict type object or None if key not present in dict.

        """
        json_data = []
        try:
            for result in results:
                json_data.append(dict(zip(row_headers, result)))
                query_result = json.dumps(json_data, default=str)
                json_string = query_result.replace("'", "\"")
                json_to_dict = json.loads(json_string)[0]
                return json_to_dict[key_name]
        except KeyError:
            return None
