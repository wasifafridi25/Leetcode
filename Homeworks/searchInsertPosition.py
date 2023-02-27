class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if target < nums[m]:
            return m
        else:    
            return m + 1 
def main():
    s = Solution()
    print("Sample 1 Example:")
    position1 = s.searchInsert([1,3,5,6], 5)
    print("Position: ", position1)
    
    print("Sample 2 Example:")
    position2 = s.searchInsert([1,3,5,6], 2)
    print("Position: ", position2)
    
    print("Sample 3 Example:")
    position3 = s.searchInsert([1,3,5,6], 7)
    print("Position: ", position3)
    
    
    
    
    

if __name__ == "__main__":
    main()            