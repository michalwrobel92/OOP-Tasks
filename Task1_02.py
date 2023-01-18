class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie({self.x}, {self.y})"

    def describe(self):
        return f"Figura koloru {self.color} o środku w punkcie({self.x}, {self.y})"

    def distance(self, figure):
        return ((abs(self.x-figure.x)**2) + (abs(self.y-figure.y)) ** 2) ** 0.5



s = Shape(1, 2, 'niebieski')
z = Shape(3, 5, "biały")
print(s.describe())
print(s.distance(z))