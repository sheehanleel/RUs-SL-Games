class Player:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    @property
    def uid(self):
        return self._uid
    
    @uid.setter
    def uid(self, value):
        self._uid = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        dispay_player = f"Player: {self.name} - uid: {self.uid}"
        return dispay_player
    
    @classmethod
    def hash_uid(cls, key: str) -> int: #Take the UID of the player and create a HASH
        #cls is like self
        #Gets the key if its a string it will convert it to int

        hash_value = 0
        prime = 31 # Use a prime number to create the hash

        for char in key:
            hash_value = hash_value * prime * ord(char)

        return hash_value

    def __hash__(self):
        return Player.hash_uid(self.uid)
    
    def __eq__(self, other):
        return self.uid == other.uid