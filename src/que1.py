# arr1  = [11, 1, 13, 21, 3, 7]
# arr2 = [11, 3,1111, 7, 1,99, 88]

# wrtie a function to print true if array2 is a subset of arr1 
# print false if it is not a subset of arr
# along with wi have to print indices of the extra elements in the array2


# def checkSubset(arr1, arr2):
    
#     mySet = set([value for value in arr1])

#     extra_indices = []
#     for index, num in enumerate(arr2):
#         if num not in mySet:
#             extra_indices.append(index)

#     if extra_indices:
#         print("False")
#         print("Indexs of the extra elements in arr2", extra_indices)
#         return False, extra_indices
#     else:
#         print("True")
#         return True, []
    

def checkSubset(arr1, arr2):
    
    dict = {}
    for num in arr1:
        dict[num] = dict.get(num, 0) + 1
        

    extra_indices = []
    for index, val in enumerate(arr2):
        if dict.get(val, 0) > 0:
            dict[val] -= 1
        else:
            extra_indices.append(index)

    if extra_indices:
        print("False")
        print("Indexs of the extra elements in arr2", extra_indices)
        return False, extra_indices
    else:
        print("True")
        return True, []

arr1= []
arr2 = [12,123,1,1,1]
checkSubset(arr1, arr2)

# import unittest

# class TestCaseCheck(unittest.TestCase):    
#     def test_checkSubset_arrays_with_duplicates(self):
#         arr1 = [1, 2, 3, 4, 5]
#         arr2 = [1, 2, 3, 4, 5]
#         result, extraIndices = checkSubset(arr1, arr2)
#         self.assertTrue(result)
#         self.assertEqual(extraIndices, [])
    
#     def test_checkSubset_arrays_with_extra_elements(self):
#         arr1 = [1, 2, 3, 4, 5]
#         arr2 = [1, 2, 3, 4, 5, 6]
#         result, extraIndices = checkSubset(arr1, arr2)
#         self.assertFalse(result)
#         self.assertEqual(extraIndices, [5])
    


# if __name__ == '__main__':
#     unittest.main()

