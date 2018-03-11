def is_pangram(msg):
    letters = set("".join([x.lower() for x in msg if x.isalpha()]))
    if len(letters) == 26:
        return True
    else:
        return False