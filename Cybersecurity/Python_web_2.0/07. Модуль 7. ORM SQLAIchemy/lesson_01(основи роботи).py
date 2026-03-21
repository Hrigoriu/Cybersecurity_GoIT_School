# ==============================================================================================
"""
    ! ORM (Object Relationship Mapper) пакет SQLALchemy !
дозволяє створювати об'єктно-орієнтовану модель бази даних, яка відображає структуру таблиць та їх взаємозв'язки. Це дозволяє розробникам працювати з базою даних на рівні об'єктів, а не на рівні SQL-запитів, що спрощує розробку та підтримку коду.
"""


# ==============================================================================================
def create_projects_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS projects (
                id integer PRIMARY KEY,
                name text NOT NULL,
                begin_date text,
                end_date text
            );"""
        )
    except Error as e:
        print(e)


def create_tasks_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id integer PRIMARY KEY,
                name text NOT NULL,
                priority integer,
                project_id integer NOT NULL,
                status_id integer NOT NULL,
                begin_date text NOT NULL,
                end_date text NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            );"""
        )
    except Error as e:
        print(e)


# ==============================================================================================
