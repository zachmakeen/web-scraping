import re


class CleanData:
    def __init__(self, html_soup, json_list):
        self.__html = html_soup
        self.__json = json_list

    # Returns the covid data as a list of tuples
    def generate_covid_list(self, table_id, date):
        table = self.__html.find(id=table_id)  # Gets the table for that id
        return self.__clean_table_row(table.find_all('tr'), date)  # Passes a list of table rows to be cleaned

    # Returns the cleaned table rows
    def __clean_table_row(self, table_row_list, date):
        clean_data = []
        for table_row in table_row_list[1:]:
            temp_table_row = [date]  # Creates a list starting with the date correlating to the data
            table_entry_list = table_row.find_all('td')  # Creates a list of entries for the selected row
            for table_entry in table_entry_list:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            clean_data.append(tuple(temp_table_row))  # Appends data as tuple to the main list
        return clean_data[8:-8]

    # Returns the cleaned table row entries
    def __clean_table_entry(self, table_entry):
        table_entry = re.sub(r'\n|\+|\s{2,}|,|N/A', '', table_entry)  # Removes unnecessary characters
        if table_entry == '':
            return None  # Replaces empty string with the key word None
        elif re.match(r'^\d+$', table_entry):
            return int(table_entry)  # Returns ints for numbers that were originally strings
        else:
            return table_entry

    # Returns the country border data as a list of tuples
    def generate_border_list(self):
        temp_list = []
        for json_dict in self.__json:  # Iterates through each dictionary
            country_data = list(json_dict.values())[0]  # Gets the neighbouring countries and their values
            neighbor_num = len(list(country_data.keys()))  # Counts how many neighbouring countries there are
            for i in range(neighbor_num):
                country_name = list(json_dict.keys())[0]  # Gets the country name
                neighbor = list(country_data.keys())[i]  # Gets the neighbour for that country
                distance = list(country_data.values())[i]  # Gets the distance for the neighbouring country
                temp_tuple = (country_name, neighbor, distance)
                temp_list.append(temp_tuple)
        temp_list.pop(297)  # Removes duplicate neighbouring country
        return temp_list
