def Articles():
    articles = [
        {
            'id': 1,
            'title': 'Article One',
            'body': 'Lorem ipsum dolor sit amet, qui no mutat utamur assuever',
            'author': 'Brad Traversy',
            'create_date': '04-25-2017'
        }, {
            'id': 2,
            'title': 'Article Two',
            'body': 'Qui no mutat utamur assueverit, molestiae',
            'author': 'John Traversy',
            'create_date': '04-26-2017'
        }, {
            'id': 3,
            'title': 'Article Three',
            'body': 'Magna delectus molestiae nam at. Ut affert iudi.',
            'author': 'Brandy Macmillan',
            'create_date': '04-27-2017'
        }, {
            'id': 4,
            'title': 'Article Four',
            'body': 'Utamur assueverit, magna delectus at.',
            'author': 'Johnny Diapinsnagen',
            'create_date': '04-29-2017'
        }
    ]
    return articles

#  CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, 
#  name VARCHAR(100), email VARCHAR(100),username VARCHAR(30), password 
#  VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);