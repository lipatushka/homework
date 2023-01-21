def countOnes(number):
    counter = 0
    while (number > 0):
        counter += (number & 1)
        number >>= 1
    return counter

def convert(val, ones):
    return f'1{ones % 2}' + (f'{val:b}{ones % 2}')[2:]

def R(N):   
    ones = countOnes(N)
    return int(convert(N, ones), 2)

def task(arguments):
    limit = arguments
    for N in range(limit):
        answer = R(N)
        if (answer > limit):
            return N
    return None

if __name__ == '__main__':
    print(task(40))
