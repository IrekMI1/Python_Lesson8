import datetime as dt

def log(mode):
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.write(f'{dt.datetime.now().time()}  {mode}\n')
    