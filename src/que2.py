
# arr1 = [1,2,1,0,5,6, 5]
# tar = 6

# ex:
# pairs
# 1 5
# 1 5
# 0 6

# print the values form the array 

def find_pairs_in_array(arr, target:int):
    sorted_Array =  arr
    sorted_Array.sort()  # O(n log n) time complexity
    left, right = 0, len(arr) -1
    pairs = []
    
    while left < right:
        current_sum = sorted_Array[left] + sorted_Array[right]
        
        if current_sum == target:
            pairs.append((sorted_Array[left], sorted_Array[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    print(pairs,"------>>>\n\n")
    return pairs


import unittest

class TestFindPairsInArray(unittest.TestCase):
    def test_find_pairs_in_array_with_duplicates(self):
        arr = [1, 2, 1, 0, 5, 6, 5]
        target = 2
        self.assertEqual(find_pairs_in_array(arr, target), [(0,6), (1, 5), (1, 5)])
    
    def test_find_pairs_in_array_with_no_pairs(self):
        arr = [1, 2, 3, 4, 5]
        target = 60
        self.assertEqual(find_pairs_in_array(arr, target), [])

if __name__ == "__main__":
    unittest.main()












# arr1 = [1,2,1,0,5,6,5]
# target = 6

# sorted_Array = arr1
# sorted_Array.sort()
# print(sorted_Array)
# left = 0
# right = len(arr1) -1
# pairs = []
    
# # while left < right:
# #     current_sum = sorted_Array[left] +  sorted_Array[right]
# #     if current_sum == target:
# #         pairs.append((sorted_Array[left], sorted_Array[right]))
# #         left += 1
# #         right -= 1
# #     elif current_sum < target:
# #         left += 1
# #     else:
# #         right -= 1
#     # return pairs
# print(pairs,"------>>>\n\n")


