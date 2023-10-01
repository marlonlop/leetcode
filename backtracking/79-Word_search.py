class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def backtrack(r, c, charI):
            if charI == len(word):
                return True
            # checking all cases where it be false
            if  (r < 0 # neg r
                or c < 0
                or r >= rows #ind over bound
                or c >= cols
                or word[charI] != board[r][c] #char not in current path coordinate
                or (r, c) in seen): #current path has already been seen in current path
                return False
            
            seen.add((r, c)) #adding curr coordinate to avoid in backtracks below
            # checking all possble paths for currretn coordinate 
            result = (backtrack(r + 1, c, charI + 1) #down
                    or backtrack(r - 1, c, charI + 1) #up
                    or backtrack(r, c + 1, charI + 1) #right
                    or backtrack(r, c - 1, charI + 1)) #left
            
            # removing to make ready for checking from next matrix position
            seen.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False

        '''
        time O(m*n*4^w) w is word length
        space  O(w) w is word length
        '''