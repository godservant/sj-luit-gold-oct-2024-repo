

# What is import random used for?
# In Python, import random is a statement that allows you to access the functions and classes provided by the random module.
# This module is part of Python's standard library and is used for generating random numbers, shuffling sequences, and making random selections.

# What Is a Function?
# A function is a block of reusable code that performs a specific task. It can take input (parameters) and return a result.


# Explanation of def generate_ec2_name():
# def: This is a keyword in Python that is short for "define." It tells Python that you're creating a new function.

# generate_ec2_name: 'man_made_name'
# This is the name of the function. The name should be descriptive, so you (and others) know what the function does.

# (): These parentheses indicate that this function can take inputs (called parameters). In this case, the parentheses are empty, so it doesn't take any input.

# :: The colon marks the beginning of the function body. Everything indented after this line is part of the function.


# def generate_ec2_name():
# In Python, the line def generate_ec2_name(): is used to define a function. Here's a breakdown of what it does:

# Explanation of def generate_ec2_name():
# def: This is a keyword in Python that is short for "define." It tells Python that you're creating a new function.

# generate_ec2_name: This is the name of the function. The name should be descriptive, so you (and others) know what the function does.

# (): These parentheses indicate that this function can take inputs (called parameters). In this case, the parentheses are empty, so it doesn't take any input.

# :: The colon marks the beginning of the function body. Everything indented after this line is part of the function.

# Reusability: Instead of repeating code, you can call the function whenever needed.
# Readability: It makes the code cleaner and easier to understand.
# Flexibility: Functions can take inputs and return different results.




import random

# Lists of possible name components
prefixes = ["web", "app", "db", "cache", "api"]
environments = ["dev", "test", "prod", "stage"]
numbers = list(range(1, 101))  # Numbers from 1 to 100

# Function to generate a random EC2 name
def generate_ec2_name():
    prefix = random.choice(prefixes)  # Pick a random prefix
    env = random.choice(environments)  # Pick a random environment
    num = random.choice(numbers)  # Pick a random number
    return f"{prefix}-{env}-{num}"

# Generate and display some random EC2 names
if __name__ == "__main__":
    for _ in range(5):  # Generate 5 random names
        print(generate_ec2_name())
        


