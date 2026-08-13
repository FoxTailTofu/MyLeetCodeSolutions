from typing import List

class Solution:

    # My solution
    # The hint said use counting sort, so I think this is the "correct" answer 
    def sortColors(self, nums: List[int]) -> None:
        # index stands for color
        colors = [0,0,0]
        for color in nums:
            colors[color] +=1
        index = 0
        for color in range(len(colors)):
            while colors[color] > 0:
                nums[index] = color
                colors[color] -= 1
                index+=1

    # the answer everyone's using, by swaping the 0's and 2's to the side
    def sortColors_swap(self,nums: List[int]) -> None:
        left = 0
        right = len(nums)-1
        mid = left
        # whenever I find a 0 or 2, I move it to the side using the left/right pointer, then continue scanning
        while mid <= right:
            if nums[mid] == 0:
                # it's 0, put it to the left
                nums[mid],nums[left] = nums[left],nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                # nothing important, skip, if we find any 0's, it should be swapped to the correct spot
                mid += 1
            elif nums[mid] == 2: 
                # if we swap the value to the right, it means the new value from the right is not checked
                # so we need to check it by not increment mid
                nums[mid],nums[right] = nums[right],nums[mid]
                right -= 1

nums = [2,0,2,1,0,0,1,2,1,0,1]
(Solution()).sortColors_swap(nums)
print(nums)