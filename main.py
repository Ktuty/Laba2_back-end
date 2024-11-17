from functions import (
    divide, get_list_element, safe_divide, safe_get_list_element,
    process_number, read_file, calculate_square_root, validate_age,
    check_value, example_function_1, example_function_2, example_function_3
)

def run_all_functions() -> None:
    """
    Функция, последовательно вызывающая все созданные функции.
    """
    try:
        # Шаг 1
        print(divide(10, 2))
        print(get_list_element([1, 2, 3], 1))

        # Шаг 2
        print(safe_divide(10, 0))

        # Шаг 3
        print(safe_get_list_element([1, 2, 3], 5))

        # Шаг 4
        print(process_number(101))
        print(read_file("nonexistent_file.txt"))
        print(calculate_square_root(-1))

        # Шаг 5
        print(validate_age(121))

        # Шаг 7
        print(check_value(101))

        # Шаг 8
        print(example_function_1(-1))
        print(example_function_2(101))
        print(example_function_3("string"))

    except Exception as e:
        print(f"Необработанное исключение: {e}")

if __name__ == "__main__":
    run_all_functions()
