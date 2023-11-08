import model
import text
import view
import datetime 
from datetime import datetime

def search_notice():
    word = view.input_request(text.input_search_word)
    result = model.find_notice(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True

def start():
    while True:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
            view.print_message(text.load_successful)
        if choice == 2:
            model.save_file()
            view.print_message(text.save_successful)
        if choice == 3:
            model.sort_file()
            view.show_book(model.notice_book, text.empty_notice_error)
        if choice == 4:
            new_notice = view.input_notice(text.input_notice)
            now = datetime.now() 
            new_notice.append(now.strftime("%Y-%m-%d %H:%M:%S"))
            model.add_notice(new_notice)
            view.print_message(text.notice_action(new_notice[0], text.operation[0]))
        if choice == 5:
            search_notice()
        if choice == 6:
            if search_notice():
                c_id = int(view.input_request(text.input_edit_notice_id))
                new_notice = view.input_notice(text.input_edit_notice)
                now = datetime.now() 
                new_notice.append(now.strftime("%Y-%m-%d %H:%M:%S"))
                name = model.edit_notice(c_id, new_notice)
                view.print_message(text.notice_action(name, text.operation[1]))
        if choice == 7:
            if search_notice():
                c_id = int(view.input_request(text.input_dell_notice_id))
                name = model.delete_notice(c_id)
                view.print_message(text.notice_action(name, text.operation[2]))

        if choice == 8:
            view.print_message(text.exit_program)
            break
