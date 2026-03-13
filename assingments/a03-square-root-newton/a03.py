## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(num, guess=0.0):
    
    if num == 0:
        return None
    
    if good_enough(guess, num):
        return guess
    else:
        new_guess = improve_guess(guess, num)
        return sqrt(num, new_guess)

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(first_num, second_num):
    avg = (first_num + second_num) / 2.0
    return avg
#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(a, x):
    if a == 0.0:
        a = a + 1.0
 
    x = x * 1.0

    better_guess = average(a, x/a)
    return better_guess
#### End OF MARKER

#### YOUR CODE FOR good_engoth() FUNCTION GOES HERE ####
def good_enough(guess, num):
    if abs(guess * guess - num) < 0.12346:
        return True
    else:
        return False
#### End of MARKER

if __name__ == '__main__':
    print (sqrt(36))
