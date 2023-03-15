from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = {i: [] for i in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        distance = {i: float('inf') for i in range(1, N+1)}
        heap = [(0, K)]

        while heap:
            time, node = heapq.heappop(heap)
            if time < distance[node]:
                distance[node] = time
                for neighbor, w in graph[node]:
                    if time + w < distance[neighbor]:
                        heapq.heappush(heap, (time+w, neighbor))

        max_time = max(distance.values())
        return -1 if max_time == float('inf') else max_time



def main():
    s = Solution()
    print("Test case from manual solution:----------------------")
    A, B, C, D, E = 1, 2, 3, 4, 5
    t1 = s.networkDelayTime([[A,B,1], [A,D,2], [B,C,2], [D,C,2], [C,E,8], [D,E,3]], 5, A)
    print("Minimum time: ", t1)

    print("\nLeetcode test cases: -------------------------")

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
