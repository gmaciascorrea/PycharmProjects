class Solution:
    def __init__(self, board):
        self.board = board

    def is_valid_sudoku(self, board) -> bool:

        N = 9
        for r in range(N):
            row = [c for c in board[r] if c != '.']
            if len(row) != len(set(row)):
                return False

        for c in range(N):
            col = [board[r][c] for r in range(N) if board[r][c] != '.']
            if len(col) != len(set(col)):
                return False

        def helper(R, C):
            l = set()
            for r in range(R, R + 3):
                for c in range(C, C + 3):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] not in l:
                        l.add(board[r][c])
                    else:
                        return False

        for r in range(0, N, 3):
            for c in range(0, N, 3):
                if not helper(r, c):
                    return False

        return True


sample = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

a = Solution(sample).is_valid_sudoku(sample)
print(a)
if a:
    print('Válido')
else:
    print('Não válido')
