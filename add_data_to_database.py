from mysql.connector import connect, Error
import os


class CreateDatabase:

    def __init__(self):
        self.conn = self.__connect_to_db()
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
        except Error as e:
            print('There as a problem with the db: {}'.format(e))

    def create_db(self, dbName):
        try:
            self.__dbConn.cursor().execute(f'CREATE DATABASE {dbName}')
        except Error as err:
            print('There as a problem with the db: {}'.format(err))