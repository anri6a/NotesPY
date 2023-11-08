import text


def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)


def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')
    
def show_book(book: dict[int, list[str]], msg: str):
    if book:
        print('\n' + '*' * 67)        
        for i, notice in book.items():
            print(
                f'{i:>3}. {notice[0]:<20} {notice[1]:<20} {notice[2]:<20}')  # i ровняем по правому краю и выделяем ему 3 символа
        print('*' * 67 + '\n')
    else:
        print_message(msg)


def input_notice(msg: str) -> list[str]:
    notice = []
    for input_text in msg:
        notice.append(input(input_text))
    return notice

def input_request(msg: str) -> str:
    return input(msg)