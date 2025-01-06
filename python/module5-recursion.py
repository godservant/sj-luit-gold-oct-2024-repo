# factorial
# 3! = 1 * 2 * 3 = 6
# 5% = 1 * 2 * 3 * 4 * 5 = 120

def get_factorial(number):
    factorial = 1
    for x in range(1,  number + 1):
        factorial *= x
        return factorial
    
print(get_factorial (6))

