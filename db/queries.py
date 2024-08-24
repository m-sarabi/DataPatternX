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
            with open('pattern_queries/dummy.sql', 'r') as file:
                query = file.read()

            with conn.cursor() as cur:
                cur.execute(query)
                columns = [col[0] for col in cur.description]
                result = cur.fetchall()

                df = pd.DataFrame(result, columns=columns)

        finally:
            self.db_connection.put_connection(conn)

        return df
