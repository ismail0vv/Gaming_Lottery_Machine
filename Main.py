import random
import os
import time
from Display import Display


def clear_screen():
    os.system('cls' if os.name == 'windows' else 'clear')


def generate_numbers(avtomat):
    avtomat.choosing_number(0, random.randint(20, 40))
    avtomat.choosing_number(1, random.randint(20, 40))
    avtomat.choosing_number(2, random.randint(20, 40))


avtomat = Display(['1', '2', '3', '4', '5', '$'])
money = 10000
while True:
    if(money < 1000):
        print('Недостаточно денег :(')
        break
    answer = input(f'Остаток: {money}$\nЗапустить автомат? (-1000$) ')
    if answer.lower() == 'да':
        money -= 1000
        clear_screen()
        avtomat.clear_display()
        avtomat.display()
        time.sleep(1)

        generate_numbers(avtomat)

        clear_screen()
        money += avtomat.count_money()
    else:
        break

print(f'Вы ушли с {money}$')