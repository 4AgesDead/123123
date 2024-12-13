import json, random


with open('quests.json', 'r', encoding='utf-8') as file:
    list_quest = json.loads(file.read())



class Quests():
    def __init__(self, quest, diff, answer):
        self.quest = quest
        self.diff = diff
        self.answer = answer
        self.quested = False
        self.user_answer = None
        self.scores = self.get_points()

    def get_points(self):
        return self.diff * 10

    def is_correct(self):
        if self.user_answer == self.answer:
            return True
        else:
            return False


class Works():
    def __init__(self):
        self.list_quest = []
        self.random_numb = None
        self.make_list()

    def make_list(self):
        for quest in list_quest:
            self.list_quest.append([Quests(quest['quest'], quest['dif'], quest['answer']), False])

    def build_question(self):
        if self.list_quest[self.random_numb][1] == False:
            print(self.list_quest[self.random_numb][0].quest, )
            print('diff', self.list_quest[self.random_numb][0].diff)
            self.list_quest[self.random_numb][0].user_answer = input("ur answer ")
        else:
            self.build_question()

    def build_feedback(self):
        if self.list_quest[self.random_numb][0].is_correct():
            print('Боже, а ты хорош, получено',  self.list_quest[self.random_numb][0].scores, ' баллов')
        else:
            print('АХАХАХАХАХХА ЛОХ, верный ответ', self.list_quest[self.random_numb][0].answer)

    def is_correct(self):
        if self.list_quest[self.random_numb][0].user_answer == self.list_quest[self.random_numb][0].answer:
            return True
        else:
            return False
    def work(self):

        self.random_numb = random.randint(0, len(list_quest)-1)
        self.build_question()
        self.build_feedback()

Works().work()
'''
for i in range(len(list_quest)-1):
    a = random.randint(0,len(list_quest)-1)
    quest = Quests(list_quest[a]['quest'], list_quest[a]['dif'], list_quest[a]['answer'])
    quest.build_question()
    quest.user_answer = input("ur answer ")
    quest.build_feedback()'''
