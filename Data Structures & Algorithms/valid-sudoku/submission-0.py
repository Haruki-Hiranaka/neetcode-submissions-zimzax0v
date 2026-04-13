class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(i, j)
        judge_row = defaultdict(int)
        judge_colum = defaultdict(int)
        judge_subbox0_0 = defaultdict(int)
        judge_subbox0_1 = defaultdict(int)
        judge_subbox0_2 = defaultdict(int)
        judge_subbox1_0 = defaultdict(int)
        judge_subbox1_1 = defaultdict(int)
        judge_subbox1_2 = defaultdict(int)
        judge_subbox2_0 = defaultdict(int)
        judge_subbox2_1 = defaultdict(int)
        judge_subbox2_2 = defaultdict(int)
        for i in range(9):
            judge_row = defaultdict(int)
            judge_colum = defaultdict(int)
            for j in range(9):
                if board[i][j] != ".":
                    judge_row[board[i][j]] += 1#行被り
                    if judge_row[board[i][j]] > 1:
                        return False

                    if i // 3 == 0 and j // 3 == 0:
                        judge_subbox0_0[board[i][j]] += 1
                        if judge_subbox0_0[board[i][j]] > 1:
                            return False
                    elif i // 3 == 0 and j // 3 == 1:
                        judge_subbox0_1[board[i][j]] += 1
                        if judge_subbox0_1[board[i][j]] > 1:
                            return False
                    elif i // 3 == 0 and j // 3 == 2:
                        judge_subbox0_2[board[i][j]] += 1
                        if judge_subbox0_2[board[i][j]] > 1:
                            return False
                    elif i // 3 == 1 and j // 3 == 0:
                        judge_subbox1_0[board[i][j]] += 1
                        if judge_subbox1_0[board[i][j]] > 1:
                            return False
                    elif i // 3 == 1 and j // 3 == 1:
                        judge_subbox1_1[board[i][j]] += 1
                        if judge_subbox1_1[board[i][j]] > 1:
                            return False
                    elif i // 3 == 1 and j // 3 == 2:
                        judge_subbox1_2[board[i][j]] += 1
                        if judge_subbox1_2[board[i][j]] > 1:
                            return False
                    elif i // 3 == 2 and j // 3 == 0:
                        judge_subbox2_0[board[i][j]] += 1
                        if judge_subbox2_0[board[i][j]] > 1:
                            return False
                    elif i // 3 == 2 and j // 3 == 1:
                        judge_subbox2_1[board[i][j]] += 1
                        if judge_subbox2_1[board[i][j]] > 1:
                            return False
                    elif i // 3 == 2 and j // 3 == 2:
                        judge_subbox2_2[board[i][j]] += 1
                        if judge_subbox2_2[board[i][j]] > 1:
                            return False
                if board[j][i] != ".":
                    judge_colum[board[j][i]] += 1#列被り
                    if judge_colum[board[j][i]] > 1:
                        return False
        else:
            return True
        






        