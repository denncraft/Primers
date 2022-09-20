class Vektor:
    # атрибуты класса
    MAX_COORD = 100
    MIN_COORD = 0

    # методы класса

    def __init__(self, x, y):
        self.x = 0;
        self.y = 0
        # обычные методы могут обрааться к методам класса, но не наоборот
        if self.validate(x) and self.validate(y):
            # атрибуты экземпляров класса
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    # метод класса не имеет информации (ссылки) на экземпляр класса его вызвавший, но имеет ссылку на сам класс
    # методы класса не могут работать с атрибутами экземраляров класса
    @classmethod
    def validate(cls, z):
        print(cls)
        return cls.MAX_COORD >= z >= cls.MIN_COORD

    # статичные метода вообще не принимают ссылок, только атрибуты которыми оперируют
    # но вполне могут обращаться к методам класса, но этого делать НЕ РЕКОМЕНДУЕТСЯ
    @staticmethod
    def norm2(x, y):
        return x * x + y * y


print('создаем экземпляр класса Vektor')
v = Vektor(5, 99)
print('получаем координаты переданных в класс значений x и y')
print(v.get_coords())
print('смотрим на ссылку экземпляра класса')
print(v)
print('вызываем метод класса')
print('хоть вызов и произошел из экземпляра класса, но в самом методе используется ссылка на класс')
print(v.validate(5))
# эквивалентно
print(Vektor.validate(5))
print('Обращение к статическому методу')
print(v.norm2(5, 6))
