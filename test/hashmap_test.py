import unittest
from app.player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):
    def test_insert_and_get(self):
        
        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"
        hashmap["555"] = "Lee"

        # Use function to put the player name to a variable
        player1 = hashmap["123"]
        player2 = hashmap["555"]

        self.assertEqual(player1.name, "Chrissandra") 
        self.assertEqual(player2.name, "Lee")
    
    def test_update_player(self):

        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"
        hashmap["123"] = "Sandra" # Update the name

        # Delete the player with the given UID
        player = hashmap["123"]
        self.assertEqual(player.name, "Sandra")
    
    def test_delete_player(self):
        hashmap = PlayerHashMap()

        hashmap["123"] = "Chrissandra"
        del hashmap["123"]

        with self.assertRaises(KeyError):
            hashmap["123"]   # should not exist anymore

    def test_len(self):
        hashmap = PlayerHashMap()

        hashmap["1"] = "Z"
        hashmap["2"] = "X"
        hashmap["3"] = "C"

        self.assertEqual(len(hashmap), 3)

    def test_collision_handling(self):
        hashmap = PlayerHashMap()

        # Force a collision by using keys that hash to the same bucket
        hashmap["122"] = "Chrissandra"
        hashmap["212"] = "Lee"

        # Both should still be retrievable
        self.assertEqual(hashmap["122"].name, "Chrissandra")
        self.assertEqual(hashmap["212"].name, "Lee")
        
if __name__ == "__main__":
    unittest.main()

