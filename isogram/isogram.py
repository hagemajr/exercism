def is_isogram(msg):
    tmpmsg = "".join([x.lower() for x in msg if x.isalnum()])
    distinct_letters = set(tmpmsg)
    if len(distinct_letters) == len(tmpmsg):
        return True
    else:
        return False
