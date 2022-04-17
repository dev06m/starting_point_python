# from OOP.coffee import Coffee
# from OOP_Person.person import Person
# from QuizProject.question import Question
#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# QUESTIONS = {
#     1: {"question": "3 + 5", "answer": 8},
#     2: {"question": "3 - 5", "answer": -2},
#     3: {"question": "3 * 5", "answer": 15},
# }
#
# print(MENU['espresso'].get('ingredients')['water'])
#
# question_1 = Question(QUESTIONS[1].get('question'), QUESTIONS[1].get('answer'))
# question_2 = Question(QUESTIONS[2].get('question'), QUESTIONS[2].get('answer'))
# question_3 = Question(QUESTIONS[3].get('question'), QUESTIONS[3].get('answer'))
#
# question_objects = [question_1, question_2, question_3]
#
# for item in question_objects:
#     answer = input(f'{item.text} = ? -->\t')
#     item.check__answer(int(answer))

import threading


def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")


printit()
