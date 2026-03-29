import unittest
from app.player_hash_map import PlayerHashMap
from app.player import Player

class PlayerHashMapTest(unittest.TestCase):
    
    def insert_and_get_test(self):
        
        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"
        hashmap["555"] = "Lee"

        player1 = hashmap["123"]
        player2 = hashmap["555"]