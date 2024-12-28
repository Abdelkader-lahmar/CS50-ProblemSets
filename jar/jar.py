class Jar:
    def __init__(self, capacity=12):
        if type(capacity) != int or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, number):
        if type(number) != int or number < 0 or number > self.capacity:
            raise ValueError
        self._size = number
