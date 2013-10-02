# -*- coding:utf-8 -*-

import solver
from copy import deepcopy

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
    myturn=0
    """
    Code below is for the case step is 1.
    """
    for i in range(N):
        for j in range(N):
            myturn=e_func(i,j,table,COLOR)
            max_exturn=0
            for k in range(N):
                for l in range(N):
                    exturn=e_func(i,j,table,ENEMY)
                    if max_exturn > exturn:
                        max_exturn=exturn
            prediction=myturn-exturn
            if maxscore>prediction:
                maxscore=prediction
                maxpoint=[i,j]

    return maxpoint

    
    
