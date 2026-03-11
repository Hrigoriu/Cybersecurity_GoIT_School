# ===================================================================================================
#! Стандарт PEP249 (Python Database API Specification v2.0) !
# ===================================================================================================
# Методи Cursor
# execute() - Виконує SQL-запит
# executemany() - Виконує SQL-запит для кожного елемента в послідовності
# fetchone() - Повертає наступний рядок результату запиту
# fetchmany(size) - Повертає наступні size рядків результату запиту
# fetchall() - Повертає всі рядки результату запиту
# close() - Закриває об'єкт Cursor
# rowcount - Властивість, що повертає кількість рядків, які були змінені або вибрані останнім виконаним запитом
# description - Властивість, що повертає інформацію про стовпці результату запиту
# Методи Connection
# cursor() - Створює об'єкт Cursor для виконання SQL-запитів
# commit() - Фіксує транзакцію
# rollback() - Відкочує транзакцію
# close() - Закриває з'єднання з базою даних
# Винятки
# DatabaseError - Базовий клас для всіх винятків, пов'язаних з базою даних
# IntegrityError - Виняток, що виникає при порушенні цілісності даних
# OperationalError - Виняток, що виникає при помилках операцій з базою даних
# ProgrammingError - Виняток, що виникає при помилках у програмуванні SQL-запитів
# InterfaceError - Виняток, що виникає при помилках у інтерфейсі між Python і базою даних
# DataError - Виняток, що виникає при помилках у даних, що передаються в базу даних
# NotSupportedError - Виняток, що виникає при спробі використовувати функціональність, яка не підтримується базою даних
# ===================================================================================================
# Підключення до бази даних
# connect.py
import sqlite3
from contextlib import contextmanager

database = "./test.db"


@contextmanager
def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ================================================================================================
# Створення таблиць
# create_table.py
from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
     id integer PRIMARY KEY,
     name text NOT NULL,
     begin_date text,
     end_date text
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id integer PRIMARY KEY,
     name text NOT NULL,
     priority integer,
     project_id integer NOT NULL,
     status Boolean default False,
     begin_date text NOT NULL,
     end_date text NOT NULL,
     FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
# ===================================================================================================
# Заповнення таблиць
# seed.py
from sqlite3 import Error

from connect import create_connection, database


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """ 
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?); 
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = """ 
    INSERT INTO tasks(name,priority,status,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == "__main__":
    with create_connection(database) as conn:
        # create a new project
        project = ("Cool App with SQLite & Python", "2022-01-01", "2022-01-30")
        project_id = create_project(conn, project)
        print(project_id)

        # tasks
        task_1 = (
            "Analyze the requirements of the app",
            1,
            True,
            project_id,
            "2022-01-01",
            "2022-01-02",
        )
        task_2 = (
            "Confirm with user about the top requirements",
            1,
            False,
            project_id,
            "2022-01-03",
            "2022-01-05",
        )

        # create tasks
        print(create_task(conn, task_1))
        print(create_task(conn, task_2))
# ===================================================================================================
# Запити до бази даних
# select.py
from sqlite3 import Error

from connect import create_connection, database


def select_projects(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows projects
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_task_by_status(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param status:
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE status=?", (status,))
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


if __name__ == "__main__":
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(projects)
        print("\nQuery all tasks")
        tasks = select_all_tasks(conn)
        print(tasks)
        print("\nQuery task by status:")
        task_by_priority = select_task_by_status(conn, True)
        print(task_by_priority)
# ===================================================================================================
# Зміна даних
# update.py
from sqlite3 import Error

from connect import create_connection, database


def update_task(conn, parameters):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param parameters:
    :return:
    """
    sql = """ 
    UPDATE tasks
    SET priority = ?, begin_date = ?, end_date = ?
    WHERE id = ?
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def update_task_status(conn, parameters):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param parameters:
    :return:
    """
    sql = """ 
    UPDATE tasks
    SET status = ? 
    WHERE id = ?
    """

    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == "__main__":
    with create_connection(database) as conn:
        update_task(conn, (2, "2022-01-04", "2022-01-06", 1))
        update_task_status(conn, (True, 2))
# ===================================================================================================
# Видалення даних
# delete.py
from sqlite3 import Error

from connect import create_connection, database


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = "DELETE FROM tasks WHERE id=?"
    cur = conn.cursor()
    try:
        cur.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == "__main__":
    with create_connection(database) as conn:
        delete_task(conn, 1)
# ===================================================================================================
# Висновок даних з декількох таблиць
# conclusion.py
from sqlite3 import Error

from connect import create_connection, database


def select_projects(conn):
    """
    Query all rows in the projects table with its tasks
    :param conn: the Connection object
    :return: rows projects or None
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM projects JOIN tasks ON tasks.project_id = projects.id;"
        )
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


if __name__ == "__main__":
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(projects)

# ===================================================================================================
