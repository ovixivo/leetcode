class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #slow method

        full = sorted(nums1 + nums2)
        f = len(full)

        if f % 2:
            i = f / 2
            return float(full[int(i)])

        else:
            i = f // 2
            j = i - 1
            return float((full[int(i)] + full[int(j)])/2)