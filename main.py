from scrape_save_data_second import ScrapeAndSaveData
from add_data_to_database import CreateDatabase


# print('Type "help" to see more commands')
# command = ''
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''
#         scrape - to scrape data
#         analyse - to analyse data
#         quit - to end the program
#         ''')
#     elif command == 'scrape':
#         ScrapeData()
#         CreateDatabase()
#     elif command == 'analyse':
#         pass
#     elif command == 'quit':
#         break
#     else:
#         print('Sorry, that is not a valid command.')

data_object = ScrapeAndSaveData()
# print(data_object.get_today_data())
# data_object.console_interaction()
# CreateDatabase(data_object)

