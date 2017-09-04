class Stack:
    def __init__(self):
        self.value = 0
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def push(self, value):
        self.value = value
        self._size += 1

    def pop(self):
        self.__emptyCheck()

        self._size -= 1
        return self.value

    def top(self):
        self.__emptyCheck()

        return self.value

    def size(self):
        return self._size

    def __emptyCheck(self):
        if self.isEmpty():
            raise EmptyStackException()
	

class EmptyStackException(Exception):
    pass

