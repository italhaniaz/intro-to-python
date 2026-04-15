def sqrt(x, guess=1.0):
    if good_enough(guess, x):
        return guess
    else:
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)
    

def good_enough(guess, x):
    return abs(guess*guess -x) < 1e-5


def avg(a, b):
    return (a + b) /2


def improve_guess(guess, x):
    return avg(guess, x/guess)


print(sqrt(36))