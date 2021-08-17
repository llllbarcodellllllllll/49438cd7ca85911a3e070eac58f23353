class Stack:
    """ A simple Stack implemntation """

    def pop(self):
        return self.s.pop()

    def push(self, item):
        return self.s.append(item)

    def top(self):
        i = len(self.s)
        return self.s[i-1]

    def size(self):
        return len(self.s)

    def isEmpty(sef):
        return 

    def __init__(self):
        self.s = []

        
