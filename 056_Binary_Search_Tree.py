class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
    
    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def inorder_display(self):
        print("In-order Traversal:")
        def inorder(node):
            if node:
                inorder(node.left)
                print(node.value, end=' ')
                inorder(node.right)
        inorder(self.root)
        print()

    def preorder_display(self):
        print("Pre-order Traversal:")
        def preorder(node):
            if node:
                print(node.value, end=' ')
                preorder(node.left)
                preorder(node.right)
        preorder(self.root)
        print()

    def postorder_display(self):
        print("Post-order Traversal:")
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                print(node.value, end=' ')
        postorder(self.root)
        print()


tree = Binary_Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(2)

tree.inorder_display()
tree.preorder_display()
tree.postorder_display()
