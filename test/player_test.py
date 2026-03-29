import unittest
from app.player import Player
#from app import Node, insert_at_beginning, traverse, traverse_backwards, insert_after_node, find_node, insert_before_node, insert_at_end, delete_at_beginning, delete_at_postion, delete_at_end

class TestPlayerFunction(unittest.TestCase):
    def test_uid_property(self):
        player = Player(123, "Bob")
        self.assertEqual(player.uid, 123)
                          
    def test_name_function(self):
        player = Player(123, "Bob")
        self.assertEqual(player.name, "Bob")
        return
    
if __name__ == "__main__":
    unittest.main()