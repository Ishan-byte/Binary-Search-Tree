from re import I
from tempfile import TemporaryDirectory
from BSTNode import *

class BST():
    def __init__(self):
        self.root = None

    def insert(self, Currency):
        newNode = BSTNode(Currency)
        head = self.root

        if (head == None):
            self.root = newNode
        else:
            curr = self.root
            while curr != None:
                if curr.data.getValue() > Currency.getValue():
                    if curr.left == None:
                        curr.left = newNode
                        return
                    else:
                        curr = curr.left

                elif curr.data.getValue() < Currency.getValue():
                    if curr.right == None:
                        curr.right = newNode
                        return
                    else:
                        curr = curr.right

            if(curr.data.getValue() > Currency.getValue()):
                curr.left = newNode
            else:
                curr.right = newNode


    def search(self, value):
        head = self.root
        while head is not None:
            if head.data.getValue() == value:
                return True
            else:
                if value < head.data.getValue():
                    if head.left is None:
                        return False
                    head = head.left

                elif value > head.data.getValue():
                    if head.right is None:
                        print(f"{value} was not found in the Binary search tree")
                        return False
                    head = head.right
    
    def minValueNode(self,node):
        curr = node
        while (curr.left is not None):
            curr = curr.left
        return curr


    def delete(self, root, value):

        if root is None:
            return root
        
        if value < root.data.getValue():
            root.left = self.delete(root.left, value)
             
        elif value > root.data.getValue():
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
            
            temp = self.minValueNode(root.right)

            root.data.setValue(temp.data.getValue())

            root.right = self.delete(root.right, temp.data.getValue())
        
        return root


    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data.getValue())
            res = res + self.inorderTraversal(root.right)

        return res
    
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data.getValue())
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
        
        
    def postorderTraversal(self, root):
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data.getValue())
        return res
    
    def BFSTraversal(self, root):
        res = []
        queue = [root]
        while len(queue) > 0:
            curr = queue.pop(0)
            res.append(curr.data.getValue())
            if curr.getLeftChild() is not None:
                queue.append(curr.getLeftChild())
            if curr.getRightChild() is not None:
                queue.append(curr.getRightChild())
        return res


    def printallTraversals(self, root):
        print("Binary Search Tree printed in different sequences: ")
        print("\n")
        print("Breadth-First Traversal")
        print(self.BFSTraversal(root))
        print("\n")
        print("In-order Traversal")
        print(self.inorderTraversal(root))
        print("\n")
        print("Pre-order Traversal")
        print(self.preorderTraversal(root))
        print("\n")
        print("Post-order Traversal")
        print(self.postorderTraversal(root))
    



    def isEmpty(self):
        if self.root == None:
            print("The Binary Search Tree is empty")
            return True
        else:
            print("The Binary Search Tree is not empty")
            return False
    