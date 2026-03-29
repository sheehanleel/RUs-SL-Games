from app.node import Node
from app.player import Player

class LinkedList:
    def __init__(self):
        self.head = None #Linked List Object to use in Main , functions from my node for linked list 
    
    def traverse(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.player)) # Appends players to result
            #Into the next node
            current = current.next
        result = " <-> ".join(result) + " <-> None" # joins each players in the result with "<->" before it
        print (result)
        return result
        

    def traverse_backwards(self):
            if self.head is None: #Check if the list is empty
                print("None")
                return "None"

            #Find the last node
            tail = self.head
            result = []
            while tail.next:
                tail = tail.next

            #Traverse Backwards using prev
            current = tail
            while current:
                result.append(str(current.player)) # Appends players to result
                #Into the next node
                current = current.prev
            result = " <-> ".join(result) + " <-> None" # joins each players in the result with "<->" before it
            print (result)    
            return result

    def find_node(self, target_uid):
        current = self.head
        while current:
            if current.player.uid == target_uid:
                return current
            current = current.next
        return None

    def insert_at_beginning(self, player):
        #Adds a new node at the beginning of the list
        new_node = Node(player)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after_node(self, node, player):
        #Adds a new node after a specific node of the list
        if node is None:
            print("Error: The given node is empty")

        new_node = Node(player)
        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node

        node.next = new_node

    def insert_before_node(self, node, player):
        #Adds a new node before a node of the list
        if node is None:
            print("Error: The given node is empty")
            return None
            

        new_node = Node(player)

        new_node.prev = node.prev
        new_node.next = node

        if node.prev is not None:
            node.prev.next = new_node
        
        node.prev = new_node

    def insert_at_end(self, player):
        #Adds a node at the end of the list
        new_node = Node(player)

        #Handle Empty head
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
        return self.head

    def delete_at_beginning(self):
        # Delete the first node from the beginning of the list
        if self.head is None:
            print("The list is empty!") 
            return None
        
        if self.head.next is None:
            self.head = None
            return

        new_head = self.head.next
        new_head.prev = None
        del self.head
        self.head = new_head

    def delete_at_postion(self, target_uid):
        #Delete a node at a position on the list
        if self.head is None:
            return None
        
        current = self.head
        
        while current: #Find the node using UID
            if current.player.uid == target_uid:
                break
            current = current.next
        
        if target_uid < 0: #Check
            print("Invalid UID")
            return self.head
        
        if current == self.head: # Delete if the node is the head
            self.head = current.next
            if self.head:
                self.head.prev = None
            return self.head

        if current.prev: #Links up the list
            current.prev.next = current.next

        if current.next:
            current.next.prev = current.prev
        
        return self.head    

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")

        if self.head.next is None:
            self.head = None
            return 

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        

    def display(self, forward = True):
        if forward == True:
            print("<-**************************->")
            self.traverse()
            print("<-**************************->")
        else:
            print("<-**************************->")
            self.traverse_backwards()
            print("<-**************************->")