class QueryExecutor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_query(self, query_file):
        conn = self.db_connection.get_connection()
        try:
            with open(query_file, 'r') as file:
                query = file.read()

            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

        finally:
            self.db_connection.put_connection(conn)

        return result
