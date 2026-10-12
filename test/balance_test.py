import unittest
from app.player_bst import PlayerBST
from app.player import Player

class TestPlayerBSTBalance(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()

        # Add names in a sorted alphabetical order, then this makes it the worst case for a list
        # A tree but it's just a linked list

        self.names = ["Ann", "Brian", "Chris", "Lee", "Sam", "Temu", "Zoe"]
        for i, name in enumerate(self.names):
            self.bst.insert(Player(i, name))

    def test_get_sorted_players_returns_names_in_order(self): # Check if the return names are in order
        players = self.bst.get_sorted_players()
        self.assertEqual([p.name for p in players], self.names)

    def test_get_sorted_players_empty_tree(self): # Check the empty tree
        self.assertEqual(PlayerBST().get_sorted_players(), [])

    def test_unbalanced_tree_is_tall_before_balancing(self): # check the setup if its unbalanced
        self.assertEqual(self._height(self.bst.root), 7)

    def test_balance_makes_middle_player_the_root(self): # Check if the middle becomes the root
        self.bst.balance()
        self.assertEqual(self.bst.root.player.name, "Lee")

    def test_balance_builds_expected_shape(self): # Check if it rebuilds the tree on the expected shape
        self.bst.balance()
        root = self.bst.root

        self.assertEqual(root.left.player.name, "Brian")
        self.assertEqual(root.left.left.player.name, "Ann")
        self.assertEqual(root.left.right.player.name, "Chris")

        self.assertEqual(root.right.player.name, "Temu")
        self.assertEqual(root.right.left.player.name, "Sam")
        self.assertEqual(root.right.right.player.name, "Zoe")

    def test_balance_reduces_height(self): # check if its balance and that nodes can fit in a tree of height of 3
        self.bst.balance()
        self.assertEqual(self._height(self.bst.root), 3)

    def test_balance_keeps_all_players(self): # CHeck if the list still have 7 names
        self.bst.balance()
        players = self.bst.get_sorted_players()
        self.assertEqual([p.name for p in players], self.names)

    def test_balanced_tree_is_still_a_valid_bst(self): # Check if its a valid binary search tree
        self.bst.balance()
        names = self._in_order_names(self.bst.root)
        self.assertEqual(names, sorted(names))

    def test_search_still_works_after_balancing(self): # Test the search function after balancing
        self.bst.balance()
        for name in self.names:
            self.assertEqual(self.bst.search(name).player.name, name)
        self.assertIsNone(self.bst.search("Nobody"))

    def test_balance_even_number_of_players(self): #Check if the tree comes out correct, with 3 height and all of the names in the right order
        bst = PlayerBST()
        for i, name in enumerate(["Ann", "Brian", "Chris", "Lee"]):
            bst.insert(Player(i, name))

        bst.balance()

        self.assertEqual(self._height(bst.root), 3)
        self.assertEqual(self._in_order_names(bst.root),
                         ["Ann", "Brian", "Chris", "Lee"])

    def test_balance_empty_tree(self): # this should leave the root as none because its empty
        bst = PlayerBST()
        bst.balance()
        self.assertIsNone(bst.root)

    def test_balance_single_player(self): # if there is only one player it becomes the root of the tree
        bst = PlayerBST()
        bst.insert(Player(1, "Ann"))
        bst.balance()
        self.assertEqual(bst.root.player.name, "Ann")
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)


    # Helpers for this test file

    def _height(self, node): # Measures how tall is the tree of bst
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _in_order_names(self, node): # get names left and right nodes
        if node is None:
            return []
        return (self._in_order_names(node.left)
                + [node.player.name]
                + self._in_order_names(node.right))


if "__main__" == __name__:
    unittest.main()




