class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        # if tree is empty
        if self.value is None:
            self.value = BSTNode(value)
        # tree not empty
        else:
            # goes left
            if value < self.value:
                if self.left is not None:
                    self.left.insert(value)
                # left of current node is empty
                else:
                    self.left = BSTNode(value)
            # value is greater than or equal to current node value
            # goes right
            else:
                if self.right is not None:
                    self.right.insert(value)
                    # right of current node is empty
                else:
                    self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return
        else:
            if self.right is None:
                return self.value
            else:
                return self.right.get_max()
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self.value:
            return
        else:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)