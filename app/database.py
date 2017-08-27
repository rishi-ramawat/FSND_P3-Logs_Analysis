#!/usr/bin/env python3

from psycopg2 import pool
import settings


class Database():

    # @classproperty
    __connection_pool = None

    @classmethod
    def initialize(cls):
        if cls.__connection_pool is None:
            cls.__connection_pool = pool.SimpleConnectionPool(
                1,
                3,
                user=settings.DB_USERNAME,
                password=settings.DB_PASSWORD,
                database=settings.DB_DATABASE,
                host=settings.DB_HOST
            )

    @classmethod
    def getConnection(cls):
        if cls.__connection_pool is None:
            cls.initialize()

        return cls.__connection_pool.getconn()

    @classmethod
    def returnConnection(cls, connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def closeAllConnections(cls):
        cls.__connection_pool.closeall()
        cls.__connection_pool = None


class Cursor():

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.getConnection()
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.cursor.close()
        Database.returnConnection(self.connection)
