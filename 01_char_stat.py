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

    def print_stat(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for items in self.sorted_static:
            print('|{:^9}|{:^10}|'.format(items[0], items[1]))
        print('+---------+----------+')
        print('|  Итого  |{:^10}|'.format(self.alpha_counter))
        print('+---------+----------+')

    @abstractmethod
    def _stats(self):
        pass
    def do_anal(self):
        self._stats()
        self.statistics()
        self.print_stat()



class key_up(Stat_counting):
    def _stats(self):
        self._stats = sorted(self.statistic.items(), key=lambda x: x[0])


class key_doun(Stat_counting):
    def sort_result(self):
         self._stats = sorted(self.statistic.items(), key=lambda x: x[1], reverse=True)


class sourt_down(Stat_counting):
    def sort_result(self):
        self.sorted_static.clear()
        self.sorted_static = sorted(self.statistic.items())


class sourt_up(Stat_counting):
    def sort_result(self):
        self.sorted_static.clear()
        self.sorted_static = sorted(self.statistic.items(), reverse=True)


file_path = "voyna-i-mir.txt"
ta = key_up(file_path)
ta.do_anal()
