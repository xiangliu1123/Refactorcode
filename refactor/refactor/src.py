# ### Doubly Linked List
#
# The purpose of this assignment is to make you familiar with implementing a data structure in Python in an object oriented way.
# During lectures we implemented a few simple linear data structres: queue, list, deques, stacks. Now we expect you to implement one of these structures yourself.
#
# You are provided with two classes: **Node** and **DoublyLinkedList**. The first one is already implemented (you don't need to modify it), the second one consist only a structure of empty methods defined. Your task is to come up with an implementation of these methods.
#
# _Note_: If a list is doubly linked, each node contains a reference to the _previous_ node in the chain and a reference to the _next_ node.
#
# You are expected to implement every function in DoublyLinkedList. Including the *next()* function, which is used by an iterator object in python. The *map(func)* function applies a function to every element in the list.
# All other functions are available in the PSADS book.

# ## Constructing a Doubly Linked List
#
# The **Node** class implementation is already given:


class Node(object):
    """Doubly linked node which stores an object"""

    def __init__(self, element, next_node=None, previous_node=None):
        # The underscores are to prevent overwriting the variables if inherited and prevents access from outside of scope
        self.__element = element
        self.__next_node = next_node
        self.__previous_node = previous_node

    def get_element(self):
        """Returns the element stored in this node"""
        return self.__element

    def get_previous(self):
        """Returns the previous linked node"""
        return self.__previous_node

    def get_next(self):
        """Returns the next linked node"""
        return self.__next_node

    def set_element(self, element):
        """Sets the element stored in this node"""
        self.__element = element

    def set_previous(self, previous_node):
        """Sets the previous linked node"""
        self.__previous_node = previous_node

    def set_next(self, next_node):
        """Sets the next linked node"""
        self.__next_node = next_node

    def __repr__(self):
        return str((self.__element, self.get_next()))


# The following code snippet is a constructor provided by the **DoublyLinkedList** Python class for the creation of a new doubly linked list. **Extend the snippet below with your implementation of the DoublyLinkedList**.


class DoublyLinkedList(object):
    """Doubly linked node data structure"""

    def __init__(self):
        self.__size = 0
        self.__header = Node('Header')
        self.__trailer = Node('Trailer')
        self.__header.set_next(self.__trailer)
        self.__trailer.set_previous(self.__header)
        self.__current = None

    def __repr__(self):
        return str(self.get_first())

    def __iter__(self):
        self.__current = None
        return self

    def __next__(self):
        """Standard python iterator method"""
        if self.is_empty() or self.__current == self.__trailer:
            raise StopIteration()
        elif self.__current is None:
            self.__current = self.__header
        self.__current = self.__current.get_next()
        if self.__current != self.__trailer:
            return self.__current
        else:
            raise StopIteration()

    def map(self, function):
        """Run function on every element in the list"""
        for node in self:
            if node != self.__trailer and node != self.__header:
                node.set_element(function(node.get_element()))

    def size(self):
        """Returns the number of elements in the list"""
        return self.__size

    def is_empty(self):
        """Returns the number of elements in the list"""
        return self.__size == 0

    def get_first(self):
        """Get the first element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__header.get_next()

    def get_last(self):
        """Get the last element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__trailer.get_previous()

    def get_previous(self, node):
        """Returns the node before the given node"""
        if node == self.__header:
            raise Exception("Cannot get the element before the header of this list")
        else:
            return node.get_previous()

    def get_next(self, node):
        """Returns the node after the given node"""
        if node == self.__trailer:
            raise Exception("Cannot get the element after the trailer of this list")
        else:
            return node.get_next()

    def add_before(self, new, existing):
        """Insert the new before existing"""
        previous_existing = self.get_previous(existing)
        new.set_previous(previous_existing)
        new.set_next(existing)
        existing.set_previous(new)
        previous_existing.set_next(new)
        self.__size += 1

    def add_after(self, new, existing):
        """Insert the new after existing"""
        next_existing = self.get_next(existing)
        new.set_previous(existing)
        new.set_next(next_existing)
        existing.set_next(new)
        next_existing.set_previous(new)
        self.__size += 1

    def add_first(self, new):
        """Insert the node at the head of the list"""
        self.add_after(new, self.__header)

    def add_last(self, new):
        """Insert the node at the tail of the list"""
        self.add_before(new, self.__trailer)

    def remove(self, node):
        """Removes the given node from the list"""
        before = self.get_previous(node)
        after = self.get_next(node)
        before.set_next(after)
        after.set_previous(before)
        node.set_next(None)
        node.set_previous(None)
        self.__size -= 1

