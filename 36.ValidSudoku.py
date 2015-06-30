__author__ = 'amow'
class Solution:
    # @param {character[][]} board
    # @return {boolean}

    def valid_arr(self, arr):
        tmp = filter(lambda x: x != ".", arr)
        return len(tmp) == len(set(tmp))

    def isValidSudoku(self, board):
        for i in range(9):
            if not (self.valid_arr(board[i])
                and self.valid_arr(map(lambda x:x[i], board))
                and self.valid_arr("".join(map( lambda x: "".join(x[(i%3)*3 : (i%3)*3 + 3]) ,
                    board[i/3*3 : i/3*3 + 3])))):
                return False
        return True