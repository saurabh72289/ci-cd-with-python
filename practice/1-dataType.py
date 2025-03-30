# Integer
num = 10
val = 99
# print(num)

# Float
pi = 3.14
# print(pi)


# String
name = "Alice"
# print(name)

# Boolean
is_active = True
# print(is_active)


# List (mutable)
numbers = [1, 2, 3, 4,"hellooo"]
numbers[1] = 100000
print(numbers[4])

# Tuple (immutable)
coordinates = (10, 20, 9990)
tupl = (11, 221, 21 )
# tupl[0] = 1231231   tuple are immutable
print(tupl[0])
print(coordinates[0])

# Dictionary (key-value pair)
# key is not mutable
# values are mutable
user = {"name": "Alice", "age": 25}
user["name"] = "saurabh"
print(user['name'], 'user NAME using dictionary')
print(user['age'], 'user AGE using dictionary')

# Set (unique values)
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)
print(3 in unique_numbers)
print(4 in unique_numbers)
print(5 in unique_numbers)
unique_numbers.add(100)
print("\n\n 100 in unique number",100 in unique_numbers)

print(f"the cordinates {coordinates[0]} is situated on the {user['name']} house")


val = True
# this is assignment not modification
val = False  # Naya object assign hota hai
print(val)   # False

lst = [True]
lst[0] = False  # List ke andar change hota hai, naya object nahi banta
print(lst)      # [False]