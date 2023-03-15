from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Initialize distance array with infinite values
        distance = [float('inf')] * N
        # Distance from source node to itself is zero
        distance[K-1] = 0
        
        # Relax edges N-1 times
        for _ in range(N-1):
            for u, v, w in times:
                # If we can reach v node with less weight through u node
                if distance[u-1] + w < distance[v-1]:
                    # Update distance of v node
                    distance[v-1] = distance[u-1] + w
        
        # Find the maximum distance from source node to any other node
        max_time = max(distance)
        return -1 if max_time == float('inf') else max_time

def main():
    s = Solution()
    print("Test case from manual solution:")
    A, B, C, D, E = 1, 2, 3, 4, 5
    t1 = s.networkDelayTime([[A,B,1], [A,D,2], [B,C,2], [D,C,2], [C,E,8], [D,E,3]], 5, 1)
    print("Minimum time: ", t1)

    print("Leetcode test cases: ")

    print("Test case 1: ")
    t1 = s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
    print("Minimum time: ", t1)

    print("Test case 2: ")
    t2 = s.networkDelayTime([[1,2,1]], 2, 1)
    print("Minimum time: ", t2)

    print("Test case 3: ")
    t3 = s.networkDelayTime([[1,2,1]], 2, 2)
    print("Minimum time: ", t3)

if __name__ == '__main__':
    main()
