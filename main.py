#coding: UTF-8
#　＜ＫＡＩＤＯＫＵ＞
#　数独パズルを解くやつ

import numpy as np
import table as tbl
import utils as utl
import json

def main(json_number):
    # 問題をｊｓｏｎで読み込み
    json_path = './Level_' + str(json_number) + '.json'
    question = utl.ReadJson(json_path).question
    answer = np.array(question)
    # ヒントの数字が少な過ぎのとき
    if len(np.where(answer > 0)[0]) < 10:
        return 'ヒントが少なすぎですよ', answer
    main_table = tbl.Table(answer)
    main_table.set_flags()
    ret =  main_table.solve()
    if ret == 0:
        return 'できましたよ (level-' + str(json_number) + ')', answer
    elif ret == -1:
        return '問題が間違ってますよ (level-' + str(json_number) + ')', answer
    
    ret = Virtual(answer, main_table.flags, 'more') 
    if ret[0] == 0:
        return 'できましたよ (level-' + str(json_number) + ')', ret[1]
    else:
        return '難しくて解けないです (level-' + str(json_number) + ')', 0


def Virtual(answer, flags, flg_more):
    '''
    仮置きロジック　再帰呼び出しで仮仮までやる
    '''
    init_answer = np.copy(answer)
    init_flags  = np.copy(flags)
    v_table = tbl.Table(np.copy(init_answer))
    v_table.flags = np.copy(init_flags)

    while True:     # 「進展なし」になるまで回し続ける
        flags_before = np.copy(v_table.flags)  
        for i in range(2, 9):       #候補が少ないセルから仮置きしてみる
            for row in range(9):
                for col in range(9):
                    indexes = np.where(v_table.flags[row, col] == 1)            
                    if len(indexes[0]) == i:
                        for j in range(i):
                            v_table.numbers = np.copy(init_answer)
                            v_table.flags = np.copy(init_flags)
                            v_table.set_num(row, col, indexes[0][j] + 1)
                            v_ret = v_table.solve()
                            
                            if v_ret == 0: 
                                return 0, v_table.numbers
                            
                            elif v_ret == -1:   # 矛盾してたら候補から外す
                                init_flags[row, col, indexes[0][j]] = 0

                            else:   # 仮仮ロジック（再帰呼び出し）
                                if flg_more == 'more':
                                    vv_ret = Virtual(v_table.numbers, v_table.flags, ' ') 
                                    if vv_ret[0] == 0:
                                        return vv_ret

        if np.array_equal(v_table.flags, flags_before):
            return 1, v_table.numbers

#ret = main()
#print(ret)
