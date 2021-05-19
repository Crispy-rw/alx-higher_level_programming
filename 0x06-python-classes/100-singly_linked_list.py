#!/usr/bin/python3
"""Contains the definition of class Node that of a singly linked list"""


class Node:
    """Definition of class Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes an instance of class Node.

        Ensures data is an integer and raises a TypeError if it's not.
        """

        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.data = data
        if isinstance(next_node, Node) or next_node is None:
            self.next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Retrieves the value of the data attribute.

        Setter method ensures data is an integer and raises a TypeError if not.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of the next_node attribute

        Setter method ensures value is of type Node, else raises a TypeError.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Definition of class SinglyLinkedList."""

    def __init__(self):
        """Initializes an instance of class SinglyLinkedList"""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing)

        Args:
            value (int): Value to initialize new node with
        """

        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Depict the linked list as a string"""
        temp = self.__head
        ss = []
        while temp is not None:
            ss.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(ss))
