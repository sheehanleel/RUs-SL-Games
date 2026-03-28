class Node:
    def __init__(self, player):
        #Initiase a new node by using next, prev, and next pointers
        self.player = player
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.player)
