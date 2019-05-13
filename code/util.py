def load_thesaurus(fn):
    f = open(fn, 'r')
    thesaurus = {}
    for line in f:
        line_parts = line.strip().split(',')
        word = line_parts[0]
        synonyms = line_parts[1:] # everything after first
        thesaurus[word] = synonyms
    f.close()
    return thesaurus
