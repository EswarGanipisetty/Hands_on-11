# TreeNode class represents each node in the Binary Search Tree
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# BinarySearchTree class represents the Binary Search Tree itself
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Pointer to the root of the tree
    
    # Insert a new value into the BST
    def insert(self, value):
        if not self.root:  # If the tree is empty, create a root node
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)  # Otherwise, call the recursive helper function
    
    # Helper function to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.val:  # If the value is less than the current node's value
            if node.left is None:  # If there is no left child, create a new node
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)  # Otherwise, recursively insert into the left subtree
        elif value > node.val:  # If the value is greater than the current node's value
            if node.right is None:  # If there is no right child, create a new node
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)  # Otherwise, recursively insert into the right subtree
    
    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)  # Call the recursive helper function
    
    # Helper function to recursively search for a value in the BST
    def _search_recursive(self, node, value):
        if node is None:  # If the current node is None, the value is not found
            return False
        if node.val == value:  # If the current node's value matches the target value, return True
            return True
        elif value < node.val:  # If the target value is less than the current node's value, search in the left subtree
            return self._search_recursive(node.left, value)
        else:  # If the target value is greater than the current node's value, search in the right subtree
            return self._search_recursive(node.right, value)
    
    # Delete a value from the BST
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)  # Call the recursive helper function
    
    # Helper function to recursively delete a value from the BST
    def _delete_recursive(self, node, value):
        if node is None:  # If the current node is None, the value is not found
            return node
        
        if value < node.val:  # If the value is less than the current node's value, delete from the left subtree
            node.left = self._delete_recursive(node.left, value)
        elif value > node.val:  # If the value is greater than the current node's value, delete from the right subtree
            node.right = self._delete_recursive(node.right, value)
        else:  # If the current node's value matches the target value
            if node.left is None:  # If there is no left child, return the right child
                return node.right
            elif node.right is None:  # If there is no right child, return the left child
                return node.left
            
            # If there are both left and right children, find the successor (minimum value node in the right subtree)
            temp = self._min_value_node(node.right)
            node.val = temp.val  # Replace the current node's value with the successor's value
            node.right = self._delete_recursive(node.right, temp.val)  # Delete the successor from the right subtree
        
        return node
    
    # Helper function to find the minimum value node in a subtree
    def _min_value_node(self, node):
        current = node
        while current.left is not None:  # Traverse left until reaching the leaf node
            current = current.left
        return current

# Helper function to perform an inorder traversal of the BST (left, root, right)
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)  # Traverse the left subtree
        print(node.val, end=" ")  # Print the current node's value
        inorder_traversal(node.right)  # Traverse the right subtree

# Test Binary Search Tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Print the BST after insertion
print("Binary Search Tree:")
inorder_traversal(bst.root)
print("\nSearch 40:", bst.search(40))  # Search for value 40
print("Delete 40")  # Delete value 40
bst.delete(40)
inorder_traversal(bst.root)  # Print the BST after deletion
print("\nSearch 40:", bst.search(40))  # Search for value 40 again to verify deletion
