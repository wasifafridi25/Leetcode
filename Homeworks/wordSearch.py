class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def backtrack(i, j, word_index):
            if word_index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[word_index]:
                return False

            visited[i][j] = True

            if (backtrack(i-1, j, word_index+1) or
                backtrack(i+1, j, word_index+1) or
                backtrack(i, j-1, word_index+1) or
                backtrack(i, j+1, word_index+1)):
                return True

            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
def main():
    s = Solution()

    print("Test case 1: ")
    result1 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED')
    print(result1)

    print("Test case 2: ")
    result2 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE')
    print(result2)

    print("Test case 3: ")
    result3 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB')
    print(result3)

if __name__ == '__main__':
    main()
