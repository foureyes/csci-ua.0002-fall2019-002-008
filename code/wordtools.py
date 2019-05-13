class Thesaurus:
    def __init__(self, fn):
        f = open(fn, 'r')
        self.d = {}
        self.fn = fn
        for line in f:
            line_parts = line.strip().split(',')
            word = line_parts[0]
            syns = line_parts[1:]
            self.d[word] = syns
    def __str__(self):
        return f'my thesaurus {self.fn}'

t = Thesaurus('t.csv')
print(t)
print('file name', t.fn)
print('dictionary', t.d)






def load_thesaurus(fn):
    thesaurus = {}
    for line in f:
        line_parts = line.strip().split(',')
        word = line_parts[0]
        syns = line_parts[1:]
        thesaurus[word] = syns
    return thesaurus
