class bst:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst(data)
        else:
            # add in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst(data)

    # inorder

    def inorder(self):
        elements = []

        # visit left
        if self.left:
            elements += self.left.inorder()

        # visit base
        elements.append(self.data)

        # visit right
        if self.right:
            elements += self.right.inorder()

        return elements

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


def build_tree(elements):
    root = bst(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':

    num = [17, 4, 1, 2, 5, 66, 89, 123, 333, 456]
    num_tree = build_tree(num)
    # print(num_tree.inorder())
    print(num_tree.search(456))