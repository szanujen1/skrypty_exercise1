import jellyfish

import texts

similarity_threshold = 0.2


def get_highest_similarity(customer_question):
    max_similarity = 0
    highest_index = 0
    for idx, text in enumerate(texts.questions):
        distance = jellyfish.levenshtein_distance(customer_question, text)
        similarity = 1 - distance / max(len(customer_question), len(text))  # print(similarity)
        if similarity > max_similarity:
            highest_index = idx
            max_similarity = similarity
    if max_similarity > similarity_threshold:
        return texts.answers[highest_index]
    else:
        return "The issues has been saved. We will contact you soon."


def run_chatbot():
    print(texts.welcome)
    question = ""
    while question != "thank you":
        question = input()
        answer = get_highest_similarity(question)
        print(answer)


run_chatbot()
