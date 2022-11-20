import view
import logger
import export
import search

def start_program():
    working_mode = view.get_mode()
    while working_mode != 'q':
        logger.log(working_mode)
        if working_mode == 'w':
            data = view.input_data()
            export.export_to_csv(data)
            print('Данные записаны.')
        elif working_mode == 'f':
            search_type = input('Выберите тип поиска: (ф) по фамилии; (и) по имени; (о) по отчеству:\n' )
            if search_type == 'ф':
                view.print_info(search.search_by_surname(input('Искомая фамилия: ')))
            elif search_type == 'и':
                view.print_info(search.search_by_name(input('Искомое имя: ')))
            elif search_type == 'о':
                view.print_info(search.search_by_patronymic(input('Искомое отчество: ')))
        working_mode = view.get_mode()
    
