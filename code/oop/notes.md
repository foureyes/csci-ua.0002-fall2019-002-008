object - some value that a name can refer to

you can use value and object interchangeably

* (may consist of data... "hello")
* may have some actions, methods
	* a function called within the context of an object
	* method have access to object's data

type - a category of values
class - kind of like a type... or a blueprint for making objects of a particular type

instantiation - when we make an object of a particular class/type... 

(something is an instance of a class)
class Cat:
	pass

# instantiation
c = Cat()

# c is instance of class Cat

initializing instance w/ data... we have to use a special method: __init__

to define methods in a class, make a function within the body of the class definition

access (read / write) to an object's data (attributes) using the dot

obj.a = 'foo'
print(obj.a)

allows object's user complete access to write / read from attributes

instead of using attributes directly, mediate access to those attributes via methods

obj.a = 'value'
obj.set_a('value')
obj.get_a()

getters and setters




1. last class of new material... object oriented programming... (making our own types to make our own objects)
2. next class is just review




