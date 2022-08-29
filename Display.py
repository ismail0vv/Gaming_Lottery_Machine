import os
import time


def clear_screen():
    os.system('cls' if os.name == 'windows' else 'clear')


class Display:

    def __init__(self, nums):
        self.__nums = nums
        self.__lst = [' ', ' ', ' ']

    @property
    def nums(self):
        return self.__nums

    @property
    def lst(self):
        return self.__lst

    def display(self):
        print('╔═╦═╦═╗ ▄')
        print(f'║{self.lst[0]}║{self.lst[1]}║{self.lst[2]}║─┘')
        print('╚═╩═╩═╝')

    def choosing_number(self, pos, spins):
        for i in range(spins):
            self.lst[pos] = self.nums[i % len(self.nums)]
            self.display()
            time.sleep(0.05)
            if i < spins - 1:clear_screen()
        time.sleep(1)
        if pos != 2: clear_screen()
    def count_money(self):
        amount = 0
        if self.lst[0] == self.lst[1] and self.lst[0] == self.lst[2]:
            if self.lst[0] == '1':
                amount = 1000
            elif self.lst[0] == '2':
                amount = 2000
            elif self.lst[0] == '3':
                amount = 3000
            elif self.lst[0] == '4':
                amount = 4000
            elif self.lst[0] == '5':
                amount = 5000
            else:
                amount = 50000
                print('Вы сорвали джекпот')

        print(f'Вы выиграли {amount}$')
        return amount

    def clear_display(self):
        self.__lst = [' ', ' ', ' ']