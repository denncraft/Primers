class DataBase():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # т.к. все создаваемые классы наследуются от класса Object
            # все классы имеют магические методы, даже если они в них не определены
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, passw, port):
        self.user = user
        self.passw = passw
        self.port = port

    def get_info(self):
        print(self.user, self.passw, self.port)

    def __del__(self):
        DataBase.__instance = None

db = DataBase('root', '12345', 80)
db2 = DataBase('user', '5678', 81)
# нового экземпляра класса не создается
print(id(db), id(db2))
# но переопределение значений арибутов все же происходит
db.get_info()
del db
del db2
# хотя экземпляры класса db и db2 были удалены, т.е. ссылок на класс больше не существует,
# метод __del__ не был вызван и атрибут класса __instance не был сброшен в состояние None
db3 = DataBase('admin','password','1443')
print(id(db3))
db3.get_info()
#print(id(db2))
