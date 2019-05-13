"""
thesaurus = {
    yes: [ok, yeah, aye], 
    delicious: [tasty, yummy],
    good: [nice]
}
show all items in thesaurus:
yes has 3 synonyms: ok, yeah, aye
delicious ...

give me a word

if word doesn't exist
idk!!!!
"""
import wordtools
thesaurus = wordtools.load_thesaurus('t.csv')
print(thesaurus)


#print(f.read()) # entire contents as string
#print(f.readlines()) # entire contents as string














