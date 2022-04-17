class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def print__question(self):
        print(self.text)

    def check__answer(self, answer_of_participant):
        if answer_of_participant == self.answer:
            print('you answered correctly')
        else:
            print('bilemedin yamuldun')