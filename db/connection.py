import os
from psycopg2 import pool
from config.config import DATABASE_URL


class DBConnection:
    def __init__(self):
        self.pool = pool.SimpleConnectionPool(1, 10, DATABASE_URL)

    def get_connection(self):
        return self.pool.getconn()

    def put_connection(self, conn):
        self.pool.putconn(conn)

    def close_connection(self):
        self.pool.closeall()
