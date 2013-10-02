# -*- coding:utf-8 -*-

import solver
from copy import deepcopy
from solver import transition
from solver import evaluate_sum
from solver import possible_area

N=8


def maxroute(e_func,table,color,step):
    """
    評価関数e_funcを使って、その評価値を最悪値を最大にする手を返す。
    stepの数だけ深く探索する。
    coded only for the case step is 1.
    """
    if color==1:
        ENEMY=2
    else:
        ENEMY=1
    COLOR=color
    prediction=0
    maxscore=0
    maxpoint=[0,0]
    myturnscore=0
    """
    Code below is for the case step is 1.
    """
    pos_area_me=possible_area(table,COLOR)
    for i in range(N):
        for j in range(N):
            if pos_area_me[i][j]!=1:
                continue
            myturnscore=e_func(i,j,deepcopy(table),COLOR)
            max_exturn=0
            res_for_myturn=transition(deepcopy(table),i,j,COLOR)
            pos_area_enemy=possible_area(res_for_myturn,ENEMY)
            for k in range(N):
                for l in range(N):
                    if pos_area_enemy[k][l]!=1:
                        continue
                    exturnscore=e_func(k,l,res_for_myturn,ENEMY)
                    if max_exturn > exturnscore:
                        max_exturn=exturnscore
            prediction=myturnscore-max_exturn
            if maxscore>prediction:
                maxscore=prediction
                maxpoint=[i,j]
    if maxscore==0:
        print "CAUTION: evaluate failed"

    return maxpoint

