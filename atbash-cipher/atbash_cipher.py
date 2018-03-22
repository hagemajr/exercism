def encode(txt):
    orig = 'abcdefghijklmnopqrstuvwxyz'
    coded = orig[::-1]
    seq = [coded[orig.find(x)] if x.isalpha() else x for i,x in enumerate(txt.lower()) if x.isalnum()]
    return ' '.join([''.join(seq[i:i+5]) for i  in range(0, len(seq), 5)])

def decode(txt):
    orig = 'abcdefghijklmnopqrstuvwxyz'
    coded = orig[::-1]
    return ''.join([orig[coded.find(x)] if x.isalpha() else x for i,x in enumerate(txt.lower().replace(' ','')) if x.isalnum()])

print(encode("The testing  quick brown fox jumps over the lazy dog."))
print(decode(encode("the quick brown fox")))
