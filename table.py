import numpy as np
import math

class Table:

    def __init__(self, answer):
        self.numbers = answer   # 数字テーブル
        self.flags  = np.ones((9, 9, 9)) 
        
    def set_flags(self):
        # 数字テーブル　→　フラグテーブル
        for row in range(9):  
            for col in range(9):
                self.set_num(row, col, self.numbers[row, col])

    def solve(self):
        '''
        問題を解く処理
        　戻り値：解けなかったセルの数　（０なら全部解けたの意）
        　　　　　矛盾が起こったら「－１」を返す
        '''
        flags_before = np.copy(self.flags)
        while True:
            if self.fix_check() < 0:                        # 矛盾発生
                return -1   
            if np.array_equal(self.flags, flags_before):    # 進展なし－＞終了
                break
            else:                                           # 進展あり－＞継続
                flags_before = np.copy(self.flags)          

        zero_indexes = np.where(self.numbers == 0)
        return len(zero_indexes[0])

    def set_num(self, row, col, num):
        '''
        数字が確定した時の処理
        １．自分の所属するセル、行、列、ボックスのフラグをクリア（候補から外す）
        ２．自分のフラグだけ立てる
        ３．数字テーブルに確定数字を入れる
        '''
        if num != 0:
            self.flags[row, col].fill(0)            # セル
            self.flags[row, :, num - 1].fill(0)     # 行
            self.flags[:, col, num - 1].fill(0)     # 列
            i_from = math.floor(row / 3) * 3        # ボックス
            j_from = math.floor(col / 3) * 3
            for i in range(i_from, i_from + 3):
                for j in range(j_from, j_from + 3):
                    self.flags[i, j, num - 1] = 0

            self.flags[row, col, num - 1] = 1
            self.numbers[row, col] = num
            
    def fix_check(self):
        '''
        数字が確定したか調べる処理
        （セル、行、列、ボックス内で候補が１つだけになったら確定）
        '''
        for row in range(9):    # セル
            for col in range(9):
                true_indexes = np.where(self.flags[row, col] == 1)
                if len(true_indexes[0]) == 1:
                    self.set_num(row, col, true_indexes[0][0] + 1)
                elif len(true_indexes[0]) == 0:
                    return -1

        for row in range(9):    # 行
            for num_idx in range(9):
                true_indexes = np.where(self.flags[row, :, num_idx] == 1)
                if len(true_indexes[0]) == 1:
                    self.set_num(row, true_indexes[0][0], num_idx + 1)
                elif len(true_indexes[0]) == 0:
                    return -1

        for col in range(9):    # 列
            for num_idx in range(9):
                true_indexes = np.where(self.flags[:, col, num_idx] == 1)
                if len(true_indexes[0]) == 1:
                    self.set_num(true_indexes[0][0], col, num_idx + 1)
                elif len(true_indexes[0]) == 0:
                    return -1
        
        for row in range(0, 9, 3):  # ボックス
            for col in range(0, 9, 3):
                for num_idx in range(9):
                    count = 0
                    last_row = 0
                    last_col = 0
                    for i in range(row, row + 3):
                        for j in range(col, col + 3):
                            if self.flags[i, j, num_idx] == 1:
                                count += 1
                                last_row = i
                                last_col = j
                    if count == 1:
                        self.set_num(last_row, last_col, num_idx + 1)
                    elif count == 0:
                        return -1
        return 0
