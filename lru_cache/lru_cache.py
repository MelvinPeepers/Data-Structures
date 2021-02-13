from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    # def __init__(self, limit=10):
    #     self.limit = limit
    #     self.size = 0
    #     self.storage = dict()
    #     self.order = DoublyLinkedList()

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # def get(self, key):
    #     # If key is in storage
    #     if key in self.storage:
    #         # move it to the end
    #         node = self.storage[key]
    #         self.order.move_to_end(node)
    #         # return the value
    #         return node.value[1]

    #     # If not
    #     else:
    #         # return none
    #         return None

    def get(self, key):
        # update items if used
        if key in self.storage:
            # update items if used
            # find the key in order structure, and move to front
            node = self.storage[key]  # node.value = (apple. 'is a fruit')
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None

            # we're reading from a storage
            # it's limited to 10 items

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # remove items that aren't used
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return

        if self.size == self.limit:  # size has reach the limit
            # first value of the tail node
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1

        # add the node to storage
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1

        # key is not in storage, and limit has not been hit
        # add the key to the front of the order structure
        # key is in storage
        # find the key in order, and move to front
        # what if self.size == self.limit?
        # either the head or the tail, that node will be removed
        # delete key from dict

        # def set(self, key, value):
        #     # check and see if the key is in the Dictorary
        #     if key in self.storage:
        #         # If it is
        #         node = self.storage[key]  # grabbing the node
        #         # overwrite the value
        #         node.value = (key, value)  # tuple
        #         # move it to the end
        #         self.order.move_to_end(node)
        #         # nothing else to do, so exit function
        #         return

        #         # check and see if cache is full
        #     if self.size == self.limit:
        #         # remove oldest entry from Dictionary
        #         del self.storage[self.order.head.value[0]]
        #         # AND Linked List
        #         self.order.remove_from_head()
        #         # reduce the size
        #         self.size -= 1

        #     # Add it to the Linked List (key and the value)
        #     self.order.add_to_tail((key, value))
        #     # Add the key and value to the Dictionary
        #     self.storage[key] = self.order.tail
        #     # Increment size
        #     self.size += 1
