import json
from random import shuffle

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

user_list = []
report = ''
money = 0
class User():
    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.position = position
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.cash = self.calculate_salary()

    def calculate_salary(self, k=1):
        return self.hours_worked * self.hourly_rate * k

    def get_info(self):
        text = f'{self.name},  {self.position}, зп – {self.cash}$'
        return text

    def __repr__(self):
        return f'{self.name}'




def add_person():
    for person in data:
        user_list.append(
            User(person['name'], person['position'], person['hours_worked'], person['hourly_rate']))

def get_report():
    global report, money
    add_person()
    for user in user_list:
        report += f'{user.get_info()}\n'
        money += user.cash
    return f'{report}\n{money}'

print(get_report())
