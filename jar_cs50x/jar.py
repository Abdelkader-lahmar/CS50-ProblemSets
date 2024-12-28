class Jar:
    """ testing __doc__"""
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError
        self._size += n
        ...

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n
        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return str(self._size)
        ...


def main():
    jar = Jar(10)
    print(str(jar.capacity))
    print(str(jar))
    jar.deposit(2)
    print(str(jar))
    jar.withdraw(1)
    print(str(jar))

main()
