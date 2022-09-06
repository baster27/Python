import dataMgr
import datetime

def addData():
    """Add a film to the inventory by following the prompts"""
    item = {}
    ratings = ['G', 'g', 'PG', 'pg', 'PG-13', 'pg-13', 'R', 'r']
    temp = dataMgr.loadData('data.json')
    print('Would you like to:\n1. Add a new film to the inventory\n2. Add a copy of an existing film in the '
          'inventory.\n')
    choice = int(input("Choice: "))
    if choice == 1:
        item['title'] = input('Enter the title of the film: ')
        item['length'] = int(input(f'Enter {item["title"]}\'s length in minutes: '))

        item['rating'] = input(f'Enter {item["title"]}\'s rating: ')
        if item['rating'] not in ratings:
            print("You did not enter a valid film rating, please re-enter the film's rating.")
            item['rating'] = input(f'Enter {item["title"]}\'s rating: ')
            if item['rating'] not in ratings:
                print('Selection is still not a valid rating. Try again')
                addData()
        item['year'] = int(input(f'Enter the year {item["title"]} was released: '))
        if item['year'] < 1900:
            print(f'They weren\'t making movies in {item["year"]}.')
            item['year'] = int(input(f'Re-enter the year {item["title"]} was released: '))
            if item['year'] < 1900:
                print('Take it from the top.')
                addData()
        elif item['year'] > datetime.datetime.now().year:
            print('That year is in the future, try again.')
            item['year'] = int(input(f'Re-enter the year {item["title"]} was released: '))
            if item['year'] > datetime.datetime.now().year:
                print('Take it from the top.')
                addData()
        item['stock'] = 1
        temp.append(item)
        dataMgr.writeData('data.json', temp)
    elif choice == 2:
        print('Which film are you adding a copy of?')
        film = input('')
        for entry in temp:
            title = entry['title']
            if title == film:
                entry['stock'] += 1
        dataMgr.writeData('data.json', temp)