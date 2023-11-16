import random

# Importing a custom module
import my_module
print(my_module.pi)

# Print random integer
random_integer = random.randint(1,10)
print(random_integer)

# Print random float between [0.0,1.0)
random_float = random.random()
print(random_float)

# Print random float between 0-5
random_float = random.random() * 5
print(random_float)
