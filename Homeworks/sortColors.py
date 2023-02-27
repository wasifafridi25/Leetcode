def sort(nums):
    i, l, r = 0, 0, len(nums) - 1
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
def main():
    print("Example 1:")
    print("Before sort: ")
    nums1 = [2,0,2,1,1,0]
    print(nums1)
    sort(nums1)
    print("--------------After sort: ")
    print(nums1)
    
    print("Example 2:")
    print("Before sort: ")
    nums2 = [2,0,1]
    print(nums2)
    sort(nums2)
    print("--------------After sort: ")
    print(nums2)
    
    print("Example 3:")
    print("Before sort: ")
    nums3 = [2, 2, 2, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0]
    print(nums3)
    sort(nums3)
    print("--------------After sort: ")
    print(nums3)
    
    
if __name__ == "__main__":
    main()
        
          

    