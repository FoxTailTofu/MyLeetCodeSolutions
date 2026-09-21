import time


class Solution:
    # I don't except this to pass the test, but I guess it does
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        goal = total // 2
        cumulate = set({0})
        for i in range(0, len(nums)):
            # I run into change size while looping cumulate, so i put it inside temp first
            temp = []
            for c in cumulate:
                if c + nums[i] == goal:
                    return True
                temp.append(c + nums[i])
            for t in temp:
                cumulate.add(t)
        return False


def validate(s, exp):
    start = time.time()
    result = (Solution()).canPartition(s)

    if result != exp:
        print(s, exp, result)
    print("--T: {:.2f}".format(time.time() - start))


validate([1, 5, 11, 5], True)
validate([1, 2, 3, 5], False)
