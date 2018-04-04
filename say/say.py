nummap = {
    0:"zero", 
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"one hundred",
    }

testnum = -87
strnum = str(testnum)
retstr = ""
if strnum[0] == '-':
    retstr += "negative "
    strnum = strnum[1:]


for i,x in enumerate(strnum):
    if len(strnum) - i == 2 and i == 0:
        tmp = int(x)*10
        retstr += nummap[tmp] + " "
    else:
        retstr += nummap[int(x)] + " "
print(retstr.strip())

