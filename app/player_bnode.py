

def __init__(self, player):
    # store the player in this node
    self._player = player

    # pointers for the left and right subtrees, none to start
    self._left = None
    self._right = None

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value