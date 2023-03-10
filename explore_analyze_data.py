from extract_data import ExtractData
from explore_data import ExploreData
from plot_data import PlotData


class ExploreAnalyzeData:
    def __init__(self):
        self.__country = None
        self.__explore_object = None

        # Extract records from the database
        self.__extract_object = ExtractData()
        self.__corona_df = self.__extract_object.get_corona_df()
        self.__border_df = self.__extract_object.get_border_df()

    def interact(self):
        while True:  # Asks the user to enter the country name and repeats if it does not exist
            try:
                self.__country = str(input('Enter the country to analyze here: ')).title()
                self.__explore_object = ExploreData(self.__country, self.__corona_df, self.__border_df)
            except IndexError:
                print('That is not a valid country')
                continue
            else:
                break
        print(f'''
help - to see the list of available commands
plot1 - to view the evolution throughout the 6 days for {self.__country}
plot2 - to view the evolution throughout the 6 days of {self.__country} along with its neighbour
plot3 - to view the difference between the Deaths/1M pop for the first 3 days for {self.__country} and 2 of its neighbour
back - to scrape data or exit the program
        ''')
        while True:
            command = input('> ').lower()
            if command == 'help':
                print(f'''
help - to see the list of available commands
plot1 - to view the evolution throughout the 6 days for {self.__country}
plot2 - to view the evolution throughout the 6 days of {self.__country} along with its neighbour
plot3 - to view the difference between the Deaths/1M pop for the first 3 days for {self.__country} and 2 of its neighbour
back - to scrape data or exit the program
                ''')
            elif command == 'plot1':
                explore_df = self.__explore_object.get_six_days_evolution()  # Retrieves the dataframe used for plot 1
                plot_data = PlotData(self.__country, self.__explore_object.get_neighbour(), explore_df)
                plot_data.evolution_six_days()  # Shows plot 1
            elif command == 'plot2':
                explore_df = self.__explore_object.get_six_days_newCases()  # Retrieves the dataframe used for plot 2
                plot_data = PlotData(self.__country, self.__explore_object.get_neighbour(), explore_df)
                plot_data.two_countries_evouluton_six_days()  # Shows plot 2
            elif command == 'plot3':
                explore_df = self.__explore_object.get_six_days_Deaths()  # Retrieves the dataframe used for plot 3
                plot_data = PlotData(self.__country, self.__explore_object.get_many_neighbours(), explore_df)
                plot_data.neigbours_deaths_perPop()  # Shows plot 3
            elif command == 'back':
                break
            else:
                print('Sorry, that is not a valid command.')
