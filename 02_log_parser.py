# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

file_name = "events.txt"
log_name = "log.txt"


class in_out_loog(metaclass=ABCMeta):
    def __init__(self, ):

        self.log_line = {}
        self.out_data = []

    @abstractmethod
    def sort_by(self):
        pass

    def read_file(self):
        with open(file_name, mode='r', encoding='utf8') as original:
            for line in original:

                if line.endswith('NOK\n'):
                    if line[1:self.sort_by()] in self.log_line:
                        self.log_line[line[1:self.sort_by()]] += 1
                    else:
                        self.log_line[line[1:self.sort_by()]] = 1

    def write_file(self):

        self.out_data = sorted(start.log_line.items(), key=lambda x: x[0])
        if log_name == None:
            for key in self.out_data:
                print(f'[{key[0]}]:{key[1]}')
        else:
            with open(log_name, mode='w', encoding='utf8') as log:
                for key in self.out_data:
                    write_data = f'[{key[0]}]:{key[1]}\n'
                    log.write(write_data)

    def do_it(self):
        self.read_file()
        self.write_file()


class hour(in_out_loog):
    def sort_by(self):
        self._sort_by = 14
        return self._sort_by


class month(in_out_loog):
    def sort_by(self):
        self._sort_by = 8
        return self._sort_by


class year(in_out_loog):
    def sort_by(self):
        self._sort_by = 5
        return self._sort_by


class minut(in_out_loog):

    def sort_by(self):
        self._sort_by = 17
        return self._sort_by


start = minut()
start.do_it()
