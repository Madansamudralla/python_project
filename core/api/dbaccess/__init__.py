import json


from core.api import GenericFeature


class Dbaccess(GenericFeature):
    """Dbaccess defines the interface to execute actions on a SQL server.
    """
    def send_query(self, query):
        self._res.db.cursor.execute(query)
        row_headers = [x[0] for x in self._res.db.cursor.description]  # this will extract row headers
        results = self._res.db.cursor.fetchall()
        return row_headers, results

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
        row_headers, results = self.send_query(query)

        if self.fetch_assoc(key_name, results, row_headers) is None:
            raise Exception("Incorrect or None IdAccount, search for ths Id in Database.")
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
