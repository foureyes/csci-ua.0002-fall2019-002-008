class Fraction:
    """our constructor method
    it initializes new instances based on body of
    __init__ method. within body, self refers to new
    instance

    when called, use only two arguments, as self is 
    passed in implicitly
    """
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __mul__(self, other):
        return self.multiply(other)
    
    def multiply(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
        # self.num = new_num
        # self.den = new_den

    def __str__(self):
        return f'{self.num} / {self.den}'

f1 = Fraction(1, 3)
f2 = Fraction(1, 2)
print(f1 * f2)

"""
from collections import namedtuple
Fraction = namedtuple('Fraction', ['num', 'den'])
f = Fraction(1, 3)
print('type of Fraction', type(Fraction))
print('type of f', type(f))
print(f)
print(f.num, f.den)
"""
