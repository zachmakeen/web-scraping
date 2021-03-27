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
        country = 'China'
        explore_object = ExploreData(country, corona_df, border_df)

        # Plot data
        plot_object = PlotData()
