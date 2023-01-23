class treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

    def display(self):
        spaces = ' '*self.level()*3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.display()

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


def build_product():
    root = treenode("Elctronic")

    laptop = treenode("laptop")
    laptop.add_children(treenode("dell"))
    laptop.add_children(treenode("mac"))
    laptop.add_children(treenode("asus"))
    laptop.add_children(treenode("hp"))

    mobile = treenode("mobile")
    mobile.add_children(treenode("mi"))
    mobile.add_children(treenode("nothing"))
    mobile.add_children(treenode("1+"))
    mobile.add_children(treenode("vivo"))

    tv = treenode("TV")
    tv.add_children(treenode("lg"))
    tv.add_children(treenode("samsung"))
    tv.add_children(treenode("vu"))
    tv.add_children(treenode("apple"))

    root.add_children(laptop)
    root.add_children(mobile)
    root.add_children(tv)
    # print(mobile.level())
    return root


if __name__ == '__main__':
    root = build_product()
    root.display()
    # print(root.level())
    pass
