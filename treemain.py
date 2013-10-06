# -*- coding:utf-8 -*-

import solver
from copy import deepcopy
from solver import transition
from solver import evaluate_sum
from solver import possible_area
from solver import greedy_eval
from multiprocessing import Pool

N=8
ENEMYPOWER=4


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
    print "<calc start on maxroute>"

    
    for i in range(N):
        print str(i)+"/7"
        for j in range(N):
            if pos_area_me[i][j]!=1:
                continue
            myturnscore=e_func(i,j,deepcopy(table),COLOR)
            max_exturn=0
            exturnscore=0
            exturn_pos=[0,0]
            res_for_myturn=transition(deepcopy(table),i,j,COLOR)
            pos_area_enemy=possible_area(res_for_myturn,ENEMY)
            
            for k in range(N):
                for l in range(N):
                    if pos_area_enemy[k][l]!=1:
                        continue
                    exturnscore=e_func(k,l,res_for_myturn,ENEMY)
                    if max_exturn < exturnscore:
                        max_exturn=exturnscore
                        exturn_pos=[k,l]
            if step>0:
                if max_exturn>0:
                ## monotomic increase, we can improve here.
                    prediction=myturnscore-max_exturn+best_score(e_func,transition(deepcopy(res_for_myturn),exturn_pos[0],exturn_pos[1],ENEMY),COLOR,step-1)
                else:
                    prediction=myturnscore-max_exturn
            else:
                prediction=myturnscore-max_exturn
            if maxscore <prediction:
                maxscore=prediction
                maxpoint=[i,j]
    if maxscore==0:
        print "CAUTION: evaluate failed......Return greedy choice."
        maxpoint=greedy_eval(deepcopy(table),COLOR)
    return maxpoint

def best_score(e_func,table,color,step):
    """
    improveing now to parallel processing.
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
    parallel processing below
    """
    """
    p=Pool(4)
    func_args=[(myfunc,a,b) for a in range(N) for b in range(N)]
    results=p.map(argwrapper,func_args)
    """
    
    pos_area_me=possible_area(table,COLOR)
    for i in range(N):
        for j in range(N):
            if pos_area_me[i][j]!=1:
                continue
            myturnscore=e_func(i,j,deepcopy(table),COLOR)
            max_exturn=0
            exturnscore=0
            exturn_pos=[0,0]
            res_for_myturn=transition(deepcopy(table),i,j,COLOR)##
            pos_area_enemy=possible_area(deepcopy(res_for_myturn),ENEMY)
            
            for k in range(N):
                for l in range(N):
                    if pos_area_enemy[k][l]!=1:
                        continue
                    exturnscore=e_func(k,l,deepcopy(res_for_myturn),ENEMY)
                    if max_exturn < exturnscore:
                        max_exturn=exturnscore
                        exturn_pos=[k,l]
            if step>0:
                ## monotomic increase
                if max_exturn>0:
                    prediction=myturnscore-max_exturn+best_score(e_func,transition(deepcopy(res_for_myturn),exturn_pos[0],exturn_pos[1],ENEMY),COLOR,step-1)
                else:
                    prediction=myturnscore-max_exturn
            else:
                prediction=myturnscore-max_exturn
            if maxscore <prediction:
                maxscore=prediction
                maxpoint=[i,j]

            res_for_myturn=[[0]]
    return maxscore

def argwrapper(args):
    return args[0](*args[1:])


def myfunc(e_func,argtable,color,step,a,b):
     pos_area_me=possible_area(table,COLOR)
     if pos_area_me[a][b]!=1:
         pass
     myturnscore=e_func(a,b,deepcopy(table),COLOR)
     max_exturn=0
     exturnscore=0
     exturn_pos=[0,0]
     res_for_myturn=transition(deepcopy(table),a,b,COLOR)##
     pos_area_enemy=possible_area(deepcopy(res_for_myturn),ENEMY)
     
     for k in range(N):
         for l in range(N):
            if pos_area_enemy[k][l]!=1:
                continue
            exturnscore=e_func(k,l,deepcopy(res_for_myturn),ENEMY)
            if max_exturn < exturnscore:
                max_exturn=exturnscore
                exturn_pos=[k,l]
            if step>0:
                ## monotomic increase
                if max_exturn>0:
                    prediction=myturnscore-max_exturn+best_score(e_func,transition(deepcopy(res_for_myturn),exturn_pos[0],exturn_pos[1],ENEMY),COLOR,step-1)
                else:
                    prediction=myturnscore-max_exturn
            else:
                prediction=myturnscore-max_exturn
