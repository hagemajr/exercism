import re

def hey(msg):
    if len(msg.strip()) == 0:
        return 'Fine. Be that way!'
    if msg.upper() == msg and re.search('[a-zA-Z]', msg):
        if msg.strip()[-1] == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return  'Whoa, chill out!'
    else:
        if msg.strip()[-1] == '?':
            return 'Sure.'
        else:
            return 'Whatever.'