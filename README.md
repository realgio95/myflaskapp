# Myflaskapp
This is a tutorial on using [Flask](https://github.com/pallets/flask) Backend with MySQL from Scratch. 

=====

### Requirements
..* Python
..* pip
..* MySQL

###Setting up the Project
Fork the repository and cd into to Project Directory
1. pip install flask
2. pip install flask_mysqldb
3. pip install wtforms
4. pip install passlib
5. pip install functools
6. Set up the Database

### Run the Project
`cd myflaskapp`

`python app.py`

`Point yor browser to [Localhost](https://localhost:5000)`


##### Setting up Database, make sure that database is set up
`CREATE DATABASE myflaskapp;`

#### USE myflaskapp db using MySQL
```
CREATE TABLE users (id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(30), username VARCHAR(30),email VARCHAR(100), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```

```
CREATE TABLE articles (id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

Set Up db.py as follows:
```
def DBconfig():
    dbconfig = {
        "host": 'localhost',
        "user": 'INSERT DB USER NAME',
        "password": 'INSERT DB PASSWORD',
        "DBName": 'myflaskapp',
        "dictDB": 'DictCursor',
    }
    return dbconfig
```
