class CleanData:
    def __init__(self, html_soup, json_list):
        self.__html = html_soup
        self.__json = json_list

    def generate_covid_list(self, table_id, date):
        pass

    def generate_border_list(self):
        temp_list = []
        for json_dict in self.__json:
            country_data = list(json_dict.values())[0]
            neighbor_num = len(list(country_data.keys()))
            for i in range(neighbor_num):
                country_name = list(json_dict.keys())[0]
                neighbor = list(country_data.keys())[i]
                distance = list(country_data.values())[i]
                temp_tuple = (country_name, neighbor, distance)
                temp_list.append(temp_tuple)
        return temp_list

    def generate_country_list(self):
        temp_list = []
        for json_dict in self.__json:
            temp_list.append((list(json_dict.keys())[0], ))
        return temp_list
