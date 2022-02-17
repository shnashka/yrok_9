import os, time, shutil


class File:
    def __init__(self):
        self.in_name = ''
        self.out_name = ''
        self.sub = {}

    def do_it(self, input_path, output_path):
        self.in_name = os.path.join(os.path.dirname(__file__), input_path)
        self.out_name = os.path.join(os.path.dirname(__file__), output_path)
        self.sub = {}

        for dirpath, dirname, filename in os.walk(in_name):

            if filename:
                for file in filename:
                    file_path = os.path.join(dirpath, file)
                    date = os.path.getmtime(file_path)
                    date_norm = time.gmtime(date)
                    path = os.path.normpath(f'{date_norm.tm_year}\n{date_norm.tm_mon}')
                    target_path = os.path.join(out_name, path)
                    os.makedirs(target_path, exist_ok=True)
                    shutil.copy2(file_path, target_path)


do_it()
