from mysql.connector import connect, Error
import os


class CreateDatabase:

    def __init__(self, date):
        self.__date = date
        self.__db_name = None  # 'covid_corona_db_MAKE_RIVA'
        self.__connection = self.__connect_to_db()
        # self.table_name = f'covid_data{self.__date}'
        self.__table_schema = '(rank, Country,Other, TotalCases, NewCases, TotalDeaths, NewDeaths, TotalRecovered, NewRecovered, ActiveCases, Serious,Critical, Tot Cases/1M pop, Deaths/1M pop, TotalTests, Tests/1M pop, Population, Continent, 1 Caseevery X ppl, 1 Deathevery X ppl, 1 Testevery X ppl)'
        self.__data = None
        self.__table_name = None

    def store_data(self, data):
        #     self.__create_db()
        #     self.__data = data
        # self.__select_db()
        self.__create_db_tables_keys()
        self.__populate_table(self.__table_name, data)
        self.__closeDatabase()

    def __connect_to_db(self):
        try:
            if self.__db_name is not None:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                    # database=self.__db_name,
                )
            else:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                )
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __create_db(self):
        try:
            self.__connection.cursor().execute(f'CREATE DATABASE {self.__db_name}')
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __select_db(self, selected_db):
        mycursor = self.__connection.cursor()
        try:
            mycursor.execute(f'USE {selected_db};')
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __create_table(self, table_name, table_schema):
        try:
            self.__connection.cursor().execute(f'CREATE TABLE {table_name} {table_schema}')
            self.__connection.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __populate_table(self, table_name, data):
        str_form = ",%s" * (len(data[0]) - 1)
        statement = f'INSERT INTO {table_name} {self.__table_schema} VALUES (%s {str_form})'
        try:
            mycursor = self.__connection.cursor()
            mycursor.executemany(statement, data)
            print('database with tables and data created succesfully')
            self.__connection.commit()

        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __create_db_tables_keys(self):
        self.__db_name = 'covid_corona_db_MAKE_RIVA'
        self.__create_db()
        self.__select_db(self.__db_name)

        self.__table_name = f'covid_data{self.__date}'
        table_schema = """(
            `rank` decimal() NOT NULL,
            `Country,Other` varchar(50) NOT NULL,
            `TotalCases` decimal(10) DEFAULT NULL,
            `NewCases` decimal(10) DEFAULT NULL,
            `TotalDeaths` decimal(10) DEFAULT NULL,
            `NewDeaths` decimal(10) DEFAULT NULL,
            `TotalRecovered` decimal(10) DEFAULT NULL,
            `NewRecovered` decimal(10) DEFAULT NULL,
            `ActiveCases` decimal(10) DEFAULT NULL,
            `Serious,Critical` decimal(10) DEFAULT NULL,
            `Tot Cases/1M pop` decimal(10,1) DEFAULT NULL,
            `Deaths/1M pop` decimal(10,1) DEFAULT NULL,
            `TotalTests` decimal(10) DEFAULT NULL,
            `Tests/1M pop` decimal(10) DEFAULT NULL,
            `Population` decimal(10) DEFAULT NULL,
            `Continent` varchar(50) NOT NULL,
            `1 Caseevery X ppl` decimal(10) DEFAULT NULL,
            `1 Deathevery X ppl` decimal(10) DEFAULT NULL,
            `1 Testevery X ppl` decimal(10) DEFAULT NULL,
            PRIMARY KEY (`Country,Other`)
        )
        """
        self.__create_table(self.__table_name, table_schema)

    def __closeDatabase(self):
        self.__connection.close()

