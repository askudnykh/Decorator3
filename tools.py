import os
import datetime



def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'\n[{datetime.datetime.now()}] Имя функции: {old_function.__name__}; аргументы: {args} и {kwargs}; возвращаемое значение: {result}')

            return result

        return new_function

    return _logger
