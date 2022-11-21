# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников 
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, 
# содержащие имена, начинающиеся с соответствующей буквы. 
# Как поступить, если потребуется сортировка по ключам?

def thesaurus(*args):
    names_dict = {}
    for name in args:
        if name[0] not in names_dict.keys():
            names_dict[name[0]] = [name]
        else:
            names_dict[name[0]].append(name)
    return names_dict
    

def get_sorted_dict_by_key(some_dict):
    sorted_dict = sorted(some_dict.items(), key=lambda item: item[0])
    return dict(sorted_dict)


names_dict = thesaurus("Иван", "Мария", "Петр", "Илья", "Ирек", "Амир", "Саша")
print(names_dict)
sorted_names_by_key = get_sorted_dict_by_key(names_dict)
print(sorted_names_by_key)
