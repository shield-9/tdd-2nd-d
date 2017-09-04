class Stack:
    def __init__(self):
        self.value = 0

    def isEmpty(self):
        return True

    def push(self, value):
        self.value = value

    def top(self):
        return self.value

    def size(self):
        return 1
