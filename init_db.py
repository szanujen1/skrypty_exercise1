import sqlite3

import texts


def init():
    conn = sqlite3.connect('max.sqlite')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS questions")
    cur.execute("DROP TABLE IF EXISTS answers")

    conn.execute("CREATE VIRTUAL TABLE questions USING fts5(key, content);")
    conn.execute("CREATE VIRTUAL TABLE answers USING fts5(key, content);")

    for idx, text in enumerate(texts.questions):
        cur.execute('INSERT INTO questions(key, content) VALUES("' + str(idx) + '", "' + text + '");')
        conn.commit()
    for idx, text in enumerate(texts.answers):
        cur.execute('INSERT INTO answers(key, content) VALUES("' + str(idx) + '", "' + text + '");')
        conn.commit()

    return conn

# query = cur.execute("SELECT content FROM questions;")
# print(cur.fetchall())
# query2 = cur.execute("SELECT content FROM answers;")
# print(cur.fetchall())
#
# conn.close()
