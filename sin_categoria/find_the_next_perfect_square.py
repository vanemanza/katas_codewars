"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

"""
import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    raiz = math.sqrt(sq)
    if raiz.is_integer():
        return round((raiz+1)**2)
    return -1

test1 = find_next_square(121)
test2 = find_next_square(625)
test3 = find_next_square(114)

print(test1, test2, test3)