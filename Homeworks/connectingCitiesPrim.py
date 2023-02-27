import heapq

class Solution:
    def minimumCost(self, N: int, connections: list[list[int]]) -> int:
        # Create a dictionary to map nodes to integers
        node_map = {}
        count = 1
        for a, b, c in connections:
            if a not in node_map:
                node_map[a] = count
                count += 1
            if b not in node_map:
                node_map[b] = count
                count += 1

        # Create an adjacency list to represent the graph
        graph = {i: [] for i in range(1, N+1)}
        for a, b, c in connections:
            a = node_map[a]
            b = node_map[b]
            graph[a].append((b, c))
            graph[b].append((a, c))

        # Initialize Prim's algorithm
        visited = set()
        heap = [(0, 1)]  # Starting from node 1 with a cost of 0
        total_cost = 0

        # Iterate until all nodes are visited
        while heap and len(visited) != N:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total_cost += cost
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_cost, neighbor))

        # Check if all nodes are visited
        return total_cost if len(visited) == N else -1

def main():
    s = Solution()
    print("Test case 1: ")
    min1 = s.minimumCost(3, [[1, 2, 5],[1, 3, 6],[2, 3, 1]])
    print("Minimum cost", min1)
    
    print("Test case 2: ")
    min2 = s.minimumCost(4, [[1, 2, 3],[3, 4, 4]])
    print("Minimum cost", min2)
    
    print("Test case 3")
    min3 = s.minimumCost(7, [['a', 'b', 5],['b', 'c', 4], ['a', 'c', 3], ['b', 'd', 6], ['c', 'd', 5], ['d', 'f', 6], 
                             ['d', 'e', 6], ['e', 'f', 3], ['e', 'g', 5],['f', 'g', 4],['f', 'c', 6],['b', 'e', 2]])
    print("Minimum cost", min3)

if __name__ == "__main__":
    main()
