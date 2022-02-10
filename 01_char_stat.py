import zipfile
from abc import ABCMeta, abstractmethod


class Stat_counting(metaclass=ABCMeta):
    def __init__(self, file_name):
        self.statistic = {}
        self.sorted_static = []
        self.file_name = file_name
        self.alpha_counter = 0

    def statistics(self):
        self.statistic = {}
        alpha_counter = 0
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.statistic:
                            self.statistic[char] += 1
                        else:
                            self.statistic[char] = 1
        for key in self.statistic:
            alpha_counter += self.statistic[key]
        self.alpha_counter = alpha_counter

