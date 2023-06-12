import sqlite3 as sq

path = r'users.db'


def create_tables() -> None:
    """ Функция для создания БД и таблиц """
    with sq.connect(path) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY autoincrement,
               username TEXT,
               status TEXT,
               stage TEXT);
            """)


def get_data(string: str) -> list:
    """ Функция для получения данных из БД в зависимости от запроса """
    with sq.connect(path) as con:
        cur = con.cursor()
        cur.execute(string)
        return cur.fetchall()


def delete_tables(*args) -> None:
    """ Функция для удаления таблиц из БД """
    with sq.connect(path) as con:
        cur = con.cursor()
        for table in args:
            cur.execute(f"DROP TABLE IF EXISTS {table}")


def delete_data(*args) -> None:
    """ Функция для удаления данных из таблиц """
    with sq.connect(path) as con:
        cur = con.cursor()
        for table in args:
            cur.execute(f"DELETE FROM {table}")
    with sq.connect(path) as con:
        cur = con.cursor()
        for _ in args:
            cur.execute("VACUUM")


def get_all_from_table(table: str) -> list:
    """ Функция для получения всех данных из одной таблицы """
    with sq.connect(path) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * from {table}")
        return cur.fetchall()


def set_data(string, values=tuple(), multiple=False) -> bool:
    """ Функция для записи данных в БД """
    with sq.connect(path) as con:
        cur = con.cursor()
        if multiple:
            cur.executemany(string, values)
        elif len(values) != 0:
            cur.execute(string, values)
        else:
            cur.execute(string)
        return True


def set_users(users: tuple) -> bool:
    """ Функция для записи данных в таблицу users """
    return set_data(
        string=f"INSERT INTO users(username, status, stage)"
               f"VALUES(?, ?, ?);",
        values=users)


def get_users(username: str) -> list:
    """ Функция для получения данных из таблицы users """
    user = get_data(
        string=f"SELECT username, status, stage from users WHERE username = '{username}'")
    return user


def set_user_by_username(username: str,
                         status: str = None,
                         stage: int = None) -> bool:
    """ Функция для обновления данных по конкретному юзеру """
    with sq.connect(path) as con:
        cur = con.cursor()
        if status and stage:
            cur.execute(f"""UPDATE users SET 
            status = '{status}',
            stage = '{stage}'
            WHERE username = '{username}';""")
        elif status:
            cur.execute(f"""UPDATE users SET 
            status = '{status}'
            WHERE username = '{username}';""")
        elif stage:
            cur.execute(f"""UPDATE users SET 
            stage = '{stage}'
            WHERE username = '{username}';""")
    return True


def clear_database():
    """ Очистка базы данных """
    delete_data('users')
