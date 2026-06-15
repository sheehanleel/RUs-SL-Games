import unittest
from app.player import Player
import random


class TestPlayerFunction(unittest.TestCase):
    def test_uid_property(self):
        player = Player(123, "Bob")
        self.assertEqual(player.uid, 123)
                          
    def test_name_function(self):
        player = Player(123, "Bob")
        self.assertEqual(player.name, "Bob")
        return

    def test_sort_players(self):
        players = [Player("01", "Alice", 10), Player("02", "Bob", 5),
                   Player("03", "Charlie", 15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player("02", "Bob", 5), Player("01", "Alice", 10),
                                   Player("03", "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("01", "Alice", 10)
        bob = Player("01", "Bob", 5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)
        # or, event better
        self.assertGreater(alice, bob)

    def test_sort_players_fast(self):
        players = [Player("01", "Alice", 10), Player("02", "Bob", 5),
                   Player("03", "Charlie", 15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = Player.sort_players(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player("02", "Bob", 5), Player("01", "Alice", 10),
                                   Player("03", "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", random.randint(0, 1000)) for i in range(1000)]

        sorted_players = Player.sort_players(players)

        self.assertListEqual(sorted_players, sorted(players))

if __name__ == "__main__":
    unittest.main()