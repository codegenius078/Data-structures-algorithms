# a queue data structure ( Array based )

class Queue:
    def __init__(self, default_size):
        self.default_size = default_size
        self.data = [None] * self.default_size
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty')
        val = self.data[self.front]
        return val

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        dequeued = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return dequeued

    def enqueue(self, value):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = value
        self.size += 1

    def resize(self, capacity):
        old = self.data
        self.data = [None] * capacity
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0

    def __repr__(self):
        return f'Your Queue is: {self.data}'


Q = Queue(5)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.dequeue()
Q.enqueue(6)
print(Q)
print(Q.first())
