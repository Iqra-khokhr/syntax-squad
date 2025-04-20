# List with a typo in function name and logic error
numbers = [1, 2, 3, 4, 5]
numbers.apend(6)  # Typo: 'apend' instead of 'append'
print("Numbers:", numbers[6])  # IndexError

# Tuple modification (tuples are immutable)
my_tuple = (10, 20, 30)
my_tuple[1] = 25  # TypeError

# Selection structure with assignment instead of comparison
x = 10
if x = 5:  # SyntaxError: should be '=='
    print("x is 5")

# Loop repetition with incorrect range and indentation
for i in range(5)
print(i)  # IndentationError and missing colon

# List comprehension with syntax issue
squares = [i*i for i in range(5) if i % 2 = 0]  # SyntaxError in condition

# Dictionary with duplicate keys and access error
my_dict = {'a': 1, 'b': 2, 'a': 3}
print(my_dict['c'])  # KeyError: 'c' doesn't exist

# Set with unhashable item
my_set = set()
my_set.add([1, 2, 3])  # TypeError: list is unhashable

# Infinite loop due to missing update
count = 0
while count < 5:
    print("Counting...")  # No increment, infinite loop



