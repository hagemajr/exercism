def encode(txt):
    orig = 'abcdefghijklmnopqrstuvwxyz'
    coded = orig[::-1]
    [coded[i] if x.isalpha() else x if x.isnum() else '' for i,x in enumerate(txt.lower())]

def decode(txt):
    pass