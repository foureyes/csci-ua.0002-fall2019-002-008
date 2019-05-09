class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __mul__(self, other):
        return self.multiply(other)

    def multiply(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
        # return f'{new_num}  {new_den}'

    def __str__(self):
        return f'{self.num} / {self.den}'

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1.multiply(f2))







