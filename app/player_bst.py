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

