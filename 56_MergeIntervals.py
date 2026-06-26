from typing import List

class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        ptr = intervals[0]
        for interval in intervals[1::]:
            if self.overlapped(ptr,interval):
                ptr = [ptr[0],max(ptr[1],interval[1])]
                continue
            merged.append(ptr)
            ptr = interval
        merged.append(ptr)
        return merged
    

    def overlapped(self,ptr,interval):
        return interval[0] <= ptr[1] <= interval[1] or ptr[0] <= interval[0] <= ptr[1]


def valid(input,output):
    good = (Solution()).merge(input) == output
    print("Pass" if good else "Failed")


valid([[1,3],[2,6],[8,10],[15,18]],[[1,6],[8,10],[15,18]])
valid([[1,4],[4,5]],[[1,5]])
valid([[4,7],[1,4]],[[1,7]])
valid([[1,3],[6,8],[3,6]],[[1,8]])
valid([[1,4],[2,3]],[[1,4]])