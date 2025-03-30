# HASH MAP is called distionary in python


hash = {}

hash["first"] = 123
hash["last"] = 111
hash["alice"] = 909

print(hash['first'])
# print(hash['lastName'])

print('newKey' in hash)


# another way to initialize
newHash = { "name": "saurbah", "class": 122}

# new way to initialize dictionary
newDist = { i: 2*i for i in range(50)}
print(newDist)


# looping through map
myMap = {"name": "saurbah", "class": 1000}

for key in myMap:
    print(f"key: {key}, value: {myMap[key]}")