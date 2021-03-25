from mysql.connector import connect, Error
import os


class CreateDatabase:

    def __init__(self):
        self.__db_name = 'covid_corona_db_MAKE_RIVA'
        self.__connection = self.__connect_to_db()
        # self.table_name = f'covid_data{self.__date}'
        # self.__table_schema = '(`rank`, `Country,Other`, `TotalCases`, `NewCases`, `TotalDeaths`, `NewDeaths`, `TotalRecovered`, `ActiveCases`, `Serious,Critical`, `Tot Cases/1M pop`, `Deaths/1M pop`, `TotalTests`, `Tests/1M pop`, `Population`, `Continent`, `1 Caseevery X ppl`, `1 Deathevery X ppl`, `1 Testevery X ppl`)'
        self.__data = None
        self.__table_name = None

    def store_data(self, data, table):
        # self.__create_db()
        self.__data = data
        self.__table_name = table
        self.__select_db()
        self.__create_db_tables_keys()
        # self.__populate_table(data)
        # self.__closeDatabase()

    def __connect_to_db(self):
        try:
            if self.__db_name is not None:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                    database=self.__db_name
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

    def __select_db(self):
        mycursor = self.__connection.cursor()
        try:
            mycursor.execute(f'USE {self.__db_name};')
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __create_table(self, table_name, table_schema):
        try:
            self.__connection.cursor().execute(f'CREATE TABLE `{table_name}` {table_schema}')
            self.__connection.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __populate_table(self, data):
        print(self.__table_name)
        print(type(data[0]))
        if self.__table_name != 'country':
            str_form = ",%s" * (len(data[0]) - 1)
            statement = f'INSERT INTO `{self.__table_name}` VALUES (%s {str_form})'
        else:
            statement = f'INSERT INTO `{self.__table_name}` VALUES (%s)'
        try:
            my_cursor = self.__connection.cursor()
            my_cursor.executemany(statement, data)
            print('database with tables and data created succesfully')
            self.__connection.commit()
        except Error as err:
            print('There as a problem with the db: {}'.format(err))

    def __create_db_tables_keys(self):
        table_schema = ''
        if self.__table_name == 'corona_table':
            table_schema = """(
            `Date` date NOT NULL,
            `rank` int(3) NOT NULL,
            `Country,Other` varchar(50) NOT NULL,
            `TotalCases` int(10) DEFAULT NULL,
            `NewCases` int(10) DEFAULT NULL,
            `TotalDeaths` int(10) DEFAULT NULL,
            `NewDeaths` int(10) DEFAULT NULL,
            `TotalRecovered` int(10) DEFAULT NULL,
            `NewRecovered` int(10) DEFAULT NULL,
            `ActiveCases` int(10) DEFAULT NULL,
            `Serious,Critical` int(10) DEFAULT NULL,
            `Tot Cases/1M pop` int(10) DEFAULT NULL,
            `Deaths/1M pop` int(10) DEFAULT NULL,
            `TotalTests` int(10) DEFAULT NULL,
            `Tests/1M pop` int(10) DEFAULT NULL,
            `Population` int(10) DEFAULT NULL,
            `Continent` varchar(50) DEFAULT NULL,
            `1 Caseevery X ppl` int(10) DEFAULT NULL,
            `1 Deathevery X ppl` int(10) DEFAULT NULL,
            `1 Testevery X ppl` int(10) DEFAULT NULL,
            PRIMARY KEY (`Country,Other`, `Date`)
            FOREIGN KEY (`Country,Other`) REFERENCES COUNTRY(`Country,Other`)"""
        elif self.__table_name == 'corona_table':
            table_schema = """(
            `Country,Other` varchar(50) NOT NULL,
            `Neighbour` varchar(50) NOT NULL,
            `Distance` int (10) DEFAULT NULL,
            PRIMARY KEY (`Country,Other`, `Neighbour`),
            FOREIGN KEY (`Country,Other`) REFERENCES COUNTRY(`Country,Other`),
            FOREIGN KEY (`Neighbour`) REFERENCES COUNTRY(`Neighbour`)
            )"""
        else:
            table_schema = """(
                        `Country,Other` VARCHAR(50) NOT NULL,
                        PRIMARY KEY (`Country,Other`)
                        )"""

        self.__create_table(self.__table_name, table_schema)


    def __closeDatabase(self):
        self.__connection.close()

