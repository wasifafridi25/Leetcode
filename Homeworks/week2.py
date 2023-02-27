class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        test = {}
        for i in range(len(nums)):
            if nums[i] not in test:
                test[target - nums[i]] = i
            else:
                return test[nums[i]], i
def main():
    s1 = Solution()
    
    nums = [2,7,11,15]
    target = 9
    print("Example 1:")
    print("Input: nums = ", nums, ", target = ", target)
    l1 : list = s1.twoSum(nums, target)
    print("Output: ", l1)
    
    nums = [3,2,4]
    target = 6
    print("Example 2:")
    print("Input: nums = ", nums, ", target = ", target)
    l1 : list = s1.twoSum(nums, target)
    print("Output: ", l1)
    
    nums = [3,3]
    target = 6
    print("Example 3:")
    print("Input: nums = ", nums, ", target = ", target)
    l1 : list = s1.twoSum(nums, target)
    print("Output: ", l1)

if __name__ == "__main__":
    main()                
        