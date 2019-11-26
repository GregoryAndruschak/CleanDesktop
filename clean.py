import os
import shutil
import time

if __name__ == "__main__":   
    os.chdir(os.path.join(os.path.join(os.path.expanduser('~')), 'Documents'))
    if not os.path.exists('Desktop'):
        os.makedirs('Desktop')
    os.chdir('Desktop')
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    desktop_files = [x for x in os.listdir(desktop) if not x[0] == '.']
    if len(desktop_files) > 0:
        today = time.strftime('%d.%m.%Y', time.localtime())
        if not os.path.exists(today):
            os.makedirs(today)
        os.chdir(today)
        for file in desktop_files:
            try:
                shutil.move(desktop + '/' + file, os.getcwd())
            except shutil.Error:
                index = 1
                same_file_name = True
                while same_file_name:
                    try:
                        temp_name = file.split('.')
                        temp_name[-2] += '(' + str(index) + ')'
                        new_file_name = ''.join(temp_name)
                        os.rename(desktop + '/' + file, desktop + '/' + new_file_name)
                        file = new_file_name
                        shutil.move(desktop + '/' + file, os.getcwd())
                        same_file_name = False
                    except shutil.Error:
                        index += 1
