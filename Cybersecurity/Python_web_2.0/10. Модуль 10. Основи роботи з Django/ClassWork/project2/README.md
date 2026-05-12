# Інструкція

## 1

```text
poetry init
poetry install
poetry shell
exit
```

```text
poetry add Django
```

```text
django-admin startproject notes
```

```text
poetry add Django
```

```text
cd notes
```

```text
docker run --name noteapp-postgres -p 5433:5432 -e POSTGRES_PASSWORD=567234 -d postgres
```

```text
poetry add psycopg2
```

```text
python manage.py migrate
```

```text
python manage.py createsuperuser
```

"""
Login:Admin Password:Admin
"""

```text
python manage.py runserver
```

```text
localhost:8000
```

```text
http://127.0.0.1:8000/admin
```

## 2

```text
python manage.py startapp noteapp
```

```text
python manage.py makemigrations
```

```text
python manage.py migrate
```

```text
localhost:8000
```
