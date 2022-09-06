import json

def loadData(filename):
    """Loads the data in a .json file"""
    with open(filename, 'r') as f:
        temp = json.load(f)
        return temp

def writeData(filename, data):
    """Writes data to a .json file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)