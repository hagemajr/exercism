def sum_of_multiples(num,mults):
    return sum(set([x for x in range(num) for y in mults if x%y == 0]))