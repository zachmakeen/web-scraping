import re


class CleanData:
    def __init__(self, html_soup, json_list):
        self.__html = html_soup
        self.__json = json_list

    def generate_covid_list(self, table_id, date):
        table = self.__html.find(id=table_id)
        return self.__clean_table_row(table.find_all('tr'), date)

    def __clean_table_row(self, table_row_list, date):
        clean_data = []
        for table_row in table_row_list[1:]:
            temp_table_row = [date]
            table_entry_list = table_row.find_all('td')
            for table_entry in table_entry_list:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            clean_data.append(tuple(temp_table_row))
        return clean_data[8:-8]

    def __clean_table_entry(self, table_entry):
        table_entry = re.sub(r'\n|\+|\s{2,}|,|N/A', '', table_entry)
        if table_entry == '':
            return None
        elif re.match(r'^\d+$', table_entry):
            return int(table_entry)
        else:
            return table_entry

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
            temp_list.append((list(json_dict.keys())[0],))
        return temp_list
