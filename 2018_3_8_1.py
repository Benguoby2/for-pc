import socket
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'GUO', b'LI', b'WANG', b'exit']:
    s.sendto(data, ('127.0.0.1', 9998))
    print(s.recv(1024).decode('utf-8'))
s.close()
"""
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(r'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('SELECT * from user where score=?', (61,))
values = cursor.fetchall()
#print(values)

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    high = high + 1
    names = []


    for score_1 in range(low, high):
        cursor.execute('SELECT * from user where score=?', (score_1,))
        values = cursor.fetchall()
        if values:
            names.append(values[0][1])
    return names





assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60,80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam',], get_score_in(60, 100)
