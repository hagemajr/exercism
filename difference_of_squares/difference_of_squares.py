def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

def square_of_sum(n):
    return sum([x+1 for x in list(range(n))])**2

def sum_of_squares(n):
    return sum([(x+1)**2 for x in list(range(n))])