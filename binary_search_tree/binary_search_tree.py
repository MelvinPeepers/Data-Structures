# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# TreeNode we have a value and a left/right


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # either None or Nodes # BinarySearchTrees (branches)
        # either None or Nodes # BinarySearchTrees (branches)
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        if value < self.value:
            # if smaller, go left. if we reach a left, what should we do?
            if self.left is not None:  # if there's value on the left and it's not None
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

            # if bigger, go right
        else:
            if self.right is not None:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
            # if no node to go to, (either left or right)
            # make the new node at that spot

            # Return True if the tree contains the value
            # False if it does not

    def contains(self, target):
        # compare value to the current node value
        # if smaller, go left
        # if bigger, go right
        # if equal, return True!

        # if smaller, but we can't go left, return false
        # bigger, but we can't go right, return false
        pass

    # # Return the maximum value found in the tree
    # def get_max(self):
    #     pass

    # # Call the function `cb` on the value of each node
    # # You may use a recursive or iterative approach
    # def for_each(self, cb):
    #     pass

    # # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
