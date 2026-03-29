#Driver Code
from app.linked_list import LinkedList
from app.player import Player
from app.node import Node
from app.player_hash_map import PlayerHashMap

p1 = Player(1, "Chrissandra")
p2 = Player(2,"Lee" )
p3 = Player(5,"Brian")

new_player = Player(0, "Mikkel")
new_player_1 = Player(3, "Drey")
new_player_2 = Player(4, "Temu")
new_player_3 = Player(6, "Goofy")

ll = LinkedList()

# Build THE list
ll.insert_at_beginning(p1)
ll.insert_at_end(p2)
ll.insert_at_end(p3)

# Try the Operations
# Perform operations
ll.insert_at_beginning(new_player)
ll.insert_after_node(ll.find_node(2), new_player_1)
ll.insert_before_node(ll.find_node(5), new_player_2)
ll.insert_at_end(new_player_3)

ll.delete_at_beginning()
ll.delete_at_position(2)
ll.delete_at_end()


# 
# print("**************************")
# print("Print Fowards:")
# traverse(head)
# print("**************************")

# print("**************************")
# print("Print Backwards:")
# traverse_backwards(head)
# print("**************************")
# 

ll.display(True)

ll.display(False)


hashmap = PlayerHashMap()

hashmap

hashmap.display()