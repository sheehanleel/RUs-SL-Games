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

