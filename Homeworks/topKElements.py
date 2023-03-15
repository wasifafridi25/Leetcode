import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq_dict = Counter(nums)
        max_heap = [(-freq_dict[key], key) for key in freq_dict]
        heapq.heapify(max_heap)
        result = []
        for i in range(k):
            if max_heap:
                result.append(heapq.heappop(max_heap)[1])
            else:
                break
        
        return result
def main():
    s = Solution()

    print("Test case 1: ")
    result1 = s.topKFrequent([1,1,1,2,2,3], 2)
    print(result1)

    print("Test case 2: ")
    result2 = s.topKFrequent([1],1)
    print(result2)


if __name__ == '__main__':
    main()    
    
    
    