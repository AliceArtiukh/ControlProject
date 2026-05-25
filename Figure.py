import random

class Figure:
    SHAPES = [
        [[0, 0], [1, 0], [0, 1], [1, 1]],  # Квадрат (O)
        [[0, -1], [0, 0], [0, 1], [0, 2]], # Паличка (I)
        [[0, 0], [-1, 0], [1, 0], [0, 1]],  # Т-подібна
        [[0, 0], [-1, 0], [0, -1], [1, -1]], # Z-подібна
        [[0, 0], [1, 0], [0, -1], [-1, -1]], # S-подібна
        [[0, 0], [0, -1], [0, 1], [1, 1]],  # L-подібна
        [[0, 0], [0, -1], [0, 1], [-1, 1]]  # Зворотна L
    ]

    COLORS = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'orange']

    def __init__(self):
        self.x = 4
        self.y = 0
        self.shape = random.choice(self.SHAPES)
        self.color = random.choice(self.COLORS)

    def move_down(self):
        self.y += 1

    def move_side(self, dx):
        self.x += dx

    def rotate(self):
        new_shape = []
        for block in self.shape:
            dx, dy = block[0], block[1]
            new_shape.append([-dy, dx])
        self.shape = new_shape
