from collections import deque

# create an empty list started with 0
# loop each item in that list
# loop each candidates, I add the candidate into current item and test:
#   the sum of item = target => add into success list
#   the sum of item < target => we can add more candidates in it, add this back to the item list
#   the sum of item > target => the sum is too big, ignore it


# we sort the input candidates from smallest to largest, to prevent duplicated result happening
# from the example of c = [2,3,6,7], t = 7, one of the answer we want is [2,2,3]
# but we don't want others like [3,2,2] and [2,3,2], so we only add value that's bigger than the previous added one
# so when I have [2,3], I won't test [2,3,2] because the extra 2 will be tested with [2,2,3]
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # if the candidates comes sorted I don't need this
        candidates.sort()

        sumList = deque([[]])
        success = []
        while len(sumList):
            selected = sumList.pop()
            sumOfSelected = sum(selected)
            for c in candidates:
                currentBiggestValue = selected[-1] if selected else 0
                total = sumOfSelected + c
                # the result is ordered from smallest to largest, so we can have [2,3] but no [3,2]
                if currentBiggestValue > c:
                    continue

                # add too many
                if total > target:
                    continue

                possible = selected.copy()
                possible.append(c)

                if total == target:
                    success.append(possible)
                else:
                    sumList.append(possible)
        return success

    # it's a cleaner recursive dfs solution from neetcode, just put it here so i know
    def combinationSum_NeetCode(self, candidates, target):
        res = []

        def dfs(i, cur: list, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # test something like [2,2] with more 2
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # i don't want more 2, I want to test [2,2,3] add go deeper into the candidates
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    # revisit at 2026/01/06
    def combinationSum_revisit(self, candidates, target):
        answers = []

        def dfs(items,index):
            if sum(items) == target:
                answers.append(list(items))
                return
                
            if sum(items) > target:
                return

            for i in range(index,len(candidates)):
                items.append(candidates[i])
                dfs(items,i)
                items.pop()


        dfs([],0)
        return answers

def test(c, t):
    print((Solution()).combinationSum(c, t))


test([2, 3, 6, 7], 7)
