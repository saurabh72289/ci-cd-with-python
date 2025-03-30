# set
mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)

print(mySet, f"also lenth of set {len(mySet)}")

print( 1 in mySet)
print( 2 in mySet)
print( 3 in mySet)
print( 4 in mySet)

mySet.remove(1)
print( 1 in mySet) # O(N)


# create set
myset = set([1,3,4,5,3])
print(myset)