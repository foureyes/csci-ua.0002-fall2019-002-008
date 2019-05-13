"""
write a function that operates as follow:

words = ['hi', 'hey', 'hello']
new_words = shout(words)
print('words') #['hi', 'hey', 'hello'] (Same)
print(new_words, new_words) # ['HI!', 'HEY!', 'HELLO!']
"""
"""
def shout(old_list):
    new_list = []
    for w in old_list:
        new_list.append(w.upper() + '!')
    return new_list

words = ['hi', 'hey', 'hello']
new_words = shout(words)
print('words', words) #['hi', 'hey', 'hello'] (Same)
print('new_words', new_words) # ['HI!', 'HEY!', 'HELLO!']

"""

"""
words = ['hi', 'hey', 'hello']
shout(words) # shout does not give back val 
print('words', words) # modified 
"""
"""
words = ['hi', 'hey', 'hello']
def shout_in_place(old_list):
    for i in range(len(old_list)):
        old_list[i] = old_list[i].upper() + '!'
enumerate 
* built in function
* .... called with a list passed in
* returns a list (like a list)
* returned list contains tuples
    * each tuple is two elements
    * 1st element is index
    * 2nd element is value
* enumerate breaks down list into its indexes and values as separate pairs

words = ['hi', 'hey', 'hello']
result = enumerate(words)
result = [(0, 'hi'), (1, 'hey'), (2, 'hello')]
"""
"""
words = ['hi', 'hey', 'hello']
result = enumerate(words)
for t in result:
    print(t)
for i, v in enumerate(words):
    print(i, v)
"""
"""
shout_in_place(words) # shout does not give back val 
print('words', words) # modified 
    # NO return!!!!
"""         
"""
words[0] = words[0].upper() + '!'
words[1] = words[1].upper() + '!'
words[2] = words[2].upper() + '!'
"""
"""
#print(words)
words = ['hi', 'hey', 'hello']
def shout_in_place(old_list):
    for i in range(len(old_list)):
        old_list[i] = old_list[i].upper() + '!'

def shout_in_place(old_list):
    for i, word in enumerate(old_list):
        old_list[i] = word.upper() + '!'
"""
"""
swap first and last
"""
"""
def swap(li):
    if len(li) > 0:
        li[0], li[-1] = li[0], li[-1]

sound_cloud_rappers = ['lil uzi vert', 'post malone', 'lil peep']
print('before', sound_cloud_rappers)
swap(sound_cloud_rappers)
print('after', sound_cloud_rappers)
"""




















