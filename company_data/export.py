def export_to_csv(record):
    with open('personell.csv', 'a', encoding='utf-8') as data:
        data.write(';'.join(record) + '\n')
