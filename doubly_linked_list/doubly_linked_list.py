"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        # increment the DLL length attribute
        # if DLL is empty
            # set head and tail to the new node instance
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        new_list_node = ListNode(value)
        if self.length == 0:
            self.head = new_list_node
            self.tail = new_list_node        
        else:
            new_list_node.next = self.head
            self.head.prev = new_list_node
            self.head = new_list_node
        
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None
        # return the value
        old_head = self.head
        self.length -= 1
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        # increment the DLL length attribute
        # if DLL is empty
            # set head and tail to the new node instance        
        # if DLL is not empty
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
        new_list_node = ListNode(value)
        if self.length == 0:
            self.head = new_list_node
            self.tail = new_list_node
        else:
            new_list_node.prev = self.tail
            self.tail.next = new_list_node
            self.tail = new_list_node
            
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None
        # return the value
        old_tail = self.tail.value
        self.length -= 1
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
            self.tail = None

        return old_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        temp = node.value
        self.delete(node)
        self.add_to_head(temp)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        temp = node.value
        self.delete(node)
        self.add_to_tail(temp)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if its a head, tail, or something else
        if self.head == self.tail: 
            self.head = None
            self.tail = None
            self.length -= 1
            return 
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        while(current_node.next != None):
            if current_node.value > max_value:        
                max_value = current_node.value
            else:
                current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value
