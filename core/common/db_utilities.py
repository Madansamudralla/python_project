import json


class DbUtilities:

    @staticmethod
    def fetch_assoc(key_name, results, row_headers):
        """
        Convert lists from db query response to dictionary object and return specific key value from it.
        :type key_name: string - Key name for desired value.
        :type results: list type object.
        :type row_headers: list type object.
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
