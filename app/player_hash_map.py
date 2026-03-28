from linked_list import LinkedList
from player import Player

class PlayerHashMap:
    size = 10

    def __init__(self):
        #C reate a list to hold the 10 linkedlist
        self.buckets = []

        # Fill the buckets with linked list
        for i in range(self.size):
            self.buckets.append(LinkedList())
    
    def get_index(self, key):
        # This method will take a player's UID and make it to a bucket index from 0 to 9

        # Use the hash creator from Player Class
        hash_value = Player.hash_uid(key)

        # Shrink the number if it's to big to fit 0 to 9
        index = hash_value % self.size

        return index
        
