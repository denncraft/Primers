# Вариант№1 простой
#import os

#print(os.environ['SECRET_KEY'])

# Вариант№2 поинтереснее
# можно хранить чувствительную информацию в переменных окружения и загружать ее
# через класс Configuration методом get_env_key
# при отсутствии в окружении нужного ключа будет возвращен False
from os import environ


class Configuration:
    @staticmethod
    def get_env_key(key_name: str):
        return environ.get(key_name, False)
