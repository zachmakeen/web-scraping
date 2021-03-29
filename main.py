from scrape_save_data import ScrapeSaveData
from explore_analyze_data import ExploreAnalyzeData


print('''
help - to see the list of available commands
s - to save and/or scrape data
a - to analyse data
quit - to end the program
''')
command = ''
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
help - to see the list of available commands
s - to save and/or scrape data
a - to analyse data
quit - to end the program
        ''')
    elif command == 's':
        ssd_object = ScrapeSaveData()
        ssd_object.interact()
    elif command == 'a':
        ead_object = ExploreAnalyzeData()
        ead_object.interact()
    elif command == 'quit':
        break
    else:
        print('Sorry, that is not a valid command.')
