class Solution:
    def search(self, nums, target) -> int:
        size = len(nums)
        left = 0
        right = len(nums) - 1
        # try to find the pivot first
        offset = self.findPivot(nums)
        # then just do a binary search with that pivot offset applied
        while left <= right:
            mid = (left + right) // 2
            midOffset = (mid + offset) % size
            if nums[midOffset] > target:
                right = mid - 1
            elif nums[midOffset] < target:
                left = mid + 1
            else:
                return midOffset
        return -1

    # I kinda just figure this out for no reason, need explanation
    # after needcode video i still don't know why this work because different solution lol
    def findPivot(self, nums):
        left = 0
        right = len(nums) - 1
        while (right - left) > 1:
            mid = (left + right) // 2
            bigVal = max(nums[left], nums[right])

            if nums[mid] < bigVal:
                right = mid
            else:
                left = mid + 1

        leftVal = nums[left]
        rightVal = nums[right]

        if leftVal >= rightVal:
            return right
        else:
            return left

    # https://www.youtube.com/watch?v=U8XENwh8Oy8
    # drawing the graph and mark mid/target helps understand this alot
    def search_NeetCode(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # left sorted area
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                elif target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    raise Exception("should not happen")

            # right sorted area
            else: 
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                elif target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    raise Exception("should not happen")
        return -1

def test(nums, pivotAns, target, ans):
    # pivot = (Solution()).findPivot(nums)
    # print("pivot: ", end="")
    # print("ok" if pivot == pivotAns else "fail",end="")

    result = (Solution()).search_NeetCode(nums, target)
    print(", result: ", end="")
    print("ok" if result == ans else (result,ans))

print("1--")
test([1], 0, 1, 0)
test([1, 2], 0, 1, 0)
test([2, 1], 1, 1, 1)
test([1, 2, 3, 4, 5, 6], 0, 1, 0)
test([2, 3, 4, 5, 6, 1], 5, 1, 5)

print("2--")
test([3, 4, 5, 6, 1, 2], 4, 1, 4)
test([4, 5, 6, 1, 2, 3], 3, 1, 3)
test([3, 4, 5, 6, 1, 2], 0, -1, -1)
test([4, 5, 6, 1, 2, 3], 0, -1, -1)
test([5, 6, 1, 2, 3, 4], 2, 1, 2)

print("3--")
test([6, 1, 2, 3, 4, 5], 1, 1, 1)
test([1, 2, 3, 4, 5, 6, 7], 0, 1, 0)
test([2, 3, 4, 5, 6, 7, 1], 6, 1, 6)
test([3, 4, 5, 6, 7, 1, 2], 5, 1, 5)
test([3, 4, 5, 6, 7, 1, 2], 0, -1, -1)

print("4--")
test([4, 5, 6, 7, 1, 2, 3], 4, 1, 4)
test([5, 6, 7, 1, 2, 3, 4], 3, 1, 3)
test([6, 7, 1, 2, 3, 4, 5], 2, 1, 2)
test([7, 1, 2, 3, 4, 5, 6], 1, 1, 1)
test([7, 1, 2, 3, 4, 5, 6], 1, 4, 4)

print("5--")
test([7, 1, 2, 3, 4, 5, 6], 1, 0, -1)
