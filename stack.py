# The stack data structure


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')

        self.data.pop()

    def top(self):
        if self.is_empty():
            print('Stack is empty')

        return self.data[-1]

    def __repr__(self):
        return f'Stack: {self.data}'


S = ArrayStack()
S.push(4)
S.push(5)
S.push(6)
S.push(7)
S.push(8)
S.pop()
print(S)
