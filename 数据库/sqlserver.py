import pymssql

def con():
    serverName = 'localhost'
    userName = 'sa'
    passWord = 'Aug#10ps'
    database = 'AAI'
    Port = 1433
    conn = pymssql.connect(serverName,userName,passWord,database,Port)
    cor = conn.cursor()
    return cor

def remotecon():
    serverName = '117.186.228.14'
    userName = 'sa'
    passWord = 'Adams2015'
    database = 'AAI'
    Port = 15343
    conn = pymssql.connect(host=serverName, user=userName, password=passWord, database=database, port=Port)
    remotecor = conn.cursor()
    return remotecor

if __name__ == '__main__':
    cor = con()
    cor.execute('select * from Employee')
    print(cor.fetchall())