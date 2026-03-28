import unittest
from app.linked_list import LinkedList
from app.player import Player

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        #Add mock items
        self.p1 = Player(1, "Chrissandra")
        self.p2 = Player(2,"Lee")
        self.p3 = Player(5, "CJ")

        #Insert new players
        self.new_player = Player(0, "Mikkel")
        self.new_player_1 = Player(3, "Drey")
        self.new_player_2 = Player(4, "Temu")
        self.new_player_3 = Player(6, "Goofy")

        #Initialize link list
        self.ll = LinkedList()
        self.ll.insert_at_beginning(self.p1)
        self.ll.insert_at_end(self.p2)
        self.ll.insert_at_end(self.p3)
        
    def test_insert_at_beginning_forwards(self):
        self.head = self.ll.insert_at_beginning(self.new_player)
        output = self.ll.traverse()
        expected = "Player: Mikkel - uid: 0 <-> Player: Chrissandra - uid: 1 <-> Player: Lee - uid: 2 <-> Player: CJ - uid: 5 <-> None"
        self.assertEqual(output, expected)

    def test_insert_at_beginning_backwards(self):
        self.head = self.ll.insert_at_beginning(self.new_player)
        output = self.ll.traverse_backwards()
        expected = "Player: CJ - uid: 5 <-> Player: Lee - uid: 2 <-> Player: Chrissandra - uid: 1 <-> Player: Mikkel - uid: 0 <-> None"
        self.assertEqual(output, expected)
    
    def test_insert_after_node_forwards(self):
        node = self.ll.find_node(2)
        self.ll.insert_after_node(node, self.new_player_1)
        output = self.ll.traverse()
        expected = "Player: Chrissandra - uid: 1 <-> Player: Lee - uid: 2 <-> Player: Drey - uid: 3 <-> Player: CJ - uid: 5 <-> None"
        self.assertEqual(output, expected)

    def test_insert_after_node_backwards(self):
        node = self.ll.find_node(2)
        self.ll.insert_after_node(node, self.new_player_1)
        output = self.ll.traverse_backwards()
        expected = "Player: CJ - uid: 5 <-> Player: Drey - uid: 3 <-> Player: Lee - uid: 2 <-> Player: Chrissandra - uid: 1 <-> None"
        self.assertEqual(output, expected)
    
    def test_insert_before_node_forwards(self):
        node = self.ll.find_node(5)
        self.ll.insert_before_node(node, self.new_player_2)
        output = self.ll.traverse()
        expected = "Player: Chrissandra - uid: 1 <-> Player: Lee - uid: 2 <-> Player: Temu - uid: 4 <-> Player: CJ - uid: 5 <-> None"
        self.assertEqual(output, expected)
    
    def test_insert_before_node_backwards(self):
        node = self.ll.find_node(5)
        self.ll.insert_before_node(node, self.new_player_2)
        output = self.ll.traverse_backwards()
        expected = "Player: CJ - uid: 5 <-> Player: Temu - uid: 4 <-> Player: Lee - uid: 2 <-> Player: Chrissandra - uid: 1 <-> None"
        self.assertEqual(output, expected)
    
    def test_insert_at_end_forwards(self):
        self.ll.insert_at_end(self.new_player_3)
        output = self.ll.traverse()
        expected = "Player: Chrissandra - uid: 1 <-> Player: Lee - uid: 2 <-> Player: CJ - uid: 5 <-> Player: Goofy - uid: 6 <-> None"
        self.assertEqual(output, expected)

    def test_insert_at_end_backwards(self):
        self.ll.insert_at_end(self.new_player_3)
        output = self.ll.traverse_backwards()
        expected = "Player: Goofy - uid: 6 <-> Player: CJ - uid: 5 <-> Player: Lee - uid: 2 <-> Player: Chrissandra - uid: 1 <-> None"
        self.assertEqual(output, expected)

    def test_delete_at_beginning_forwards(self):
        self.head = self.ll.delete_at_beginning()
        output = self.ll.traverse()
        expected = "Player: Lee - uid: 2 <-> Player: CJ - uid: 5 <-> None"
        self.assertEqual(output, expected)
    
    def test_delete_at_beginning_backwards(self):
        self.head = self.ll.delete_at_beginning()
        output = self.ll.traverse_backwards()
        expected = "Player: CJ - uid: 5 <-> Player: Lee - uid: 2 <-> None"
        self.assertEqual(output, expected)
    
    def test_delete_at_postion_forwards(self):
        self.ll.delete_at_postion(2)
        output = self.ll.traverse()
        expected = "Player: Chrissandra - uid: 1 <-> Player: CJ - uid: 5 <-> None"
        self.assertEqual(output, expected)
    
    def test_delete_at_postion_backwards(self):
        self.ll.delete_at_postion(2)
        output = self.ll.traverse_backwards()
        expected = "Player: CJ - uid: 5 <-> Player: Chrissandra - uid: 1 <-> None"
        self.assertEqual(output, expected)
    
    def test_delete_at_end_forwards(self):
        self.head = self.ll.delete_at_end()
        output = self.ll.traverse()
        expected = "Player: Chrissandra - uid: 1 <-> Player: Lee - uid: 2 <-> None"
        self.assertEqual(output, expected)
    
    def test_delete_at_end_backwards(self):
        self.head = self.ll.delete_at_end()
        output = self.ll.traverse_backwards()
        expected = "Player: Lee - uid: 2 <-> Player: Chrissandra - uid: 1 <-> None"
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()