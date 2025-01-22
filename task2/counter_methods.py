from collections import Counter
import hyperloglog
import time


def count_unique_ips_exact(ip_addresses):
    """
    Точний підрахунок унікальних IP-адрес.
    :param ip_addresses: Список IP-адрес.
    :return: Кількість унікальних IP-адрес.
    """
    return len(set(ip_addresses))


def count_unique_ips_hyperloglog(ip_addresses):
    """
    Підрахунок унікальних IP-адрес за допомогою HyperLogLog.
    :param ip_addresses: Список IP-адрес.
    :return: Кількість унікальних IP-адрес.
    """
    hll = hyperloglog.HyperLogLog(0.01)  # Параметр похибки 1%
    for ip in ip_addresses:
        hll.add(ip)
    return len(hll)


def measure_time(func, *args):
    """
    Вимірює час виконання функції.
    :param func: Функція для виконання.
    :param args: Аргументи функції.
    :return: Результат функції та час виконання.
    """
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time
