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
    1 / 0
    'hello'[9]
    int(input('Введите значение: '))

except ValueError:
    # можно кастомизировать выводимые сообщения исключений вызовом raise
    raise ValueError("Необходимо вводить только цифры")

# у одного блока try могут быть описаны несколько различных исключений
except ZeroDivisionError:
    print('На ноль делить нельзя')

# роверяемые исключения можно комбинировать в одном блоке except
except (KeyError, IndexError):
    print('LookupError')

# блок else выполнится при ошибке, но только если не происходит исключений
else:
    print('Блок else')

# блок finaly выполняется в любом случае
finally:
    print('Блок finaly выполняется в любом случае')