#(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0


def verify(isbn):
    try:
        isbn_digits = [10 if x == 'X' and i == 9 else int(x) for i,x in \
            enumerate([x for x in isbn if x.isalnum()]) if x.isalnum()] 
        return (isbn_digits[0] * 10 + isbn_digits[1] * 9 + isbn_digits[2] \
            * 8 + isbn_digits[3] * 7 + isbn_digits[4] * 6 + isbn_digits[5] \
            * 5 + isbn_digits[6] * 4 + isbn_digits[7] * 3 + isbn_digits[8] \
            * 2 + isbn_digits[9] * 1) % 11 == 0
    except:
        return False

print(verify('3-598-21507-X'))