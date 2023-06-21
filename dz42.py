# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение
# переданного аргумента,
# а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def args_analyser(**kwargs):
    result = {}
    for key, value in kwargs.items(): 
        if not isinstance(value, (int, float, str, tuple, frozenset, bool)):
            hashable_key = str(value)
        else:
            hashable_key = value
        result[hashable_key] = key
    return result

# если я правильно поняла задание ...
# шиворот навывоворот 
print(args_analyser(x=2, y=67.2, txt="baby", lst=[1, 2, 3], flag=True, dict={'India': 13, 'Brazil': 20,  'China': 138}))
