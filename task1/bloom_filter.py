import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size, num_hashes):
        """
        Ініціалізуємо фільтр Блума.
        :param size: Розмір бітового масиву.
        :param num_hashes: Кількість хеш-функцій.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        """
        Додає елемент до фільтра.
        :param item: Елемент для додавання.
        """
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def check(self, item):
        """
        Перевіряє, чи є елемент у фільтрі.
        :param item: Елемент для перевірки.
        :return: True, якщо елемент може бути у фільтрі, інакше False.
        """
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True
