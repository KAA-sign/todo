# todo

## 1. Настройки для VS_code

```  json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Windows: Django",
            "type": "python",
            "request": "launch",
            // change below if your manage.py in different location
            "program": "${workspaceFolder}\\todo\\manage.py",
            "args": [
                "runserver",
                // "--noreload"
            ],
            "django": true
        },
        {
            "name": "WSL: Django",
            "type": "python",
            "request": "launch",
            // change below if your manage.py in different location
            "program": "${workspaceFolder}/todo/manage.py",
            "args": [
                "runserver",
                // "--noreload"
            ],
            "django": true
        }
    ]
}
```

## 2. Установка PostgreSQL

sudo apt update

sudo apt install postgresql postgresql-contrib

> sudo service postgresql status позволяет проверить состояние

> sudo service postgresql start позволяет запустить

> sudo service postgresql stop позволяет завершить работу

sudo passwd postgres

sudo service postgresql start

sudo -u postgres psql

>> CREATE DATABASE todo;

>> alter user postgres with encrypted password '7415963';

## 3. Django

django-admin startproject todo .