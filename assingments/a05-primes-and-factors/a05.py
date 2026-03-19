## IMPORTS GO HERE

## END OF IMPORTS

def is_integer(num):
  x = num - int(num)
  if x > 0:
    return False
  else:
    return True

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(num):
    if not is_integer(num):
        return False
    if num <= 1:
        return None
    
    num = int(num)
    for i in range(2, num):
        for j in range(2, num):
            multiple = i * j
            if multiple == num:
                return False
  
    return True
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(num):

    if not is_integer(num):
        return False
    if num <= 1:
        return None
    
    num = int(num)

    for i in range(1, num + 1):
        if num % i == 0:
            factor = i
            print(factor)
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(num):
    if num <= 1:
        return None

    num = int(num)

    if is_prime(num):
        return num
    else:
        largest_prime = 0
        for i in range(2, num):
            if is_prime(i) and i > largest_prime:
                largest_prime = i
    
        if largest_prime != 0:
            return largest_prime
        else:
            return None

#### End OF MARKER



if __name__ == '__main__':
    print (is_prime(499))  # should return True

    print (get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
