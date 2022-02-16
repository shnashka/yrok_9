# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class in_out_loog(metaclass=ABCMeta):
    def __init__(self, file_name, log_name=None):
        self.file_name = file_name
        self.log_name = log_name
        self.log_line = {}
        self.out_data = []



    def sort_by(self):
        pass

    @abstractmethod
