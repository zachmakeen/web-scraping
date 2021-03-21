from mysql.connector import connect, Error
import os


class CreateDatabase:

    def __init__(self, date):
        self.__date = date
        self.__db_name = 'covid_corona_db_MAKE_RIVA'
        self.table_name = f'covid_data{self.__date}'
        self.__connection = self.__connect_to_db()
        self.__data = None

    def store_data(self, data):
        self.__create_db()
        self.__data = data
        # self.__select_db()
        # self.__create_db_tables_keys()
        table_schema = '(rank, Country,Other, TotalCases, NewCases, TotalDeaths, NewDeaths, TotalRecovered, NewRecovered, ActiveCases, Serious,Critical, Tot Cases/1M pop, Deaths/1M pop, TotalTests, Tests/1M pop, Population, Continent, 1 Caseevery X ppl, 1 Deathevery X ppl, 1 Testevery X ppl)'
        # self.__populate_table(self.table_name, table_schema)

    def __connect_to_db(self):
        try:
            if self.__db_name is not None:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                    database=self.__db_name,
                )
            else:
                return connect(
                    host="localhost",
                    user=os.environ.get('DB_USER'),  # Used PyCharm environment variables.
                    password=os.environ.get('DB_PASS'),  # Used PyCharm environment variables.
                )
        except Error as e:
            print(e)

    def __create_db(self):
        try:
            # connection = self.__connect_to_db()
            # create_db_query = f'CREATE DATABASE {self.__db_name}'
            # with self.__connection.cursor() as cursor:
            #     cursor.execute(create_db_query)
            self.__connection.cursor().execute(f'CREATE DATABASE {self.__db_name}')
        except Error as e:
            print(e)

    def __select_db(self):
        try:
            # connection = self.__connect_to_db()
            use_db_query = f'USE {self.__db_name}'
            with self.__connection.cursor() as cursor:
                cursor.execute(use_db_query)
                result = cursor.fetchall()
                for table in result:
                    print(table)
        except Error as e:
            print(e)

    def __create_table(self, table_name, table_schema):
        try:
            # connection = self.__connect_to_db()
            create_table_query = f'CREATE TABLE {table_name}{table_schema}'
            with self.__connection.cursor() as cursor:
                cursor.execute(create_table_query)
                self.__connection.commit()
        except Error as e:
            print(e)

    def __populate_table(self, table_name, table_schema):
        try:
            # connection = self.__connect_to_db()
            insert_values_query = f"""
                INSERT INTO {table_name}
                {table_schema}
                VALUES ( %s{', %s' * table_schema.count(',')} )
                """
            with self.__connection.cursor() as cursor:
                cursor.executemany(insert_values_query, self.__data)
                self.__connection.commit()
        except Error as e:
            print(e)

    def __create_db_tables_keys(self):
        self.__create_db()
        table_name = f'covid_data{self.__date}'
        table_schema = """(
            `rank int(3)` NOT NULL,
            `Country,Other` varchar(50) NOT NULL PRIMARY KEY,
            `TotalCases` int(10) DEFAULT NULL,
            `NewCases` int(10) DEFAULT NULL,
            `TotalDeaths` int(10) DEFAULT NULL,
            `NewDeaths` int(10) DEFAULT NULL,
            `TotalRecovered` int(10) DEFAULT NULL,
            `NewRecovered` int(10) DEFAULT NULL,
            `ActiveCases` int(10) DEFAULT NULL,
            `Serious,Critical` int(10) DEFAULT NULL,
            `Tot Cases/1M pop` decimal(10,1) DEFAULT NULL,
            `Deaths/1M pop` decimal(10,1) DEFAULT NULL,
            `TotalTests` int(10) DEFAULT NULL,
            `Tests/1M pop` int(10) DEFAULT NULL,
            `Population` int(10) DEFAULT NULL,
            `Continent` varchar(50) NOT NULL,
            `1 Caseevery X ppl` int(10) DEFAULT NULL,
            `1 Deathevery X ppl` int(10) DEFAULT NULL,
            `1 Testevery X ppl` int(10) DEFAULT NULL
        )
        """
        self.__create_table(table_name, table_schema)