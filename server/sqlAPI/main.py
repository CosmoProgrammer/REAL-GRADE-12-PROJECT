import mysql.connector
from random import randint, sample

subColumnSaltKeys = {}
schema = {}


cnx = mysql.connector.connect(
    user='root', password='sql123', host='localhost', port='3306', database='project')
cur = cnx.cursor()


def generateSaltKey():
    x = randint(0, 16)
    y = -10
    while y < x:
        y = randint(17, 36)
    return ''.join(sample('qwertyuiopasdfghjklzxcvbnm', len('qwertyuiopasdfghjklzxcvbnm')))[x:y]


def createTable(data):
    cur.execute('drop table if exists info;')
    cur.execute('create table if not exists info(value LONGTEXT);')
    cnx.commit()
    cur.execute(f"insert into info values (\"{data}\")")
    cur.execute('drop table if exists inventory;')
    cnx.commit()
    query = "create table inventory ("
    subColumnSaltKeys = {}
    for dict in data:
        for element in dict:
            if element != 'subColumns' and dict['subColumns'] == []:
                query += str(dict[element]).replace('string',
                                                    'varchar(255)').replace('number', 'float') + ' '

            elif element == 'subColumns' and dict['subColumns'] != []:
                subColumnSaltKeys[dict['name'].lower()] = generateSaltKey()
                for subcolumn in dict[element]:
                    subcolumn['name'] = subcolumn['name'] + \
                        subColumnSaltKeys[dict['name']]
                    for subcolumnHeader in subcolumn:
                        query += str(subcolumn[subcolumnHeader]).replace(
                            'string', 'varchar(255)').replace('number', 'float') + ' '
                    query += ','
        query += ','
    k = 0
    query = query.replace(',,', ',')
    for i in range(len(query) - 1, 0, -1):
        if query[i] == ',' or query[i] == ' ':
            k += 1
        else:
            break

    print(subColumnSaltKeys)
    with open('subColSaltKeys.txt', 'w') as f:
        f.write(str(subColumnSaltKeys))

    query = query[0:-k]
    query += ')'
    print(query)
    cur.execute(query)
    cnx.commit()


def getRow(id):
    retDict = {}
    q = f"select * from inventory where ID={id};"
    # print(q)
    cur.execute(q)
    data = cur.fetchone()
    headers = [i[0] for i in cur.description]
    # headers = ['a', 'b', 'cxyz123', 'dxyz123']
    # data = ('1', '2', '3', '4')
    f = open('subColSaltKeys.txt', 'r')
    subColumnSaltKeys = eval(f.read())
    f.close()
    list = []
    print(data, headers)
    if data == [] or data == None:
        data = []
        for i in range(len(headers)):
            data += [0]
    for i in range(len(headers)):
        isSubCol = False

        t = ()
        for j in subColumnSaltKeys:

            if subColumnSaltKeys[j] in headers[i]:
                isSubCol = True
                t = (j, subColumnSaltKeys[j])
        if not isSubCol:
            retDict[str(headers[i])] = data[i] if data != None else ''
        else:
            header, key = t
            try:
                retDict[header][0] += [headers[i].strip(key)]
                retDict[header][1] += [data[i]]

            except KeyError:
                retDict[header] = [[headers[i].strip(key)], [data[i]]]
    return retDict


def returnAll(isBUTT):
    cur.execute('select * from inventory')
    data = cur.fetchall()
    headers = [i[0] for i in cur.description]
    with open('subColSaltKeys.txt', 'r') as f:
        subColumnSaltKeys = eval(f.read())
    saltKeys = subColumnSaltKeys.values()
    subcolumnHeaderIndexes = []
    for i in saltKeys:
        t = []
        for j in range(len(headers)):
            if i in headers[j]:
                t += [j]
        print('****________________', t)
        subcolumnHeaderIndexes += [t]
    print(subcolumnHeaderIndexes)
    returnList = []
    for row in data:
        rowList = []
        subColumnList = []
        stopVal = -1
        for valueIndex in range(len(row)):
            stopVal = max(checkSubColums(valueIndex, subcolumnHeaderIndexes))
            if valueIndex < stopVal:
                subColumnList += [row[valueIndex]]
                print(subColumnList)
            elif valueIndex == stopVal:
                subColumnList += [row[valueIndex]]
                rowList += [subColumnList]
                subColumnList = []
            else:
                rowList += [row[valueIndex]]
        if subColumnList != []:
            rowList += [subColumnList]
        returnList += [rowList]
    print(returnList)
    c = cnx.cursor()
    c.execute('select value from info;')
    s = c.fetchall()
    # print("vvvvvvvvvv")
    # print(s)
    # print("vvvvvvvvvv")
    sone = eval(s[0][0])
    print(returnList)
    if isBUTT:
        sone += [{'name': "Edit", 'type': "button", 'subColumns': []},
                 {'name': "Delete", 'type': "button", 'subColumns': []}]
    return {'data': returnList, 'schema': sone}


def checkSubColums(index, subcolumnHeaderIndexes):
    print('*****************', subcolumnHeaderIndexes)
    for subColRoot in subcolumnHeaderIndexes:
        if index in subColRoot:
            return subColRoot
    return [-1]


def deleteRow(id):
    q = f'delete from inventory where id = {id};'
    print(q)
    cur.execute(q)
    cnx.commit()
    return 'hi'


def addRow(rows):
    # [1, 253, 1, 253, 253, 253, 253]#
    headerType = [i[1] for i in cur.description]
    i = list(rows.values())
    c, k = 0, 0
    for element in i:
        if type != list:
            k += 1
        else:
            for x in element[1]:
                k += 1
    q = 'insert into inventory values('
    for j in range(len(i)):
        if type(i[j]) != list and len(i) - 1 != j:
            if headerType[c] == 253:
                q += f'"{i[j]}",'
            else:
                q += f'{i[j]},'
            c += 1

        elif type(i[j]) == list and len(i) - 1 != j:
            for k in i[j][1]:
                if headerType[c] == 253:
                    q += f'"{k}",'
                else:
                    q += f'{k},'
                c += 1
        elif type(i[j]) != list and len(i) - 1 == j:
            if headerType[c] == 253:
                q += f'"{i[j]}");'
            else:
                q += f'{i[j]});'
            c += 1
        elif type(i[j]) == list and len(i) - 1 == j:

            for k in range(len(i[j][1])):
                if k != len(i[j][1]) - 1:
                    if headerType[c] == 253:
                        q += f'"{i[j][1][k]}",'
                    else:
                        q += f'{i[j][1][k]},'
                    c += 1
                else:
                    if headerType[c] == 253:
                        q += f'"{i[j][1][k]}");'
                    else:
                        q += f'{i[j][1][k]});'
                    c += 1
    print(q)
    cur.execute(q)
    cnx.commit()


def updateRow(row_data):
    query = 'update inventory set '
    cond = 0
    cur.execute("SELECT * FROM inventory LIMIT 1;")
    # [1, 253, 1, 253, 253, 253, 253]
    headerType = [i[1] for i in cur.description]
    # ['id', 'public/np', 'qty', 'industry','tasteabcd','colorabcd', 'smellabcd']#
    headers = [i[0] for i in cur.description]
    temp = cur.fetchall()
    c = 0
    for element in row_data:
        stg = ''
        if type(row_data[element]) != list:
            print(element.lower())
            if element.lower() == 'id':
                cond = row_data[element]
                print('cond')
            elif element.lower != 'id':
                if headerType[c] == 253:
                    stg = str(element) + '=' + '"' + \
                        str(row_data[element]) + '"' + ','
                else:
                    stg = str(element) + '=' + str(row_data[element]) + ','
        else:
            with open('subColSaltKeys.txt', 'r') as f:
                k = eval(f.read())
            saltKey = k[element.lower()]
            changeInd = []
            for i in range(len(headers)):
                if saltKey in headers[i]:
                    changeInd += [i]
            c = 0
            for i in changeInd:
                print(c)
                if headerType[i] == 253:
                    stg += headers[i] + '=' + '"' + \
                        str(row_data[element][1][c]) + '"' + ','
                else:
                    stg += headers[i] + '=' + \
                        str(row_data[element][1][c]) + ','
                c += 1
        query += stg
        c += 1
    query = query[0:-1]
    query += f' where id={cond};'
    print("HIIII")
    print(query)
    cur.execute(query)
    cnx.commit()


def createLoginTable(data):
    cur.execute('drop table if exists login;')
    cnx.commit()
    query = "create table login (username varchar(255) primary key, password varchar(255), accessLevel varchar(255));"
    cur.execute(query)
    print(data)
    for a in data:
        q = f'insert into login values ("{a["username"]}", "{a["password"]}", "{a["accessLevel"]}");'
        cur.execute(q)
        cnx.commit()


def login(user, password):
    cur.execute('select * from login;')
    data = cur.fetchall()
    print(data)
    for i in data:
        if i[0:2] == (user, password):
            return True
        else:
            return False


data = [
    {'name': "ID", 'type': "number", 'subColumns': []},
    {'name': "Public/NonPublic", 'type': "string", 'subColumns': []},
    {
        'name': "Qty",
        'type': "number",
        'subColumns': []
    },
    {'name': "Industry", 'type': "string", 'subColumns': []},
    {
        'name': "'Type's",
        'type': "string",
        'subColumns': [
            {'name': "Taste", 'type': "string"},
            {'name': "Colour", 'type': "string"},
            {'name': "Smell", 'type': "string"},
        ],
    }
]

row_data = {"ID": 1, "Public/NonPublic": "Public", "Qty": 10, "Industry": "Cooking", "senses": [[
    ["Taste"],
    ["Colour"],
    ["Smell"],
], ["Sweet", "Green", "Pungent"]]}


# addRow(row_data)
# getRow(5)
# updateRow(row_data)
