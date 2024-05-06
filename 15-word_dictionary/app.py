from PyDictionary import PyDictionary
from pprint import pprint

# method 3
dictionary = PyDictionary("eyes", "apple")

pprint(dictionary.getMeanings())

# method 2
# dictionary = PyDictionary()

# while True:
#     word = input("enter your word: ")
#     if word == '':
#         break
#     pprint(dictionary.meaning(word))

# method 1
# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eyes': 'an organ for seeing',
#         'earth': 'a planet in space',
#     }

#     while True:
#         word = input("enter a word: ")

#         if word == '':
#             break
#         if word in word_dictionary:
#             print(word, ": ", word_dictionary[word])

# main()