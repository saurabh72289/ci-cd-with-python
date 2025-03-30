
arr = [1,2, 3, 4, 5, 6, 7, 8, 9]
arr.reverse()
# print(arr)


arr2 = [22, 42, 56, 88, 61, 90, 100]
# arr2.sort(reverse=False) # for accending order
arr2.reverse() # for decending order by default it works
# print(arr2)



# string sorting
lis = ["aello", "world", "buzzle", "weather", "flying"]
lis.sort() # based on alphabetical order Accending order
print(lis)


# custom sort according to length of the string ACCENDING ORDER
lis.sort(key=lambda x: len(x), reverse=True)
print(lis)