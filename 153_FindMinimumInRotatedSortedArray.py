# this is here because of LeetCode 33


class Solution:
    # that weird solution I found working but IDK how it works
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while (right - left) > 1:
            mid = (left + right) // 2
            bigVal = max(nums[left], nums[right])

            if nums[mid] < bigVal:
                right = mid
            else:
                left = mid + 1

        return min(nums[left], nums[right])

    # the solution after watch neetcode solving leetcode 33, with that graph 
    # target: smallest value
    # left side: index range from left to target - 1
    # right side: index range from target to right, so if we're ever here, current left index is the answer
    def findMinV2(self, nums) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # right side, we have a simple slope here
            # if left is not the smallest point we already fuck it up, which should never happen
            if nums[l] < nums[r]:
                return nums[l]
            # left side,  with the graph I can know
            # if m > l, target will be at right area
            # if m < r, target will be at left area
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
