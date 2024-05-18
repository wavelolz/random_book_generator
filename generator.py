import numpy as np
import pandas as pd
import random

def GenerateRandomBookList(df):
    data = pd.read_csv("book_data.csv")
    codes = np.arange(0, 10, 1)
    books = []
    for code in codes:
        books.append(list(data.loc[data["Category"]==code]["Book Title"]))
    book_dict = {}
    for code in codes:
        book_dict[str(code)] = books[code]

    code_strs = [str(i) for i in codes]
    answers = []
    questions = []
    for i in range(28):
        answer = random.sample(code_strs, 5)
        question = [random.sample(book_dict[i], 1)[0] for i in answer]
        answers.append("".join(answer))
        questions.append(",".join(question))

    df = pd.DataFrame({
        "代碼" : answers,
        "書本清單" : questions
    })
    return df