import json


class DbUtilities:

    @staticmethod
    def fetch_assoc(key_name, results, row_headers):
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
