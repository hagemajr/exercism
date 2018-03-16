def detect_anagrams(s,l):
    r = [x for x in l if sorted(s.lower()) == sorted(x.lower()) and s.lower() != x.lower()]
    return r
