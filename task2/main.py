from time import time
from datasketch import HyperLogLog

def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = [line.split('"remote_addr": "')[1].split('"')[0] for line in file if '"remote_addr":' in line]
        return data
    except Exception as e:
        print(f"Помилка завантаження даних: {e}")
        return []

def count_unique_exact(data):
    return len(set(data))

def count_unique_hll(data):
    hll = HyperLogLog(p=4) 
    for ip in data:
        hll.update(ip.strip().encode('utf-8'))
    return len(hll)

if __name__ == "__main__":
    data = load_data('lms-stage-access.log')
    print(f"Загальна кількість зчитаних IP-адрес: {len(data)}")
    print(f"Приклади: {data[:5]}")
    
    # Точний підрахунок
    start_time = time()
    exact_count = count_unique_exact(data)
    exact_time = time() - start_time

    # HyperLogLog підрахунок
    start_time = time()
    hll_count = count_unique_hll(data)
    hll_time = time() - start_time

    # Результати
    import pandas as pd
    results = pd.DataFrame({
        "Метод": ["Точний підрахунок", "HyperLogLog"],
        "Унікальні елементи": [exact_count, hll_count],
        "Час виконання (сек.)": [exact_time, hll_time]
    })
    print("Результати порівняння:")
    print(results)


