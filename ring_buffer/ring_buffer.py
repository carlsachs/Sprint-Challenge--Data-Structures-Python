class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        #set a store as a list with nothing in it times whatever is in capacity
        self.store = [None] * capacity
        #set the element equal to 0
        self.old_element = 0
    def append(self, item):
        #set the store with the old element to variable item
        self.store[self.old_element] = item
        #if theres nothing in the old element, it equals 0
        if self.old_element == self.capacity -1:
            self.old_element = 0
        else:
            #else incredment one
            self.old_element += 1
    def get(self):
        # return each item in the self store/old element if the item is not None
        return [item for item in self.store if item is not None]