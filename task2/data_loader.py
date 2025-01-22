def load_ip_addresses(file_path):
    """
    Завантажує IP-адреси з лог-файлу.
    :param file_path: Шлях до файлу.
    :return: Список IP-адрес.
    """
    ip_addresses = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) > 0 and is_valid_ip(parts[0]):
                    ip_addresses.append(parts[0])
    except FileNotFoundError:
        print("Файл не знайдено.")
    return ip_addresses


def is_valid_ip(ip):
    """
    Перевіряє, чи є рядок валідною IP-адресою.
    :param ip: Рядок для перевірки.
    :return: True, якщо це IP-адреса.
    """
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None
