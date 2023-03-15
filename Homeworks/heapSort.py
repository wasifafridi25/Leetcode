class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(nums, n, i):
            """
            Helper function to maintain the max-heap property of the tree,
            by swapping the root node with its largest child if necessary.
            """
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        def build_heap(nums, n):
            """
            Helper function to build a max-heap from the given list of integers.
            """
            for i in range(n // 2 - 1, -1, -1):
                heapify(nums, n, i)

        n = len(nums)
        build_heap(nums, n)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums
def main():
    s = Solution()

    print("Test case 1: ")
    result1 = s.sortArray([5,2,3,1])
    print(result1)

    print("Test case 2: ")
    result2 = s.sortArray([5,1,1,2,0,0])
    print(result2)


if __name__ == '__main__':
    main()    