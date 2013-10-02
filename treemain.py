# -*- coding:utf-8 -*-

import solver
from copy import deepcopy
from solver import transition

N=8


def maxroute(e_func,table,color,step):
    """
    評価関数e_funcを使って、その評価値を最悪値を最大にする手を返す。
    stepの数だけ深く探索する。
    coded only for the case step is 1.
    contains a severe bug.
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
    for i in range(N):
        for j in range(N):
            myturnscore=e_func(i,j,deepcopy(table),COLOR)
            max_exturn=0
            res_for_myturn=transition(deepcopy(table),i,j,COLOR)
            ##First you need to check if [i,j] is allowed to put the stone.
            for k in range(N):
                for l in range(N):
                    exturn=e_func(k,l,res_for_myturn,ENEMY)
                    if max_exturn > exturn:
                        max_exturn=exturn
            prediction=myturn-exturn
            if maxscore>prediction:
                maxscore=prediction
                maxpoint=[i,j]

    return maxpoint

