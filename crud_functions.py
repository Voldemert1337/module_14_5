import sqlite3


def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    balance INTEGER
    )
    ''')

    connection.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL 
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    initiate_db()
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


def add_user(username, email, age):
    '''
    Данная функция принимает имя пользователя(username), почту(email), и возраст(age)
    и добавляет преданные данные в таблицу Users
    '''
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', f'{1000}'))
    connection.commit()


def is_included(username):
    '''
    Функция принимает имя пользователя и возвращает True, если такой пользователь уже существует в таблице User,
    в противном случае False
    '''
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    check_users = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_users.fetchone() is None:
        return False
    else:
        return True
