import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_tabe = 'CREATE TABLE users(id int, username text, password text)'
cursor.execute(create_tabe)


user=(1, 'jan', '1234')
insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'Tester', '12345'),
    (3, 'anne', '12345')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
