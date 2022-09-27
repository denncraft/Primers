import os
import re


def walk_dir(dir: str, only_dirs=False):
    try:
        for file in os.listdir(dir):
            cur_path = os.path.join(dir, file)
            if os.path.isdir(cur_path):
                if has_cyrillic(file) and only_dirs:
                    print(f'{cur_path}')
                walk_dir(cur_path, only_dirs)
            elif has_cyrillic(file) and not only_dirs:
                print(f'{cur_path}')
    except OSError:
        return


def has_cyrillic(text: str):
    return bool(re.search('[а-яА-ЯёЁ]', text))


#walk_dir(dir='g:\\Shared drives\\D K\\', only_dirs=True)
walk_dir(dir='G:\Shared drives\D K')
