from collections import deque

class Solution:
    def permute(self, nums):
        results = []
        nums_deque = deque(nums)
        def dfs(items, remains):
            if len(remains) == 0:
                results.append(items.copy())
                print("res",results)
                return
            
            for i in range(0,len(remains)):
                r = remains.pop()
                items.append(r)
                dfs(items,remains)
                items.pop()
                remains.appendleft(r)

            
        dfs([], nums_deque)
        return results


print((Solution()).permute([1, 2, 3]))
