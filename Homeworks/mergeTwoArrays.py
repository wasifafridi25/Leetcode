class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

def main():
    s = Solution()
    print("Example 1------")
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    print("Input: \nnums1: ", nums1, ",m = ", m, ",nums2: ", nums2, ",n = ", n)
    s.merge(nums1, m, nums2, n) 
    print("Result after merging: ", nums1)
    
    print("Example 2------")
    nums1, m, nums2, n = [1], 1, [], 0
    
    print("Input: \nnums1: ", nums1, ",m = ", m, ",nums2: ", nums2, ",n = ", n)
    s.merge(nums1, m, nums2, n) 
    print("Result after merging: ", nums1)
    
    print("Example 3------")
    nums1, m, nums2, n = [0], 0, [1], 1
   
    print("Input: \nnums1: ", nums1, ",m = ", m, ",nums2: ", nums2, ",n = ", n)
    s.merge(nums1, m, nums2, n) 
    print("Result after merging: ", nums1)
  

if __name__ == "__main__":
    main()            