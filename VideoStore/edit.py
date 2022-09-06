import dataMgr
import view

def editData():
    """Edit the data of a film already in the inventory"""
    view.viewData()
    newData = []
    temp = dataMgr.loadData('data.json')
    dataLen = len(temp) - 1
    print("Which index would you like to edit?")
    editOption = input(f'Select a number 0-{dataLen}: ')
    i = 0
    for entry in temp:
        if i == int(editOption):
            title = entry['title']
            length = entry['length']
            rating = entry['rating']
            year = entry['year']
            stock = entry['stock']
            print(f'Current title: {title}')
            newTitle = input('What is the new title? ')
            print(f'Current length: {length}')
            newLen = int(input('What is the new length of the film? '))
            print(f'Current rating: {rating}')
            newRating = input('What is the new rating? ')
            print(f'Current year of release: {year}')
            newYear = input('What is the new year of release? ')
            print(f'How many copies of {title} are in stock?')
            newStock = int(input(''))
            newData.append({'title': newTitle, 'length': newLen, 'rating': newRating, 'year': newYear, 'stock': newStock})
            i += 1
        else:
            newData.append(entry)
            i += 1
    dataMgr.writeData('data.json', newData)