import random

number = random.randint(0,10)

# print("Hello") # syntax error. Unexpected Indent

threshold = 6

if number < threshold:
    print("Small Number")
elif number > threshold:   
    print("Big Number")
else: # elif number == threshold:
    print("Number is"), threshold

print("dedented")
print(number)


# 1/0