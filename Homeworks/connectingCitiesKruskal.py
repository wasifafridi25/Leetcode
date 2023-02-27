# class Solution:
#     def minimumCost(self, N: int, connections: list[list[int]]) -> int:
#         # Define a helper function to find the parent of a node in the union-find data structure
#         def find(parents, i):
#             if parents[i] != i:
#                 parents[i] = find(parents, parents[i])
#             return parents[i]

#         # Create a union-find data structure to track connected components
#         parents = list(range(N+1))

#         # Define a helper function to union two nodes in the union-find data structure
#         def union(x, y):
#             parents[find(parents, x)] = find(parents, y)

#         # Sort the connections by cost in non-descending order
#         connections.sort(key=lambda x: x[2])

#         # Initialize Kruskal's algorithm
#         total_cost = 0
#         for a, b, c in connections:
#             if find(parents, a) != find(parents, b):
#                 union(a, b)
#                 total_cost += c

#         # Check if all cities are connected
#         return total_cost if len(set(find(parents, i) for i in range(1, N+1))) == 1 else -1


# def main():
#     s = Solution()
#     print("Test case 1: ")
#     min1 = s.minimumCost(3, [[1, 2, 5],[1, 3, 6],[2, 3, 1]])
#     print("Minimum cost:", min1)
    
#     print("Test case 2: ")
#     min2 = s.minimumCost(4, [[1, 2, 3],[3, 4, 4]])
#     print("Minimum cost:", min2)
    
#     print("Test case 3: ")
#     min3 = s.minimumCost(7, [[1, 2, 5], [2, 3, 4], [1, 3, 3], [2, 4, 6], [3, 4, 5], [4, 6, 6], [4, 5, 6], [5, 6, 3], [5, 7, 5], [6, 7, 4], [6, 3, 6], [2, 5, 2]])
#     print("Minimum cost:", min3)
    
# if __name__ == "__main__":
#     main()      

class Solution:
    def minimumCost(self, N: int, connections: list[list[int]]) -> int:
        # Define a helper function to find the parent of a node in the union-find data structure
        def find(parents, i):
            if parents[i] != i:
                parents[i] = find(parents, parents[i])
            return parents[i]

        # Create a union-find data structure to track connected components
        parents = list(range(N+1))

        # Define a helper function to union two nodes in the union-find data structure
        def union(x, y):
            parents[find(parents, x)] = find(parents, y)

        # Sort the connections by cost in non-descending order
        connections.sort(key=lambda x: x[2])

        # Initialize Kruskal's algorithm
        total_cost = 0
        for a, b, c in connections:
            if find(parents, a) != find(parents, b):
                union(a, b)
                total_cost += c

        # Check if all cities are connected
        return total_cost if len(set(find(parents, i) for i in range(1, N+1))) == 1 else -1

def main():
    s = Solution()
    print("Test case 1: ")
    min1 = s.minimumCost(3, [[1, 2, 5],[1, 3, 6],[2, 3, 1]])
    print("Minimum cost:", min1)
    
    print("Test case 2: ")
    min2 = s.minimumCost(4, [[1, 2, 3],[3, 4, 4]])
    print("Minimum cost:", min2)
    
    print("Test case 3: ")
    min3 = s.minimumCost(7, [[1, 2, 5], [2, 3, 4], [1, 3, 3], [2, 4, 6], [3, 4, 5], [4, 6, 6], [4, 5, 6], [5, 6, 3], [5, 7, 5], [6, 7, 4], [6, 3, 6], [2, 5, 2]])
    print("Minimum cost:", min3)
    
if __name__ == "__main__":
    main()      
