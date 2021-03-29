from mysql.connector import connect, Error
import os


class DatabaseAPI:
    def __init__(self, db_name):
        self.__db_name = db_name
        self.__init_connection = self.__create_init_connection()
        self.create_db()
        self.__connection = self.create_connection()

    # Creates a connection to the database
    def create_connection(self):
        try:
            if self.__db_name is not None:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                    database=self.__db_name
                )
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Creates a connection to MySQL
    def __create_init_connection(self):
        try:
            return connect(
                host="localhost",
                user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
            )
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Created the database with the selected name
    def create_db(self):
        try:
            query = f'CREATE DATABASE {self.__db_name}'
            with self.__init_connection.cursor() as cursor:
                cursor.execute(query)
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Uses the selected database
    def select_db(self):
        try:
            query = f'USE {self.__db_name}'
            with self.__connection.cursor() as cursor:
                cursor.execute(query)
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Creates a table in the database
    def create_table(self, name, schema):
        try:
            query = f'CREATE TABLE `{name}` {schema}'
            with self.__connection.cursor() as cursor:
                cursor.execute(query)
                self.__connection.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Populates the selected table
    def populate_table(self, name, records):
        try:
            query = f"""
            INSERT INTO {name}
            VALUES ( %s {', %s' * (len(records[0]) - 1)} )
            """
            with self.__connection.cursor() as cursor:
                cursor.executemany(query, records)
                self.__connection.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    # Closes the connection to the database and MySQL
    def close_connection(self):
        self.__init_connection.close()
        self.__connection.close()
