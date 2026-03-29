import unittest
from app.player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):
    
    def insert_and_get_test(self):
        
        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"
        hashmap["555"] = "Lee"

        # Use function to put the player name to a variable
        player1 = hashmap["123"]
        player2 = hashmap["555"]


        self.assertEqual(player1.name, "Chrissandra") 
        self.assertEqual(player2.name, "Lee")
    
    def update_player_test(self):

        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"

        # Delete the player with the given UID
        del hashmap["123"]

        with self.assertRaises(KeyError):
            hashmap["123"]   # should not exist anymore