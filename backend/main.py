from fastapi import FastAPI, Request
from urllib.parse import urlparse

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# custom validation exception
class ValidationException(Exception):
    pass


class ServerError(Exception):
    pass


def count_words(string):
    word_list = string.split(" ")  # split string into list of words
    word_dict = {}  # create empty dictionary
    for word in word_list:  # iterate over words
        word_dict[word] = word_dict.get(word, 0) + 1  # add word to dictionary with count 0 if it doesn't exist,
        # otherwise increment count

    items = list(word_dict.items())  # convert dictionary to list of tuples

    sorted_data = bubble_sort(items, sorting_logic=lambda x, y: x[1] < y[1])  # sort list of tuples by count

    return sorted_data


def bubble_sort(items, sorting_logic=lambda x, y: x[1] > y[1]):
    """
    Sort a list of items by a specified logic.
    :param items: list of items to be sorted
    :param sorting_logic: function that takes two items and returns True if first item should be sorted before second
    :return: sorted list of items
    """
    total = len(items)  # get total number of items
    for i in range(total):
        for j in range(i, total):
            if sorting_logic(items[i], items[j]):
                items[i], items[j] = items[j], items[i]
    return items


@app.get("/api/count")
async def count(request: Request):
    params = request.query_params
    string = params.get('string')

    if not string:
        raise ValidationException("String is required")

    try:
        sorted_data = count_words(string)
        data_list = count_words(string)
        data_dict = {key: value for key, value in data_list}
    except Exception as e:
        raise ServerError(e)

    return data_dict
