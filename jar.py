class Jar:
    def __init__(self, capacity = 12):
       self.capacity = capacity
       self.size = 0

    def __str__(self):
       return self.size * "\N{Cookie}"


    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not(type(capacity) is int and capacity > 0):
            raise ValueError("wrong capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not (type(size) is int and size >= 0 and size <= self.capacity):
            raise ValueError("wrong size")
        self._size = size
