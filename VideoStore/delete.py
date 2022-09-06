import dataMgr
import view

def deleteStock(temp, delOption, newData):
    """Deletes an entire films entry, regardless of number of copies in stock"""
    i = 0
    for entry in temp:
        if i == delOption:
            pass
            i += 1
        else:
            newData.append(entry)
            i += 1
    dataMgr.writeData('data.json', newData)


def delete():
    """Deletes a film from the inventory"""
    view.viewData()
    newData = []
    temp = dataMgr.loadData('data.json')
    dataLen = len(temp) - 1
    print('Are you deleting:\n1. An entire film\'s stock\n2. A copy of a film')
    choice = int(input(''))
    if choice == 1:
        print('-------------------- W A R N I N G: -------------------------\n'
              ' This action will delete all the stock of the selected film.\n'
              '           Are you sure you want to do this?')
        yn = input('Y/N: ')
        if yn == 'Y' or yn == 'y':
            print("Which index would you like to delete?")
            delOption = int(input(f'Select a number 0-{dataLen}: '))
            deleteStock(temp, delOption, newData)
        if yn == 'N' or yn == 'n':
            print('Going back to main menu.')

    if choice == 2:
        print('Which index are you removing a copy of?')
        delOption = int(input(f'Select a number 1-{dataLen + 1}: '))
        i = 0
        for entry in temp:
            if i == delOption:
                if entry['stock'] == 1:
                    deleteStock(temp, delOption, newData)
                else:
                    entry['stock'] -= 1
                    newData.append(entry)
                    i += 1
            else:
                newData.append(entry)
                i += 1

        dataMgr.writeData('data.json', newData)
