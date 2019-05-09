"""
create a class called Fraction
f = Fraction(1, 2)
print(f) # 1 / 2
print(f.num) # 1
print(f.den) # 2
"""
class CutenessException(Exception):
    pass

class Cat:
    # anytime you create a method, first param must
    # always be self: refers the actual instance itself
    # (or the instance method was called on)
    # __init__ this specifies the behavior of Cat
    # when used as a function (a constructor... bc
    # it's what's used to create new instances)
    # when you call the constructor Cat(...)
    # it will have number parameters - 1
    # as number of arguments (ignore self)
    def __init__(self, name, cuteness_factor):
        self.name = name
        if cuteness_factor < 1:
            raise CutenessException('not cute enuff')
        self.cuteness_factor = cuteness_factor

    def set_cuteness_factor(self, n):
        if n > 0:
            self.cuteness_factor = n
        """otherwise, don't set the value"""

    def get_name(self):
        return self.name.title()

    def meow(self, how_loudly):
        number_of_os = how_loudly * 'o'
        print(f'{self.name} me{number_of_os}ws')

    def __str__(self):
        """return the intended string version of obj"""
        return f'Cat {self.name}: {self.cuteness_factor}'

c1 = Cat('paw newman', -100) # use type/class name like function
c1.hunger = 0
print(c1, c1.hunger)
#c2 = Cat('Bill Furry', 10)
#c2.meow(1)
#print('type of Cat is ', type(Cat))
#print('type of c', type(c))
#print(c.name, c.cuteness_factor)

"""
x, y = 1, 2
print(x)
print(y)
point = [1, 2]
point = (1, 2)
print(point[0])
point = {'x': 1, 'y': 2}
point['x']
point['y']
"""
