from accessify import private


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def __get_old(self):
        # дополнительные действия при считывании значения аттрибута
        return self.__old

    def __set_old(self, old):
        # проверка и обработка поступившего значения до записи в аттрибут
        self.__old = old

    old = property(__get_old, __set_old)

    # using features of accessify module, but this feature works for methods, not attributes
    @private
    def some_method(self):
        print('This is a private method')

    def access_to_private_method(self):
        return self.some_method()


p = Person('denis', 42)
p.old = 41
print(p.old, p.__dict__)

# p.some_method() # --> error
p.access_to_private_method()
print(p.__dict__)