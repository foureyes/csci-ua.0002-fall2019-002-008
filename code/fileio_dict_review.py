"""
we'll load everything into a dictionary
we will display it
ask the user for a word... and if the word is in dictionary, print out one of the synonyms

thesuarus:
tasty has 1 synonym: delicious
difficult has 2 synonyms: tough, hard

give me a word:
> difficult
a synonym for difficult is tough

give me a word:
> beautiful
i don't know that word yet


1. load into dictionary - make this a function
2. display our thesaurus - make this a function
3. interactive part - put into a "main" function
thesaurus = {
    yes: [yeah, ok, right],
    difficult: [hard, tough]
}
"""

import util
thesaurus = util.load_thesaurus('fake.txt')
for word, synonyms in thesaurus.items():
    print(f'{word} has {len(synonyms)} synonyms: {",".join(synonyms)}')
answer = input('give me a word\n>')
"""
get will attempt to retrieve value at key
if key doesn't exist NO EXCEPTION is raised
... returns second argument passed (defaults to None)
"""
print(thesaurus.get(answer, f'I do not know {answer}'))
"""
try:
    print(thesaurus[answer])
except KeyError:
    print(f'i do not know what a {answer} is')
"""
# answer = yes
#print(thesaurus)


#print(f.read()) # a single string
#print(f.readlines()) # a list of strings (each w/ a newline)

























