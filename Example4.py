# Задача 4*. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» 
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме 
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. 
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    names_dict = {} 
    for name in args:
        name_list = name.split()
        if name_list[1][0] not in names_dict.keys():
            names_dict[name_list[1][0]] = {name_list[0][0]: [name]}
        else:
            if name_list[0][0] not in names_dict[name_list[1][0]].keys():
                names_dict[name_list[1][0]][name_list[0][0]] = [name]
            else:
                names_dict[name_list[1][0]][name_list[0][0]].append(name)
    return names_dict


def sort_by_key(some_dict):
    sorted_dict = sorted(some_dict.items(), key=lambda item: item[0])
    return dict(sorted_dict)


names_dict = thesaurus_adv(
    "Иван Сергеев",
    "Инна Серова", 
    "Петр Алексеев",
    "Илья Иванов",
    "Анна Савельева"
)
print(names_dict)
print(sort_by_key(names_dict))
