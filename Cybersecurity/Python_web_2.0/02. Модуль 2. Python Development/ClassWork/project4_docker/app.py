from flask import Flask
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql = MySQL()

# Налаштування підключення
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'my_sql_database'
# ВАЖЛИВО: host має збігатися з назвою сервісу в docker-compose.yml
app.config['MYSQL_DATABASE_HOST'] = 'database' 

mysql.init_app(app)

@app.route('/')
def hello_world():
    # Використовуємо try/except, щоб уникнути падіння, якщо база ще вантажиться
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        
        # Використовуємо стандартний SQL синтаксис (без одинарних лапок для імен таблиць)
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(20) NOT NULL, PRIMARY KEY (id))")
        
        # Виправляємо помилку: connection.commit() замість cursor.comit()
        cursor.execute("INSERT INTO users (name) VALUES ('Hrigoriu')")
        connection.commit()
        
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return str(users)
    except Exception as e:
        return f"Помилка підключення: {e}. Спробуйте оновити сторінку через 10 секунд."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
     
    # 127.0.0.1 - це "домашня адреса" твого комп'ютера, яка дозволяє браузеру знайти сервер, що працює на твоєму комп'ютері. Якщо ти використовуєш 0.0.0.0, браузер не зможе знайти сервер на Windows.