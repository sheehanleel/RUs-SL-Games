import unittest
from app.player_bst import PlayerBST
from app.player import Player

class TestPlayerBSTSearch(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()

        # Test players - the following names are chosen so the tree branches both side

        self.p_lee = Player(1, "Lee")
        self.p_brian = Player(2, "Brian")
        self.p_temu = Player(3, "Temu")
        self.p_ann = Player(4, "Ann")
        self.p_chris = Player(5, "Chris")
        self.p_sam = Player(6, "Sam")
        self.p_zoe = Player(7, "Zoe")

        # the tree will be:
        #       Lee
        #   Brian Temu
        # Ann Chris Sam Zoe

        for player in [self.p_lee, self.p_brian, self.p_temu,
                       self.p_ann, self.p_chris, self.p_sam, self.p_zoe]:
            self.bst.insert(player)

    def test_search_empty_tree_returns_none(self): # Check if the tree is empty or not
        empty_bst = PlayerBST()
        self.assertIsNone(empty_bst.search("Lee"))

    def test_search_root_returns_root_node(self): # Checks the root node of the tree
        result = self.bst.search("Lee")
        self.assertIs(result, self.bst.root)
        self.assertEqual(result.player, self.p_lee)

    def test_search_finds_node_in_left_subtree(self): # check if there is a node on the left side
        result = self.bst.search("Brian")
        self.assertIsNotNone(result)
        self.assertEqual(result.player, self.p_brian)

    def test_search_finds_node_in_right_subtree(self): # check if there is a node on the right side
        result = self.bst.search("Temu")
        self.assertIsNotNone(result)
        self.assertEqual(result.player, self.p_temu)

    def test_search_finds_deep_nodes_on_both_sides(self): # check the tree two levels down, to see if the recursion happens
        self.assertEqual(self.bst.search("Ann").player, self.p_ann)
        self.assertEqual(self.bst.search("Chris").player, self.p_chris)
        self.assertEqual(self.bst.search("Sam").player, self.p_sam)
        self.assertEqual(self.bst.search("Zoe").player, self.p_zoe)

    def test_search_returns_the_actual_node_in_the_tree(self): # This should be the node itself, not the copy
        result = self.bst.search("Chris")
        self.assertIs(result, self.bst.root.left.right)

    def test_search_missing_name_returns_none(self): # these names that might fall left of, right of, and between existing nodes
        self.assertIsNone(self.bst.search("Aaron"))  # left of everything
        self.assertIsNone(self.bst.search("Zzz"))  # right of everything
        self.assertIsNone(self.bst.search("Carl"))  # between Brian and Chris
        self.assertIsNone(self.bst.search("Mike"))  # between Lee and Sam

    def test_search_is_case_sensitive(self): # make sure that it's case sensitive
        self.assertIsNone(self.bst.search("lee"))

    def test_search_returns_updated_player_after_duplicate_insert(self):
        updated_lee = Player(99, "Lee", score=500) # update a player with a score
        self.bst.insert(updated_lee)

        result = self.bst.search("Lee") # search the player then, check if it's updated while doing a search
        self.assertEqual(result.player, updated_lee)
        self.assertEqual(result.player.score, 500)

if __name__ == "__main__":
    unittest.main()





