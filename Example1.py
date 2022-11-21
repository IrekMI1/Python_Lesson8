# Задача 1. Написать функцию num_translate(), переводящую числительные 
# от 0 до 10 c английского на русский язык. Реализовать корректную работу 
# с числительными, начинающимися с заглавной буквы — результат 
# тоже должен быть с заглавной.


def num_translate_adv(num):
    if num.istitle():
        return numbers_dict.get(num.lower()).capitalize()
    else: 
        return numbers_dict.get(num)

numbers_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два', 
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
print(num_translate_adv('nine'))
