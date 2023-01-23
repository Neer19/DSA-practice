class bst2:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst2(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst2(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = bst2(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    num_tree = build_tree([17, 4, 1, 20, 5, 66, 89, 123, 333, 456])
    num_tree.delete(20)
    print("After deleting 20 the numbers are= ", num_tree.inorder())

    num_tree = build_tree([17, 4, 1, 2, 5, 66, 9, 123, 333, 456])
    num_tree.delete(9)
    print("After deleting 9 the numbers are= ", num_tree.inorder())

    num_tree = build_tree([17, 4, 1, 2, 5, 66, 89, 123, 333, 456])
    num_tree.delete(17)
    print("After deleting 17 the numbers are= ", num_tree.inorder())
