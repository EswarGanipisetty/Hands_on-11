class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        
        return x
    
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        
        if value < root.val:
            root.left = self.insert(root.left, value)
        elif value > root.val:
            root.right = self.insert(root.right, value)
        else:
            return root
        
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        
        balance = self._get_balance(root)
        
        if balance > 1 and value < root.left.val:
            return self._rotate_right(root)
        
        if balance < -1 and value > root.right.val:
            return self._rotate_left(root)
        
        if balance > 1 and value > root.left.val:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        
        if balance < -1 and value < root.right.val:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        
        return root
    
    def delete(self, root, value):
        if not root:
            return root
        
        if value < root.val:
            root.left = self.delete(root.left, value)
        elif value > root.val:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self._get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        
        if root is None:
            return root
        
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)
        
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._rotate_right(root)
        
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._rotate_left(root)
        
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        
        return root
    
    def _get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, root, value):
        if not root or root.val == value:
            return root
        
        if root.val < value:
            return self.search(root.right, value)
        
        return self.search(root.left, value)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Test AVL Tree
avl = AVLTree()
avl.root = avl.insert(avl.root, 10)
avl.root = avl.insert(avl.root, 20)
avl.root = avl.insert(avl.root, 30)
avl.root = avl.insert(avl.root, 40)
avl.root = avl.insert(avl.root, 50)
avl.root = avl.insert(avl.root, 25)

print("AVL Tree after insertion:")
inorder_traversal(avl.root)
print()

avl.root = avl.delete(avl.root, 30)
print("AVL Tree after deletion of 30:")
inorder_traversal(avl.root)
print()

print("Search for value 20:", avl.search(avl.root, 20))
print("Search for value 30:", avl.search(avl.root, 30))
