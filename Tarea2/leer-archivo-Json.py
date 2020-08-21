import json

def readJason():
    file = open('Archivo1.json')
    data= json.load(file)
    file.close()
    print(data)
    return data

dict = readJason()
for element in dict:
    print(element)