from extract_data import ExtractData
from explore_data import ExploreData
from plot_data import PlotData


class ExploreAnalyzeData:
    def __init__(self):
        self.__country = None

        # Extract records from the database
        extract_object = ExtractData()
        corona_df = extract_object.get_corona_df()
        border_df = extract_object.get_border_df()

        # Explore data
        country = 'Belgium'
        explore_object = ExploreData(country, corona_df, border_df)
        explore_df = explore_object.get_six_days_evolution()


        # Plotting 6 days evolution of Italy
        plot_data = PlotData(country, explore_df)
        plot_data.evolution_six_days()

        neighbours = explore_object.get_six_days_neighbours()
        plot_data = PlotData(country, explore_df)

        # Plot data
        # plot_object = PlotData()

    def interact(self):
        self.__country = str(input('Enter the country to analyze here: '))
        print(f'''
help - to see the list of available commands
plot1 - to view the evolution throughout the 6 days for {self.__country}
plot2 - to view the evolution throughout the 6 days of {self.__country} along with its neighbour
plot3 - to view the difference between the  Deaths/1M pop for the first 3 days for {self.__country} and 2 of its neighbour
back - to scrape data or exit the program
        ''')
        while True:
            command = input('> ').lower()
            if command == 'help':
                print('''
help - to see the list of available commands
plot1 - to view the evolution throughout the 6 days for {self.__country}
plot2 - to view the evolution throughout the 6 days of {self.__country} along with its neighbour
plot3 - to view the difference between the  Deaths/1M pop for the first 3 days for {self.__country} and 2 of its neighbour
back - to scrape data or exit the program
                ''')
            elif command == 'plot1':
                pass
            elif command == 'plot2':
                pass
            elif command == 'plot3':
                pass
            elif command == 'back':
                break
            else:
                print('Sorry, that is not a valid command.')
