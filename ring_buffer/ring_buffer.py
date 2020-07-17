class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None] * capacity
        self.old_element = 0
    def append(self, item):
        self.store[self.old_element] = item
        if self.old_element == self.capacity -1:
            self.old_element = 0
        else:
            self.old_element += 1
    def get(self):
        return [item for item in self.store if item is not None]