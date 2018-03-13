def encode(val):
    encoded = []
    a = []
    for x in val:
        if x in a or len(a) == 0:
            a.append(x)
        else:
            encoded.append((len(a), a[0]))
            a = [x]
    if len(a) != 0:
        encoded.append((len(a), a[0]))
    return "".join([('' if count == 1 else str(count)) + str(ltr) for count,ltr in encoded])

def decode(val):
    decoded = []
    a = '0'
    for x in val:
        if x.isnumeric():
            a += str(x)
        else:
            tup = (int(1 if a == '0' else a),x)
            a = '0'
            decoded.append(tup)
    return "".join([x for x in sum([count * [ltr] for count,ltr in decoded],[])])