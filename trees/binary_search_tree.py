class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        return self
                    current = current.left

                elif data > current.data:
                    if current.right is None:
                        current.right = node
                        return self
                    current = current.right

    def lookup(self, data):
        if self.root is None:
            return False
        current = self.root
        while True:
            if data == current.data:
                return True
            elif data < current.data:
                if current.left is None:
                    return False
                current = current.left
            elif data > current.data:
                if current.right is None:
                    return False
                current = current.right

    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

    def printt(self, curr_node):
        if curr_node is not None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
print(bst.lookup(6))
print(bst.lookup(99))
bst.print_tree()
