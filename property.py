class Person:
    def __init__(self, name, old):
        self.__name = name
        self.old = old
        # так тоже работает, потому что при создании property в __dict__
        # создается атрибут с таким же именем, но с двумя подчеркиваниями
        # а так как имена атрибута, метода и property совпадают, то все работает

    # устанавливается декоратор, который из метода делает property и сразу же этому методу назначается getter с именем самого метода
    @property
    def old(self):
        # дополнительные действия при считывании значения аттрибута
        return self.__old

    # через ранее определенное property c именем old декоратором преобразуем метод
    # и назначаем его методом setter для свойства old
    @old.setter
    def old(self, old):
        # проверка и обработка поступившего значения до записи в аттрибут
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('denis', 42)
p.old = 41
print(p.old, p.__dict__)
