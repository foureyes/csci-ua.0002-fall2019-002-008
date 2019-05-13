exam material
=====

* all topics up through class 27 (object oriented programming)
* enumerate is a function that i give documentation on in the exam
* won't be on exam:
	* recursion
	* list comprehensions


topics
=====
* iterating w/ indexes
* exception handling
* turtle
* file io
* dictionaries
	* looping over them
* oop




dictionaries
=====
1. mutable
2. they're a compound data type: composed of different values
3. key and value pairs
	* key must be immutable
	* value can be any value

read from dict
-----
1. key into dict... d[k]
	* if k doesn't exist, KeyError
2. .get ... will retrieve value at key... d.get(k)
	* if k doesn't exist, you get 2nd argument
	* if 2nd argument isn't passed, then it's None
	* d = {}... d.get('foo', 'default') # default is returned

dealing with KeyError
-----
* try... except KeyError
* check if key exists in dictionary
	* if k in d:

writing to a dict
-----
* new key value pair
	* key into dict w/ key that doesn't exist AND assign
	* d[new_k] = new_v
* update value at key
	* d[old_k] = new_v

methods
-----
get(k, default_v_if_k_not_exist)
items() # list like object with k, v tuples [(k1, v1), (k2, v2)...]
keys() # list like object of keys
values() # list like object of values
pop(k) # remove k/v pair..
popitem()
old_d.update(d) # takes all keys from d and adds them to old_d... if they exist, then just change the value

fileio
-----
1. loop over file object (each line still contains \n)
2. read() returns whole string (required split on \n to get separate lines)
3. readlines() returns list of strings, each element a line (w/ \n)





































































