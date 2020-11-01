import jellyfish

import init_db
import texts


def show_levenshtein_similarity(customer_question):
    print('Levenshtein similarity:')
    print(f'Customer question: {customer_question}')
    for idx, text in enumerate(texts.questions):
        distance = jellyfish.levenshtein_distance(customer_question, text)
        normalized_distance = 1 - distance / max(len(customer_question), len(text))
        print('Distance %.2f' % normalized_distance + ' | ' + text)


def show_sqllite_fulltextsearch_response(customer_question):
    print('SQL Full Text Search')
    print(f'Customer question: {customer_question}')
    connection = init_db.init()
    cursor = connection.cursor()
    query = "SELECT content, bm25(questions) FROM questions WHERE questions MATCH '" + customer_question + "' ORDER BY bm25(questions) DESC;"
    cursor.execute(query)
    print(cursor.fetchall())
    connection.close()


show_sqllite_fulltextsearch_response('The app is freezing')
show_levenshtein_similarity('The app is freezing')
