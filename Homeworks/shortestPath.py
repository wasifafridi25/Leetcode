import sys

class Solution:
    def networkDelayTime(self, times, n, k):
        # create a dictionary to hold the graph
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))
        
        # initialize the distance dictionary
        dist = {node: sys.maxsize for node in range(1, n+1)}
        dist[k] = 0
        
        # iterate n-1 times to find the shortest path
        for i in range(n-1):
            for u in graph:
                for v, w in graph[u]:
                    dist[v] = min(dist[v], dist[u] + w)
        
        # find the maximum distance
        max_dist = max(dist.values())
        return max_dist if max_dist < sys.maxsize else -1

def main():
    s = Solution()
    print("Test case from manual solution:")
    t1 = s.networkDelayTime([['A','B',1], ['A','D',2], ['B','C',2], ['D','C',2], ['C','E',8], ['D','E',3]], 5, 'A')
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
