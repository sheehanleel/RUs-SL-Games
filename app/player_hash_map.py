from linked_list import LinkedList

class PlayerHashMap:
    size = 10

    def __init__(self):
        self.buckets = []
        self.buckets = [LinkedList() for _ in range(self.size)]