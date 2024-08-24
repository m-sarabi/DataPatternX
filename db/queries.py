import pandas as pd


class QueryExecutor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_pattern_query(self, pattern):
        query_file = pattern
        if not query_file:
            raise ValueError(f"Pattern '{pattern}' not found")

        conn = self.db_connection.get_connection()
        try:
            with open(pattern, 'r') as file:
                query = file.read()

            with conn.cursor() as cur:
                cur.execute(query)
                columns = [col[0] for col in cur.description]
                result = cur.fetchall()

                result_df = pd.DataFrame(result, columns=columns)

                cur.execute("SELECT date, open, high, low, close FROM ohlc_data")
                columns = [col[0] for col in cur.description]
                all_data = cur.fetchall()

                all_data_df = pd.DataFrame(all_data, columns=columns)

        finally:
            self.db_connection.put_connection(conn)

        return result_df, all_data_df
