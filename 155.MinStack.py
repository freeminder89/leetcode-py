__author__ = 'amow'
class MinStack:

    def __init__(self):
        self.items = []
        self.minv = 0
        self.mint = 0
    # @param x, an integer
    def push(self, x):
        if not self.items:
            self.minv = x
            self.mint = 1
        elif x == self.minv:
            self.mint += 1
        elif x < self.minv:
            self.mint = 1
            self.minv = x
        self.items.append(x)

    def find_min(self):
        if not self.items:
            return
        self.mint = 1
        self.minv = min(self.items)

    # @return nothing
    def pop(self):
        if not self.items:
            return
        item = self.items[-1]
        self.items.pop()
        if item == self.minv:
            self.mint -= 1
            if not self.mint:
                self.find_min()

    # @return an integer
    def top(self):
        return self.items[-1]

    # @return an integer
    def getMin(self):
        if not self.mint:
            return
        return self.minv