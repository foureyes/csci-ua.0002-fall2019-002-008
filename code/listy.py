"""
write a function:
increment(arg)
returns a list

numbers = [100, 101, 102]
new_numbers = increment(numbers)
print(numbers) # [100, 101, 102] (same)
print(new_numbers) # [101, 102, 103]
"""
def increment(my_list):
    new_list = []
    for element in my_list:
        new_list.append(element + 1)
    return new_list
numbers = [100, 101, 102]
#new_numbers = increment(numbers)
#print('numbers', numbers) # [100, 101, 102] (same)
#print('new numbers', new_numbers) # [101, 102, 103]


"""
increment_in_place - original list will be changed!!!
we're not going to return anything
"""
def increment_in_place(my_list):
    # new_list = [] ...no new list needed, bc we're changing
    # original
    for i in range(len(my_list)):
        # new_list.append(element + 1)
        my_list[i] = my_list[i] + 1
    # return new_list NO RETURN 
# increment a specific element
numbers = [100, 101, 102]
# increment_in_place(numbers)
"""
result = increment_in_place(numbers)
print('result', result) # None
print('numbers', numbers) # original changes
"""


words = ['foo', 'bar', 'baz']
enumerate(words) # [(0, 'foo'), (1, 'bar'), (2, 'baz')]
# enumerate gives back a list-like object
# each element in the list is a tuple, where the elements are:
# (index, value)
for t in enumerate(words):
    print(t)

for i, value in enumerate(words):
    print(i, value)

def increment_in_place(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i] + 1

def increment_in_place(my_list):
    for pos, num in enumerate(my_list):
        my_list[pos] = num + 1














