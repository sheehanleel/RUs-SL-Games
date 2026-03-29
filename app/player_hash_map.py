from app.linked_list import LinkedList
from app.player import Player
from app.node import Node

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
    
    def __setitem__(self, key, name):
        # Get the index of the player
        index = self.get_index(key)

        # Get the linked list - player will be stored here
        player_list = self.buckets[index]

        # Check if the player is in the linked list
        existing_node = player_list.find_node(key)

        if existing_node is not None:
            # Updates the player name if it exists
            existing_node.player.name = name
            return
        
        # Create the player if it doesn't exist
        new_player = Player(key, name)

        # Insert the new player at the end of the linked list
        player_list.insert_at_end(new_player)

    def __getitem__(self, key):
        # This function will get the player from the hashmap using UID

        # Get the index of the player
        index = self.get_index(key)

        # Get the linked list - player will be stored here
        player_list = self.buckets[index]

        # Search the list using the function with UID
        node = player_list.find_node(key)

        # Node is found then return the player
        if node is not None:
            return node.player
        
        # If not node not found, handle and raise the error
        raise KeyError(f"Player with UID '{key}' not found.")
        
    def __delitem__(self, key):
        # This function will remove the player from the hashmap

        # Get the index of the player
        index = self.get_index(key)

        # Get the linked list - player will be stored here
        player_list = self.buckets[index]

        # Search the list using the function with UID
        node = player_list.find_node(key)

        if node is None:
            # No player found
            raise KeyError(f"Player with UID '{key}' not found.")
        
        # if its found then it will delete it
        player_list.delete_at_position(key)
        
    def __len__(self):
        # Function to count how many players in the entire thing

        count = 0

        for player_list in self.buckets:

            # Start the count at the start of the list
            current = player_list.head

            # Move through the linked list
            while current is not None:
                count += 1
                current = current.next
        
        return count
    
    def display(self):
        # This will print all of the buckets and the players in each one

        # Go through loop through each bucket index
        for i in range(self.size):
            print(f"Bucket {i}:")

            # Grab the linked list in the bucket
            player_list = self.buckets[i]

            # Traverse at the start of the head of the list
            current = player_list.head

            # if the bucket is empty then
            if current is None:
                print(" (empty)")
                continue

            # Go through the linked list and print each players
            while current is None:
                print(f" {current.player}")
                current = current.next