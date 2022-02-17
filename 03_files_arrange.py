import os, time, shutil, zipfile



def do_it():
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
