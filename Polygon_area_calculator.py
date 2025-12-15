class Rectangle:
    width: int
    height: int

    def __init__(self, *args):
        if len(args) > 2:
            raise TypeError(f"'Rectangle' object takes 2 positional arguments but {len(args)} were given. ")
        if not any(isinstance(arg, int) for arg in args):
            raise TypeError(f"Arguments must be of type 'int'.")
        if any(args[x] == 0 for x in range(len(args))):
            raise ValueError(f"Argument values must be greater than zero.")
        self.measurements = dict(zip(('width', 'height'), args))
        self.shape = ''

    def set_width(self, w):
        if self.shape == 'Square':
            self.measurements['height'] = w
        self.measurements['width'] = w

    def set_height(self, h):
        if self.shape == 'Square':
            self.measurements['width'] = h
        self.measurements['height'] = h

    def get_area(self):
        a, b = self.measurements.values()
        return a * b

    def get_perimeter(self):
        a, b = self.measurements.values()
        return 2 * a + 2 * b

    def get_diagonal(self):
        a, b = self.measurements.values()
        return (a ** 2 + b ** 2) ** 0.5

    def get_picture(self):
        picture = ''
        a, b = self.measurements.values()
        if a > 50 or b > 50:
            return f"Too big for picture."
        pic = '*' * a
        picture += f"{pic}\n" * b
        return picture

    def get_amount_inside(self, figure):
        a, b = self.measurements.values()
        x, y = figure.measurements.values()
        if x > a or y > b:
            return 0
        elif x < a and y < b:
            h_times = a // x
            w_times = b // y
            return h_times * w_times

    def __str__(self):
        a, b = self.measurements.values()
        if a != b:
            return f"{self.__class__.__name__}(width={a}, height={b})"
        elif a == b:
            return f"{self.__class__.__name__}(side={a})"


class Square(Rectangle):

    def __init__(self, *args):
        super().__init__(*args)
        self.measurements['height'] = self.measurements['width']
        self.shape = self.__class__.__name__

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)


rect = Rectangle(8, 3)
print(rect.get_area())
rect.set_height(10)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))