from bloom_filter import BloomFilter


def check_password_uniqueness(bloom_filter, new_passwords):
    """
    Перевіряє унікальність паролів за допомогою фільтра Блума.
    :param bloom_filter: Екземпляр класу BloomFilter.
    :param new_passwords: Список нових паролів для перевірки.
    :return: Словник з паролями та їх статусами.
    """
    results = {}
    for password in new_passwords:
        if not password or not isinstance(password, str):
            results[password] = "Некоректний пароль"
            continue
        if bloom_filter.check(password):
            results[password] = "вже використаний"
        else:
            bloom_filter.add(password)
            results[password] = "унікальний"
    return results
