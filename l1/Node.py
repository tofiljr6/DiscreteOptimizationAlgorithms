class Node:
    def __init__(self, id, color, d, pi):
        self.id = id
        self.color = color
        self.pi = pi   # previous node
        self.d = d     # discovery time
        self.f = None  # finishing time
