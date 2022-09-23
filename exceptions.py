# исключения являются объектами, наследуемыми от BaseException
# Вторым уровнем идут: Exception, SystemExit, GeneratorExit, KeyboardInterrupt
# Третий уровень: AttributerError, ArithmeticError, EOFError, NameError, LookupError, OSError, TypeError, ValeError
# Арифметические подразделяются на: ZeroDivisionError, FloatingPointError, OverflowError
# Lookup подразделяются на: IndexError, KeyError
# Системные подразделяются на: FileNotFoundError, InterruptedError, PermissionError, TimeOutError

#a = 1/0
try:
    a = 2 / 0
except ZeroDivisionError:
    print("a = 2/0 !!! Ну нельзя делить на ноль")

#int(input('Введите значение: '))
try:
    int(input('Введите значение: '))
except ValueError:
    # можно кастомизировать выводимые сообщения исключений вызовом raise
    raise ValueError("Необходимо вводить только цифры")