from extract_data import ExtractData


class ExploreAnalyzeData:
    def __init__(self):

        # Extract records from the database
        extract_object = ExtractData()
        corona_df = extract_object.get_corona_df()
        border_df = extract_object.get_border_df()
