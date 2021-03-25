from database_api import DatabaseAPI


class ManageDatabase:
    def __init__(self):
        self.__db_api = DatabaseAPI('covid_corona_db_MAKE_RIVA')

    def add_covid_records(self, covid_records):
        table_name = 'covid_data'
        table_schema = """(
            `Date` date NOT NULL,
            `Rank` int(3) NOT NULL,
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
        )
        """
        self.__db_api.select_db()
        self.__db_api.create_table(table_name, table_schema)
        self.__db_api.populate_table(table_name, covid_records)

    def add_border_records(self, border_records):
        table_name = 'country_borders'
        table_schema = """(
            `Country,Other` varchar(50) NOT NULL,
            `Neighbour` varchar(50) NOT NULL,
            `Distance` int (10) DEFAULT NULL
        )
        """
        self.__db_api.select_db()
        self.__db_api.create_table(table_name, table_schema)
        self.__db_api.populate_table(table_name, border_records)
