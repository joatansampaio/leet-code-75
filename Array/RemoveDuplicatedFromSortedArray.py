
given_array = [1, 2, 2]


'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

def removeDuplicates(nums):
    j = 0
    for i in range(len(nums)):
        if nums[j] != nums[i]:
            j = j + 1
            nums[j] = nums[i]
    return j+1;

print(removeDuplicates(given_array))