class Node:
    """
    The Node class to represent a node of the list
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

    def __repr__(self):
        return [self.x, self.y]


class LinkedList:
    """
    The LinkedList class to build a list from nodes
    """

    def __init__(self):
        """
        The initialization of the list
        """
        self.head = None

    def __iter__(self):
        """
        Validate and yield every single node
        :return:
        """
        _node = self.head
        while _node is not None:
            yield _node
            _node = _node.next

    def add_first(self, _node):
        """
        Adds the node at the first position of the list
        :param _node: Node
        """
        _node.next = self.head
        self.head = _node


class Snake:
    """
    The Snake class
    """

    def __init__(self):
        """
        Initialization of the snake
        """
        llist = LinkedList()
        llist.add_first(Node(0, 0))
        llist.add_first(Node(1, 0))
        llist.add_first(Node(2, 0))
        self.llist = llist

    def move(self):
        _node = self.llist.head
        while _node is not None:
            _node.x += 1
            _node = _node.next
