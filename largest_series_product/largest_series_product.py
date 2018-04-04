from functools import reduce
from operator import mul
import datetime

def largest_product(series, n):
    return max([reduce(mul,[int(y) for y in series[i:i+n]]) for i,x in enumerate(series) if len(series[i:i+n]) == n])

