from distutils.log import error
from logging import exception
import sqlite3


# Create database
def creatingDatabase():
    # Connect to database.
    conn = sqlite3.connect('database.db')

    # Create a cursor.
    c = conn.cursor()

    # Create a table.
    c.execute('''CREATE TABLE product (
                code integer,
                name text,
                manufacturer text,
                price double,
                amount text,
                sold integer
            )''')
    c.execute('''CREATE TABLE clients (
                code integer,
                name text,
                lastName text,
                cpf integer,
                email text
            )''')
    c.execute('''CREATE TABLE users (
                code integer,
                user text,
                password text
            )''')
    # Commit our command.
    conn.commit()
    # Close our connection.
    conn.close()


#verify item existence
def itemVerify(type, cod):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    c.execute(f'SELECT * FROM {type} ORDER BY code')
    # Query the database
    items = c.fetchall()
    for item in items:
        if type == 'product' and item[0] == cod:
            conn.commit()
            conn.close()
            return True
        if type == 'clients' and  item[3] == cod:
            conn.commit()
            conn.close()
            return True
        if type == 'users' and item[1] == cod:
            conn.commit()
            conn.close()
            return True
    return False


def getCode(type, code):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute(f'SELECT * FROM {type} ORDER BY code')
    items = c.fetchall()
    for item in items:
        if type == 'clients' and  item[3] == code:
            conn.commit()
            conn.close()
            return item[0]
        if type == 'users' and  item[1] == code:
            conn.commit()
            conn.close()
            return item[0]
    conn.commit()
    conn.close()
    return False


def adminCountNumbers():
    i=0
    exist = False
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    listOfTables = c.execute("SELECT rowid, * FROM users").fetchall()
    for list in listOfTables:
        i += 1
    if not exist:
        conn.commit()
        conn.close()
        return i
    # Commit our command
    conn.commit()
    # Close our connection
    return i
    conn.close()


def adminCount():
    exist = False
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    listOfTables = c.execute("SELECT rowid, * FROM users").fetchall()
    for list in listOfTables:
        if list[0] >= 1:
            conn.commit()
            conn.close()
            return True
    if not exist:
        conn.commit()
        conn.close()
        return False
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def userVerify(user, password):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute(f'SELECT * FROM users ORDER BY code')
    items = c.fetchall()
    for item in items:
        if item[1] == user and  item[2] == password:
            conn.commit()
            conn.close()
            return True
    return False


# Add a new record to the table
def addProduct(type, code, one, two, three='', four='', five=''):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    if type == 'product':
        c.execute('INSERT INTO product VALUES (?,?,?,?,?,?)', (int(code), one, two, float(three), int(four), int(five)))
    elif type == 'clients':
        items = c.fetchall()
        code = 1
        for item in items:
            code+=1
        # Query the database
        c.execute(f'INSERT INTO clients VALUES ({code+1},{one},{two},{int(three)},{str(four)})')
    elif type == 'users':
        items = c.fetchall()
        # Query the database
        c.execute(f'INSERT INTO users VALUES ({code}, {one},{two})')
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def changeProduct(productType, productValue, idk, codP):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute('SELECT * FROM product ORDER BY code')
    items = c.fetchall()
    for item in items:
        japossui=True
        c.execute(f'''UPDATE product SET {productType} = "{productValue}"
                        WHERE {idk} = "{codP}"
        ''')
        conn.commit()
        conn.close()
        return True
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()
    return False


# You need to input id as a string
def deleteProduct(type, id):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute(f'DELETE from {type} WHERE code = (?)', id)
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def clearDatabase():
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute('SELECT rowid, * FROM product')
    items = c.fetchall()
    i=1
    for item in items:
        istr = str(i)
        c.execute('DELETE from product WHERE rowid = (?)', (istr))
        i+=1
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def showOne(type, id, mode):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute(f'SELECT * FROM {type} ORDER BY code')
    items = c.fetchall()
    for item in items:
        if type == 'product' and id == item[0] and mode == 'all':
            print(f'''
Código: {item[0]}
Nome: {item[1]}\tFabricante: {item[2]}
Preço: {item[3]:.2f}\tQuantidade: {item[4]}''')
            return 0
        if type == 'clients' and item[3] == id and mode == 'all':
            print(f'''
Código: {item[0]}
Nome: {item[1]} {item[2]}
CPF: {item[3]}
Email: {item[4]}''')
            return 0
        if item[0] == id and mode == '0':
            return item[0]
        if item[0] == id and mode == '1':
            return item[1]
        if item[0] == id and mode == '2':
            return item[2]
        if item[0] == id and mode == '3' and type == 'product':
            return f'{item[3]:.2f}'
        if item[0] == id and mode == '3' and type == 'clients':
            return f'{item[3]}'
        if item[0] == id and mode == '4':
            return item[4]
        if item[0] == id and mode == '5':
            return item[5]
        if item[0] == id and mode == '6':
            return item[6]
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def showAll(type):
    # Connect to database
    conn = sqlite3.connect('database.db')
    # Create a cursor
    c = conn.cursor()
    # Query the database
    c.execute(f'SELECT * FROM {type} ORDER BY code')
    items = c.fetchall()
    for item in items:
        if type == 'product':
            print(f'''
Código: {item[0]}
Nome: {item[1]}\tFabricante: {item[2]}
Preço:{item[3]:.2f}\tQuantidade: {item[4]}''')
        elif type == 'clients':
                print(f'''
Código: {item[0]}
Nome: {item[1]} {item[2]}
CPF: {item[3]}
Email: {item[4]}''')
        elif type == 'users':
            print(f'''
Usuário: {item[1]}
Senha: {item[2]}''')
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()
