from stack import Stack
from queue import Queue
from singly_linked_list import LinkedList
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            return False
        else:
            if self.right:
                return self.right.contains(target)
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self is None:
            return

        if self.left is not None:
            self.left.in_order_print(node)

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(node)

    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
    # start by placing the root in the queue​
    # need a while loop to iterate
    # what are we checking in the while statement?
    # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item​
    # place current item's left node in queue if not None
    # place current item's right node in queue if not None

        q = Queue()
        q.enqueue(node)
    
        while len(q) > 0:
            node = q.dequeue()
            print(node.value)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # initialize an empty stack
        # push the root node onto the stack​
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
            # pop top item off the stack
            # print that item's value​
            # if there is a right subtree
                # push right item onto the stack                
            # if there is a left subtree
                # push left item onto the stack
        
        s = Stack()
        s.push(node)
        
        while len(s) > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
