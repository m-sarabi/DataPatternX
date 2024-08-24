import pandas as pd
from pattern_query.patterns import get_pattern


class QueryExecutor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_pattern_query(self, patterns, table, fetch_all):
        # query_files = []
        # if not query_file:
        #     raise ValueError(f"Pattern '{pattern}' not found")

        conn = self.db_connection.get_connection()
        results = []
        try:
            with conn.cursor() as cur:
                for pattern in patterns:
                    query_file = get_pattern(pattern)
                    with open(query_file, 'r') as file:
                        query = file.read().replace('{{TABLE_NAME}}', table)

                    cur.execute(query)
                    columns = [col[0] for col in cur.description]
                    result = cur.fetchall()

                    result_df = pd.DataFrame(result, columns=columns)
                    results.append({
                        'name': pattern,
                        'df': result_df
                    })

                if fetch_all:
                    cur.execute("SELECT date, open, high, low, close FROM ohlc_data")
                    columns = [col[0] for col in cur.description]
                    all_data = cur.fetchall()

                    all_data_df = pd.DataFrame(all_data, columns=columns)

        finally:
            self.db_connection.put_connection(conn)

        if fetch_all:
            return results, all_data_df
        else:
            return results
