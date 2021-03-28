from extract_data import ExtractData
from explore_data import ExploreData
from plot_data import PlotData


class ExploreAnalyzeData:
    def __init__(self):

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
