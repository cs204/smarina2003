class Jar:
    def __init__(self, capacity = 13):
        self.capacity = capacity
        self.size = 0

    def deposit(self, n):
        self.size +=n

    def withdraw(self, n):
        self.size -= n

    def __str__(self):
        return self.size * "\N{Cookie}"

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not (type(capacity)is int and capacity > 0):
            raise ValueError("Wrong capacity")
        self._capacity = capacity

    @property
    def size(self):
        return (self._size)

    @size.setter
    def size(self, size):
        if not (type(size) is int and size >= 0 and size <= self._capacity):
            raise ValueError("Size problems")
        self._size = size

