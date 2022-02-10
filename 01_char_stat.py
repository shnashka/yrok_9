import zipfile
from abc import ABCMeta, abstractmethod


class Stat_counting(metaclass=ABCMeta):
    def __init__(self, file_name):
        self.statistic = {}
        self.sorted_static = []
        self.file_name = file_name
        self.alpha_counter = 0

    def statistics(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.statistic:
                            self.statistic[char] += 1
                        else:
                            self.statistic[char] = 1
        for key, item in self.statistic.items():
            self.alpha_counter += item
