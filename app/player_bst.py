from enum import nonmember

from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root


    @root.setter
    def root(self, value):
        self._root = value

    def insert(self, player):
        # this will insert a new player to the tree and using the player name as the key
        self._root = self._insert_recursive(self._root, player)

    def _insert_recursive(self, node, player):
        # if there is empty spot, create a new node here
        if node is None:
            return PlayerBNode(player)

        # recursive mode, figure out which side it goes to
        if player.name < node.player.name:
            node.left = self._insert_recursive(node.left, player) # Goes left
        elif player.name > node.player.name:
            node.right = self._insert_recursive(node.right, player) # Goes right
        else:
            node.player = player # if the name already exist, then updates the current node's player

        return node

    def search(self, name):
        # This where the entry point is, work will be happening recursively
        return self._search_recursive(self._root, name)

    def _search_recursive(self, node, name):
        if node is None or node.player.name == name: # the search has reached an empty spot, then the name is not on the tree
            return node

        if node.player.name == name: # if name found in the tree, it will be stored in this node
            return node

        if name < node.player.name: # to make it recursive, go left if smaller and go right if its bigger
            return self._search_recursive(node.left, name)
        return self._search_recursive(node.right, name)

    def get_sorted_players(self):
        players = []
        self._in_order_recursive(self._root, players)
        return players

    def _in_order_recursive(self, node, players): # Normal Case, nothing to visit
        if node is None:
            return

        self._in_order_recursive(node.left, players)
        players.append(node.player)
        self._in_order_recursive(node.right, players)

    def balance(self): # Build the tree again as a balances binary tree using the sorted list of players
        sorted_players = self.get_sorted_players()
        self._root = self._build_balanced(sorted_players, 0, len(sorted_players) - 1)

    def _build_balanced(self, players, start, end): # base case when there is no elements left in this section of the list
        if start > end:
            return None

        # pick the middle element and make it as the root of the tree
        middle = (start + end) // 2
        node = PlayerBNode(players[middle])

        # then do the same for left and right, do it recursively
        # 1. Get the middle of the left and make it the left child of the root from step b. (from the assessment)
        node.left = self._build_balanced(players, start, middle - 1)
        # 2. Get the middle of the right and make it the right child of the root from step b. (from the assessment)
        node.right = self._build_balanced(players, middle + 1, end)

        return node



