PATH = 'notice.txt'
notice_book = {}

def open_file():
    global notice_book, PATH
    with open(PATH, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, notice in enumerate(data, 1):  # начало enumerate  с 1
        notice = notice.strip().split(';')
        notice_book[i] = notice

        
def sort_file():
    global notice_book
    data = []
    for notice in notice_book.values():
        notice = ';'.join(notice)
        data.append(notice)
    notice_phones = list(map(lambda x: x.strip().split(';'), data))
    notice_phones.sort(key = lambda x: x[2])
    for i, notice in enumerate(notice_phones, 1):  # начало enumerate  с 1
        notice_book[i] = notice
     

def save_file():
    global notice_book, PATH
    data = []
    for notice in notice_book.values():
        notice = ';'.join(notice)
        data.append(notice)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='utf-8') as file:
        file.write(data)


def add_notice(new_notice: list[str]):
    global notice_book
    c_id = max(notice_book) + 1
    notice_book[c_id] = new_notice


def find_notice(word: str) -> dict[int, list[str]]:
    global notice_book
    result = {}
    for c_id, notice in notice_book.items():
        for field in notice:
            if word.lower() in field.lower():
                result[c_id] = notice
                break
    return result


def edit_notice(c_id: int, new_notice: list[str]):
    global notice_book
    current_notice = notice_book.get(c_id)
    notice = []
    for i in range(len(new_notice)):
        if new_notice[i]:
            notice.append(new_notice[i])
        else:
            notice.append(current_notice[i])
    notice_book[c_id] = notice
    return notice[0]

def delete_notice(c_id: int) -> str:
    global notice_book
    return notice_book.pop(c_id)[0]
