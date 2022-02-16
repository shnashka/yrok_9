class StatCounter:
    def __init__(self, file_name, sort_method='Ascending'):
        self.file_name = file_name
        self.stat = {}
        self.sort_method = sort_method
        self.alpha_counter = 0
        self.sorted_static = []

    def collect_stat(self):

        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                        self.alpha_counter += 1

    def sorting(self):

        for key, value in self.stat.items():
            self.sorted_static.append([key, value])
        match self.sort_method:
            case 'Ascending':
                self.sorted_static.sort(key=lambda val: val[1], reverse=False)
            case 'Descending':
                self.sorted_static.sort(key=lambda val: val[1], reverse=True)
            case 'abcAscending':
                self.sorted_static.sort(key=lambda val: val[0], reverse=False)
            case 'abcDescending':
                self.sorted_static.sort(key=lambda val: val[0], reverse=True)

    def print_stat(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for items in self.sorted_static:
            print('|{:^9}|{:^10}|'.format(items[0], items[1]))
        print('+---------+----------+')
        print('|  Итого  |{:^10}|'.format(self.alpha_counter))
        print('+---------+----------+')

    def do_it(self):
        self.collect_stat()
        self.sorting()
        self.print_stat()


counter = StatCounter(file_name='voyna-i-mir.txt', sort_method='Ascending')  # 'Ascending'-по возрастанию частоты;
counter.do_it()
