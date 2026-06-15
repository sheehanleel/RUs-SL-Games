import random

class Player:
    def __init__(self, uid, name, score=0):
        self.uid = uid
        self.name = name
        self.score = score #default to zero

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

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def __str__(self):
        display_player = f"Player: {self.name} - uid: {self.uid}"
        return display_player

    def __repr__(self):
        display_player = f"Player: {self.name} - uid: {self.uid}, score: {self.score}"
        return display_player
    
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

    def __lt__(self, other):
        return self.score < other.score

    # Use the same classmethod in hash_uid
    @classmethod
    def sort_players(cls, players): # Update the variable names to make it clear and descriptive
        if len(players) <= 1:
            return players
        pivot = random.choice(players) # Choosing a random player as a pivot
        left = []
        middle = [] # There is a chance that it will choose the same player
        right = []
        for player in players:
            if player < pivot:
                left.append(player)
            elif player > pivot:
                right.append(player)
            else:
                middle.append(player) # If pivot is same as the player insert in the middle
        return Player.sort_players(left) + middle + Player.sort_players(right)