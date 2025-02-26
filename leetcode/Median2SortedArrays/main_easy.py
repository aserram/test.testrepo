from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = (nums1 + nums2)
        merged.sort()
        lenght = int(len(merged)) 
        if lenght % 2:
            median = merged[int((lenght-1)/2)]
        else:
            median = (merged[int(lenght/2) - 1] + merged[int(lenght/2)])/2
        return float(median)

def main():
    target = Solution()
    result = target.findMedianSortedArrays([1,3], [2])
    print(result)

if __name__ == "__main__":
    main()