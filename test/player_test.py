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

    def test_sort_players(self):
        players = [Player("01", "Alice", score=10), Player("02", "Bob", score=5),
                   Player("03", "Charlie", score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player("02", "Bob", score=5), Player("01", "Alice", score=10),
                                   Player("03", "Charlie", score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)


if __name__ == "__main__":
    unittest.main()