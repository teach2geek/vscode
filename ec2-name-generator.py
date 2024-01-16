import random

# Example usage for the 'Finance' department needing 5 EC2 names
department = input("What is your department? ")
instances = int(input("How many EC2 instances? "))

def generate_ec2_names(department, instances):
    unique_names = set()
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%()'  # All possible characters
    while len(unique_names) < instances:
        random_chars = ''.join(random.choices(chars, k=8))
        name = f"{department}-{random_chars}"
        unique_names.add(name)
    
    return list(unique_names)

ec2_names = generate_ec2_names(department, instances)
for name in ec2_names:
    print(name)