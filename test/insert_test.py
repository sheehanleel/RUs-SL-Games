import unittest
from app.player_bst import PlayerBST
from app.player import Player

class TestPlayerBSTInsert(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()

        # Example players for the test
        self.p_lee = Player(1, 'Lee')
        self.p_brian = Player(2, 'Brian') # < Lee -> goes to the left
        self.p_temu = Player(3, 'Temu')   # > Lee -> goes to the right
        self.p_ann = Player(4, 'Ann')    # < Lee, < Brian -> goes to the left -> then left
        self.p_chris = Player(5, 'Chris') # < Lee, > Brian -> goes to the left -> then right
        self.p_sam = Player(6, 'Sam') # > Lee, < Temu -> goes to the right -> then left
        self.p_zoe = Player(7, 'Zoe') # > Lee, > Temu -> goes to the right -> then right

    def test_root_is_none_when_empty(self):
        # a new tree should have nothing in it
        self.assertEqual(self.bst.root, None)

    def test_insert_first_player_becomes_root(self):
        self.bst.insert(self.p_lee)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player, self.p_lee)

    def test_insert_smaller_name_goes_left(self):
        self.bst.insert(self.p_lee)
        self.bst.insert(self.p_brian)

        self.assertEqual(self.bst.root.left.player, self.p_brian)
        self.assertIsNone(self.bst.root.right)

    def test_insert_larger_name_goes_right(self):
        self.bst.insert(self.p_lee)
        self.bst.insert(self.p_temu)

        self.assertEqual(self.bst.root.right.player, self.p_temu)
        self.assertIsNone(self.bst.root.left)

    def test_insert_builds_correct_tree_shape(self):
        # insert in an order that make sure that it's branching in both sides
        # this is at more than one more level, to show that its recursive
        for player in [self.p_lee, self.p_brian, self.p_temu,
                       self.p_ann, self.p_chris, self.p_sam, self.p_zoe]:

            self.bst.insert(player)

        root = self.bst.root
        self.assertEqual(root.player, self.p_lee)

        # left subtree which are smaller than Lee
        self.assertEqual(root.left.player, self.p_brian)
        self.assertEqual(root.left.left.player, self.p_ann)
        self.assertEqual(root.left.right.player, self.p_chris)

        # right subtree which are bigger than Lee
        self.assertEqual(root.right.player, self.p_temu)
        self.assertEqual(root.right.left.player, self.p_sam)
        self.assertEqual(root.right.right.player, self.p_zoe)

    def test_in_order_traversal_is_sorted_by_name(self):
        # Rule 1 and Rule 2 combined: in order traversal of a valid BST
        # This should come out in sorted key order
        for player in [self.p_lee, self.p_brian, self.p_temu,
                       self.p_ann, self.p_chris, self.p_sam, self.p_zoe]:
            self.bst.insert(player)

        names = self._in_order_names(self.bst.root)
        self.assertEqual(names, sorted(names))
        self.assertEqual(
            names,
            ["Ann", "Brian", "Chris", "Lee", "Sam", "Temu", "Zoe"]
        )

    def test_insert_duplicate_name_does_not_create_new_node(self):
        # Rule 4 - there should be no duplicate keys
        # This should update the existing node, not add a node
        self.bst.insert(self.p_lee)
        self.bst.insert(self.p_brian)
        self.bst.insert(self.p_temu)

        updated_lee = Player(99, "Lee", score=500)
        self.bst.insert(updated_lee)

        # Still only 3 nodes in the tree
        self.assertEqual(self._count_nodes(self.bst.root), 3)

        # Check if the root's player is updated
        self.assertEqual(self.bst.root.player, updated_lee)
        self.assertEqual(self.bst.root.player.uid, 99)
        self.assertEqual(self.bst.root.player.score, 500)

        # Check if the rest of the tree is untouched
        self.assertEqual(self.bst.root.left.player, self.p_brian)
        self.assertEqual(self.bst.root.right.player, self.p_temu)

    def test_insert_duplicate_deeper_in_tree_updates_correct_node(self):
        for player in [self.p_lee, self.p_brian, self.p_temu, self.p_ann]:
            self.bst.insert(player)

        updated_ann = Player(100, "Ann", score=42)
        self.bst.insert(updated_ann)

        self.assertEqual(self._count_nodes(self.bst.root), 4)
        self.assertEqual(self.bst.root.left.left.player, updated_ann)
        self.assertEqual(self.bst.root.left.left.player.score, 42)


# Functions, methods ---- helpers

    def _in_order_names(self, node):
        # This gives a sorted order for a valid BST
        if node is None:
            return []
        return (self._in_order_names(node.left)
                + [node.player.name]
                + self._in_order_names(node.right))

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

if __name__ == "__main__":
    unittest.main()



