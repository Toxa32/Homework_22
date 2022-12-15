# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
# ----------------------------------------------------------------------

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():

    data = _read(csv)
    sorted_data = _sort(data)
    filtered_data = _filter(sorted_data)

    return filtered_data


def _read(data_str):
    # Чтение данных из строки
    data = []
    for line in data_str.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})

    return data


def _sort(data: list):

    data.sort(key=lambda x: x['age'])

    return data


def _filter(data: list):

    return list(filter(lambda x: x['age'] > 10, data))


if __name__ == '__main__':
    print(get_users_list())
