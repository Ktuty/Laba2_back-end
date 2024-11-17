# Шаг 1: Функции, которые выбрасывают исключения при определённых значениях входных параметров
def divide(a: float, b: float) -> float:
    """
    Функция деления, выбрасывает исключение при делении на ноль.

    Args:
        a (float): Числитель.
        b (float): Знаменатель.

    Returns:
        float: Результат деления.

    Raises:
        ValueError: Если знаменатель равен нулю.
    """
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b

def get_list_element(lst: list, index: int) -> any:
    """
    Функция получения элемента списка, выбрасывает исключение при неверном индексе.

    Args:
        lst (list): Список.
        index (int): Индекс элемента.

    Returns:
        any: Элемент списка.

    Raises:
        IndexError: Если индекс выходит за пределы списка.
    """
    if index < 0 or index >= len(lst):
        raise IndexError("Индекс выходит за пределы списка")
    return lst[index]

# Шаг 2: Функция с одним обработчиком исключений общего типа
def safe_divide(a: float, b: float) -> float:
    """
    Функция деления с обработкой исключений.

    Args:
        a (float): Числитель.
        b (float): Знаменатель.

    Returns:
        float: Результат деления или None в случае ошибки.
    """
    try:
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Шаг 3: Функция с одним обработчиком исключений общего типа и блоком finally
def safe_get_list_element(lst: list, index: int) -> any:
    """
    Функция получения элемента списка с обработкой исключений и блоком finally.

    Args:
        lst (list): Список.
        index (int): Индекс элемента.

    Returns:
        any: Элемент списка или None в случае ошибки.
    """
    try:
        if index < 0 or index >= len(lst):
            raise IndexError("Индекс выходит за пределы списка")
        return lst[index]
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        print("Операция завершена")

# Шаг 4: Функции с несколькими обработчиками разных типов исключений
def process_number(num: int) -> int:
    """
    Функция обработки числа с несколькими обработчиками исключений.

    Args:
        num (int): Число для обработки.

    Returns:
        int: Удвоенное число или None в случае ошибки.
    """
    try:
        if num < 0:
            raise ValueError("Число должно быть неотрицательным")
        elif num > 100:
            raise OverflowError("Число слишком большое")
        return num * 2
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except OverflowError as oe:
        print(f"Ошибка переполнения: {oe}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Обработка числа завершена")

def read_file(file_path: str) -> str:
    """
    Функция чтения файла с несколькими обработчиками исключений.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        str: Содержимое файла или None в случае ошибки.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as fnf:
        print(f"Файл не найден: {fnf}")
    except IOError as io:
        print(f"Ошибка ввода-вывода: {io}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Чтение файла завершено")

def calculate_square_root(num: float) -> float:
    """
    Функция вычисления квадратного корня с несколькими обработчиками исключений.

    Args:
        num (float): Число для вычисления квадратного корня.

    Returns:
        float: Квадратный корень числа или None в случае ошибки.
    """
    try:
        if num < 0:
            raise ValueError("Число должно быть неотрицательным")
        return num ** 0.5
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except TypeError as te:
        print(f"Ошибка типа: {te}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Вычисление квадратного корня завершено")

# Шаг 5: Функция, генерирующая исключения и обрабатывающая их
def validate_age(age: int) -> str:
    """
    Функция валидации возраста, генерирующая и обрабатывающая исключения.

    Args:
        age (int): Возраст для валидации.

    Returns:
        str: Сообщение о допустимости возраста или None в случае ошибки.
    """
    try:
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        elif age > 120:
            raise ValueError("Возраст слишком большой")
        return f"Возраст {age} является допустимым"
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Валидация возраста завершена")

# Шаг 6: Пользовательские исключения
class CustomError(Exception):
    """Базовое пользовательское исключение."""
    pass

class NegativeValueError(CustomError):
    """Исключение для отрицательных значений."""
    pass

class TooLargeValueError(CustomError):
    """Исключение для слишком больших значений."""
    pass

class InvalidTypeError(CustomError):
    """Исключение для недопустимых типов."""
    pass

# Шаг 7: Функция, выбрасывающая пользовательское исключение
def check_value(value: any) -> str:
    """
    Функция проверки значения, выбрасывающая пользовательское исключение.

    Args:
        value (any): Значение для проверки.

    Returns:
        str: Сообщение о допустимости значения или None в случае ошибки.
    """
    try:
        if value < 0:
            raise NegativeValueError("Значение не может быть отрицательным")
        elif value > 100:
            raise TooLargeValueError("Значение слишком большое")
        elif not isinstance(value, (int, float)):
            raise InvalidTypeError("Недопустимый тип значения")
        return f"Значение {value} является допустимым"
    except NegativeValueError as nve:
        print(f"Ошибка отрицательного значения: {nve}")
    except TooLargeValueError as tlve:
        print(f"Ошибка слишком большого значения: {tlve}")
    except InvalidTypeError as ite:
        print(f"Ошибка недопустимого типа: {ite}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Проверка значения завершена")

# Шаг 8: Функции, демонстрирующие работу исключений
def example_function_1(value: int) -> int:
    """
    Пример функции 1, демонстрирующей работу исключений.

    Args:
        value (int): Значение для обработки.

    Returns:
        int: Удвоенное значение или None в случае ошибки.
    """
    try:
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        return value * 2
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    finally:
        print("Пример функции 1 завершен")

def example_function_2(value: int) -> float:
    """
    Пример функции 2, демонстрирующей работу исключений.

    Args:
        value (int): Значение для обработки.

    Returns:
        float: Половина значения или None в случае ошибки.
    """
    try:
        if value > 100:
            raise OverflowError("Значение слишком большое")
        return value / 2
    except OverflowError as oe:
        print(f"Ошибка переполнения: {oe}")
    finally:
        print("Пример функции 2 завершен")

def example_function_3(value: any) -> float:
    """
    Пример функции 3, демонстрирующей работу исключений.

    Args:
        value (any): Значение для обработки.

    Returns:
        float: Квадрат значения или None в случае ошибки.
    """
    try:
        if not isinstance(value, (int, float)):
            raise TypeError("Недопустимый тип значения")
        return value ** 2
    except TypeError as te:
        print(f"Ошибка типа: {te}")
    finally:
        print("Пример функции 3 завершен")
