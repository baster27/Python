import dataMgr

def viewData():
    """Prints out the entire film inventory to the screen"""
    temp = dataMgr.loadData('data.json')
    i = 1
    print('\n')
    for entry in temp:
        title = entry['title']
        length = entry['length']
        rating = entry['rating']
        year = entry['year']
        stock = entry['stock']
        print(f'Index number: {i}')
        print(f'Title: {title}')
        print(f'Length: {length}')
        print(f'Rating: {rating}')
        print(f'Year of Release: {year}')
        print(f'In Stock: {stock}')
        print('\n')
        i += 1