import mysql.connector
from random import randint

subColumnSaltKeys = {}

cnx = mysql.connector.connect()
cur = cnx.cursor()

def generateSaltKey():
    x = randint(0, 16)
    y = -10
    while y < x:
        y = randint(17, 26)
    return 'qwertyuiopasdfghjklzxcvbnm'[x:y]

def createTable(data):
    query = "create table inventory ("
    for dict in data:
        for element in dict:
            if element != 'subColumns':
                query += str(dict[element]).replace('string', 'varchar(255)').replace('number', 'integer') + ' '
            
            elif element == 'subColumns' and dict[element] != []:
                subColumnSaltKeys[dict['name']] = generateSaltKey()
                print(subColumnSaltKeys)
                for subcolumn in dict[element]:
                    subcolumn['name'] = subcolumn['name'] + subColumnSaltKeys[dict['name']]
                    print(subcolumn)  
                    for subcolumnHeader in subcolumn:
                        query += str(subcolumn[subcolumnHeader]).replace('string', 'varchar(255)').replace('number', 'integer') + ' '
                    query += ','
            print(query)
        query += ','
    k = 0
    for i in range (len(query) - 1, 0, -1):
        if query[i] == ',' or query[i] == ' ':
            k += 1
        else:
            break
        
    query = query[0:-k]
    query += ')'
    print(query)

def getRow(id):
    retDict = {}
    q = f'select * from inventory where ID={id};'
    cur.execute(q)
    data = cur.fetchone()
    headers = [i[0] for i in cur.description]
    for i in range(len(headers)):
        if str(headers[i]) not in subColumnSaltKeys:
            retDict += {str(headers[i]): data[i]}
        else:
            subColInds = []
            for j in range(len(headers)):
                if subColumnSaltKeys[str(headers[i])] in str(headers[j]):
                    subColInds += j
            retList = []
            for j in subColInds:
                retList += [[headers[j], data[j]]]      
            retDict += {str(headers(i)): retList}    
    return retDict    
        
def updateRow(row_data):
    query = 'update inventory set '
    if type(row_data[element]) != list:
        for element in row_data:
            stg = str(element) + '=' + str(row_data[element])
        
        

data = [
    { 'name': "ID", 'type': "number", 'subColumns': [] },
    { 'name': "Public/NonPublic", 'type': "string", 'subColumns': [] },
    {
      'name': "Qty",
      'type': "number",
    },
    { 'name': "Industry", 'type': "string", 'subColumns': [] },
    {
      'name': "'Type's",
      'type': "string",
      'subColumns': [
        { 'name': "Taste", 'type': "string" },
        { 'name': "Colour", 'type': "string" },
        { 'name': "Smell", 'type': "string" },
      ],
    }
  ]

row_data = {"ID":1, "Public/NonPublic":"Public", "Qty":[[
        ["Public"],
        ["Private"],
      ],[5, 10]], "Industry":"Cooking", "Types":[[
        ["Taste"],
        ["Colour"],
        ["Smell"],
      ],["Sweet", "Green", "Pungent"]]}

createTable(data)