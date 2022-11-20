def search_by_surname(surname):
    with open('personell.csv', 'r', encoding='utf-8') as db:
        for row in db:
            person = row.split(';')
            if person[0] == surname:
                return person
        return 'not found'


def search_by_name(name):
    with open('personell.csv', 'r', encoding='utf-8') as db:
        for row in db:
            person = row.split(';')
            if person[1] == name:
                return person
        return 'not found'


def search_by_patronymic(patronymic):
    with open('personell.csv', 'r', encoding='utf-8') as db:
        for row in db:
            person = row.split(';')
            if person[2] == patronymic:
                return person
        return 'not found'
