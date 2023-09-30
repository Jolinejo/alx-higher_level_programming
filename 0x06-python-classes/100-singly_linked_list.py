#!/usr/bin/python3
"""linked list"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """constructor"""
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for node"""
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """linked list class"""
    def __init__(self):
        """constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """inserting"""
        if self.__head is None:
            self.__head = Node(value)
            return
        if self.__head.data > value:
            self.__head = Node(value, self.__head)
            return
        trav = self.__head
        temp = None
        while trav is not None:
            if trav.data > value:
                temp.next_node = Node(value, trav)
                return
            temp = trav
            trav = trav.next_node
        temp.next_node = Node(value)

    def __str__(self):
        """printing"""
        trav = self.__head
        s = ""
        while trav is not None:
            s += str(trav.data) + "\n"
            trav = trav.next_node
        return s[:-1]
