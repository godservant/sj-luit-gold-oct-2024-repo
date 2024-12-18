import random

# while loop

number = random.randint(0,10)

counter = 0

while number != 7:
    number = random.randint(0,10)
    counter = counter + 1 # counter += 1
    
    if counter >= 13:
        break
    
    print(counter, number)
    
    # for loop
    
    for i in range(10):
        if i**2 <50:
            print(1, 1**2)
        else:
            break
    print(i)
    
    
        

        

    
    
    
