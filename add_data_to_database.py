from mysql.connector import connect, Error
import os


class CreateDatabase:

    def __init__(self):
        self.__dbConn = self.__connect_to_db()
        self.create_db('covid_corona_db_MAKE_RIVA')  # Creating a data base
        self.table_schema = ''
        pass

    def __connect_to_db(db):
        try:
            if db is not None:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                    database=db,
                )
            else:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                )
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def create_db(self, dbName):
        try:
            self.__dbConn.cursor().execute(f'CREATE DATABASE {dbName}')
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def create_table(self, table_name, table_schema):
        try:
            self.__dbConn.cursor().execute(f'CREATE TABLE {table_name} {table_schema}')
            self.__dbConn.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))