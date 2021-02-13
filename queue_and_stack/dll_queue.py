from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

"""
class Queue:
    self.size = 0
    self.storage = storage_data_structure
"""


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Easier to insert and delete from the middle of a linked list compared to an array.
        self.storage = DoublyLinkedList()

    # FILO
    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
