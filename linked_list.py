class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """
 
    def __init__(self):
        # An empty list has no head
        self.head = None
 
    def insert_at_front(self, data):
        """Insert a new node at the front of the list. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    def insert_at_end(self, data):
        """(Optional) Insert a new node at the end of the list. O(n)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
 
    def recursive_sum(self):
        """Sum all node data in the list using recursion."""
 
        def _sum(node):
            # Base case: end of list contributes nothing
            if node is None:
                return 0
            # Recursive case: this node's data + sum of the rest
            return node.data + _sum(node.next)
 
        return _sum(self.head)
 
    def recursive_reverse(self):
        """Reverse the list in-place using recursion."""
 
        def _reverse(prev, current):
            # Base case: ran off the end, prev is the new head
            if current is None:
                return prev
            # Recursive case: save next, flip the pointer, move forward
            next_node = current.next
            current.next = prev
            return _reverse(current, next_node)
 
        self.head = _reverse(None, self.head)
 
    def recursive_search(self, target):
        """Return True if target is found, otherwise False, using recursion."""
 
        def _search(node):
            # Base case 1: end of list, not found
            if node is None:
                return False
            # Base case 2: found it
            if node.data == target:
                return True
            # Recursive case: check the rest of the list
            return _search(node.next)
 
        return _search(self.head)
 
    def display(self):
        """Print the contents of the list as 'val -> val -> None'."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values + ["None"]))
