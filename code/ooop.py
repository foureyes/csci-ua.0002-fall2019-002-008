"""
when you use your class name to construct new objects
...the behavior of that function is defined by a method
called init which you create inside the class itself
"""
class CutenessException(Exception):
    pass


class Cat:
    """initialize object / instance
    1. first argument must always be self
       self refers to the new instance to be created
    """
    """how many args to pass in? 
    number of parameters - 1 
    """
    def __init__(self, name, cuteness_factor):
        """2. add attributes to our instance"""
        self.name = name
        if cuteness_factor < 1:
            raise CutenessException('not cute enuff')
        self.cuteness_factor = cuteness_factor

    def set_cuteness_factor(self, n):
        if n > 0:
            self.cuteness_factor = n
        """otherwise, do not change"""
            

    def get_name(self):
        return self.name.title()

    """ self refers to instance""" 
    def meow(self, how_loudly): 
        number_of_os = how_loudly * 'o'
        print(f'{self.name} me{number_of_os}ws')

    def __str__(self):
        return(f'{self.name}, {self.cuteness_factor}')

"""even though init has 3 parameters, only pass in everything other than self"""        

try:
    c1 = Cat('paw newman', -100)
    print(c1)
except CutenessException:
    print('not cute enough')
#c1.cuteness_factor = -1000
"""
print(c1.name, c1.cuteness_factor)
c2 = Cat('bill furry', 7)
print(c2.name, c2.cuteness_factor)
"""




"""
store data for a two dimensional point
"""
"""
point = "1, 2"
x, y = 1, 2
point = (1, 2)
point = [1, 2]
point[0] # x
point[1] # x
point = {'x': 1, 'y': 2}
point['x']
point['y']
"""
