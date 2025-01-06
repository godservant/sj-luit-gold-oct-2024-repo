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


#web-test-23
#db-prod-88
#app-dev-12
#cache-stage-49
#api-prod-76
