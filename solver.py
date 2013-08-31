# -*- coding:utf-8 -*-

N=8 ## table size

"""
0:null
1:my spot
2:enemy spot
"""

def evaluate_sum(table,p,q,player):
    if player==1:
        ME=1
        ENEMY=2
    else:
        ME=2
        ENEMY=1
    score=0
    #below
    score_bl=0
    vect_bl=[0,0]
    if p<N-1:
        for i in range(p+1,N):
            if table[i][q]==0:
                score_bl=0
                break
            if table[i][q]==ME:
                if score_bl>0:
                    vect_bl[0]=i
                    vect_bl[1]=q
                    break
                else:
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_bl+=1
                else:
                    score_bl=0
                    break
    #overlow
    score_ol=0
    vect_ol=[0,0]
    if p>0:
        for i in range(p-1,-1,-1):
            if table[i][q]==0:
                score_ol=0
                break
            if table[i][q]==ME:
                if score_ol>0:
                    vect_ol[0]=i
                    vect_ol[1]=q
                    break
                else:
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_bl+=1
                else:
                    score_bl=0
                    break
    #right column
    score_rc=0
    vect_rc=[0,0]
    if q<N-1:
        for j in range(q+1,N):
            if table[p][j]==0:
                score_rc=0
                break
            if table[p][j]==ME:
                if score_rc>0:
                    vect_rc[0]=p
                    vect_rc[1]=j
                    break
                else:
                    break
            if table[p][j]==ENEMY:
                if i!=N-1:
                    #Extend the target area here only
                    score_rc+=1
                else:
                    score_rc=0
                    break
    #left column
    score_lc=0
    vect_lc=[0,0]
    if q>0:
        for j in range(q-1,-1,-1):
            if table[p][j]==0:
                score_lc=0
                break
            if table[p][j]==ME:
                if score_lc>0:
                    vect_lc[0]=p
                    vect_lc[1]=j
                    break
                else:
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_lc+=1
                else:
                    score_lc=0
                    break
    #southeast
    score_se=0
    vect_se=[0,0]
    i=0
    j=0
    if p<N-1 and q<N-1:
        i=p+1
        j=q+1
        while(i<N and j<N):
            if table[i][j]==0:
                score_se=0
                break
            if table[i][j]==ME:
                if score_se>0:
                    vect_se[0]=i
                    vect_se[1]=j
                    break
                else:
                    break
            if table[i][j]==ENEMY:
                if i!=N-1 and j!=N-1:
                    score_se+=1
                    i+=1
                    j+=1
                else:
                    score_se=0
                    break
    #southwest
    score_sw=0
    vect_sw=[0,0]
    i=0
    j=0
    if p<N-1 and q>0:
        i=p+1
        j=q-1
        while(i>0 and j<N):
            if table[i][j]==0:
                score_sw=0
                break
            if table[i][j]==ME:
                if score_sw>0:
                    vect_sw[0]=i
                    vect_sw[1]=j
                    break
                else:
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_sw+=1
                    i+=1
                    j-=1
                else:
                    score_sw=0
                    break
    #northeast
    score_ne=0
    vect_ne=[0,0]
    i=0
    j=0
    if p>0 and q<N-1:
        i=p-1
        j=q+1
        while(i>0 and j<N):
            if table[i][j]==0:
                score_ne=0
                break
            if table[i][j]==ME:
                if score_ne==0:
                    vect_ne[0]=i
                    vect_ne[1]=j
                    break
                else:
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_ne+=1
                    i-=1
                    j+=1
                else:
                    score_ne=0
                    break
    #northwest
    score_nw=0
    vect_nw=[0,0]
    i=0
    j=0
    if p>0 and q>0:
        i=p-1
        j=q-1
        while(i>0 and j>0):
            if table[i][j]==0:
                score_nw=0
                break
            if table[i][j]==ME:
                if score_nw==0:
                    vect_nw[0]=i
                    vect_nw[1]=j
                    break
                else:
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_nw+=1
                    i-=1
                    j-=1
                else:
                    score_nw=0
                    break
        
    return score_bl+score_ol+score_rc+score_lc+score_se+score_sw+score_nw+score_ne

def transition(table,p,q,player):
    """
    implement the transition
    """
    if player==1:
        ME=1
        ENEMY=2
    else:
        ME=2
        ENEMY=1
        
    res=table
    res[p][q]=ME
    #South
    line_south=[]#大きさ2の配列のリスト(座標のリスト)
    score_bl=0
    vect_bl=[0,0]
    if p<N-1:
        for i in range(p+1,N):
            if table[i][q]==0:
                score_bl=0
                line_south=[]
                break
            if table[i][q]==ME:
                if score_bl>0:
                    line_south.append([i,q])
                    break
                else:
                    line_south=[]
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_bl+=1
                    line_south.append([i,q])
                else:
                    score_bl=0
                    line_south=[]
                    break

    for i in range(len(line_south)):
        res[line_south[i][0]][line_south[i][1]]=ME
    
            
    #North
    score_ol=0
    line_north=[]
    if p>0:
        for i in range(p-1,-1,-1):
            if table[i][q]==0:
                score_ol=0
                line_north=[]
                break
            if table[i][q]==ME:
                if score_ol>0:
                    line_north.append([i,q])
                    break
                else:
                    line_north=[]
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_bl+=1
                    line_north.append([i,q])
                else:
                    score_bl=0
                    line_north=[]
                    break
    for i in range(len(line_north)):
        res[line_north[i][0]][line_north[i][1]]=ME
    #East
    score_rc=0
    line_east=[]
    vect_rc=[0,0]
    if q<N-1:
        for j in range(q+1,N):
            print range(q+1,N)
            print "loop:"+str(j)
            if table[p][j]==0:
                score_rc=0
                line_east=[]
                break
            if table[p][j]==ME:
                if score_rc>0:
                    line_east.append([p,j])
                    break
                else:
                    line_east=[]
                    break
            if table[p][j]==ENEMY:
                if i!=N-1:
                    score_rc+=1
                    line_east.append([p,j])
                else:
                    score_rc=0
                    line_east=[]
                    break
    print "line_east:" + str((len(line_east)))
    for i in range(len(line_east)):
        res[line_east[i][0]][line_east[i][1]]=ME
    #West
    score_lc=0
    line_west=[]
    if q>0:
        for j in range(q-1,-1,-1):
            if table[p][j]==0:
                score_lc=0
                line_west=[]
                break
            if table[p][j]==ME:
                if score_lc>0:
                    line_west.append([p,j])
                    break
                else:
                    line_west=[]
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_lc+=1
                    line_west.append([p,j])
                else:
                    line_west=[]
                    score_lc=0
                    break
    for i in range(len(line_west)):
        res[line_west[i][0]][line_west[i][1]]=ME
    #southeast
    score_se=0
    line_SE=[]
    i=0
    j=0
    if p<N-1 and q<N-1:
        i=p+1
        j=q+1
        while(i<N and j<N):
            if table[i][j]==0:
                score_se=0
                line_SE=[]
                break
            if table[i][j]==ME:
                if score_se>0:
                    line_SE.append([i,j])
                    break
                else:
                    line_SE=[]
                    break
            if table[i][j]==ENEMY:
                if i!=N-1 and j!=N-1:
                    score_se+=1
                    line_SE.append([i,j])
                    i+=1
                    j+=1
                else:
                    line_SE=[]
                    score_se=0
                    break
    for i in range(len(line_SE)):
        print "line_SE"+str(line_SE)
        res[line_SE[i][0]][line_SE[i][1]]=ME
    #southwest
    score_sw=0
    line_SW=[]
    i=0
    j=0
    if p<N-1 and q>0:
        i=p+1
        j=q-1
        while(i>0 and j<N):
            if table[i][j]==0:
                score_sw=0
                line_SW=[]
                break
            if table[i][j]==ME:
                if score_sw>0:
                    line_SW.append([i,j])
                    break
                else:
                    line_SW=[]
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_sw+=1
                    line_SW.append([i,j])
                    i+=1
                    j-=1
                else:
                    line_SW=[]
                    score_sw=0
                    break
    for i in range(len(line_SW)):
        res[line_SW[i][0]][line_SW[i][1]]=ME
    #northeast
    score_ne=0
    line_NE=[]
    i=0
    j=0
    if p>0 and q<N-1:
        i=p-1
        j=q+1
        while(i>0 and j<N):
            if table[i][j]==0:
                score_ne=0
                line_NE=[]
                break
            if table[i][j]==ME:
                if score_ne==0:
                    line_NE.append([i,j])
                    break
                else:
                    line_NE=[]
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_ne+=1
                    line_NE.append([i,j])
                    i-=1
                    j+=1
                else:
                    score_ne=0
                    line_NE=[]
                    break
    for i in range(len(line_NE)):
        res[line_NE[i][0]][line_NE[i][1]]=ME
    #northwest
    score_nw=0
    line_NW=[]
    i=0
    j=0
    if p>0 and q>0:
        i=p-1
        j=q-1
        while(i>0 and j>0):
            if table[i][j]==0:
                score_nw=0
                line_NW=[]
                break
            if table[i][j]==ME:
                if score_nw==0:
                    line_NW.append([i,j])
                    break
                else:
                    break
            if table[i][j]==ENEMY:
                if i!=0 and j!=N-1:
                    score_nw+=1
                    line_NW.append([i,j])
                    i-=1
                    j-=1
                else:
                    score_nw=0
                    break
    for i in range(len(line_NW)):
        res[line_NW[i][0]][line_NW[i][1]]=ME
    return res

    
    
def greedy_eval(table):
    mx=0
    s_vect=[0,0]
    for i in range(0,N):
        for j in range(0,N):
            score=evaluate_sum(table,i,j,1)
            if score > mx:
                mx=score
                s_vect[0]=i
                s_vect[1]=j
    return s_vect

def greedy_turn(table):
    mx=0
    s_vect=[0,0]
    for i in range(0,N):
        for j in range(0,N):
            score_us=evaluate_sum(table,i,j,ME)
            epi_table=transition(table,p,q,ME)
            my=0
            for k in range(0,N):
                for l in range(0,N):
                    score_against=evaluate_sum(table,k,l,ENEMY)
                    if score_against > my:
                        my=score_against
                        #ここでvectを記録してもよい
            if (score_us-score_against)>mx:
                mx=score_us-score_against
                s_vect[0]=i
                s_vect[1]=j
    return s_vect


def judge_constant(table,p,q,color):
    """
    return whether the candidate is constant
    """
    ME=color
    if color==1:
        ENEMY=2
    else:
        ENEMY=1
    #South-North
    score_SN=0
    enemy_left=0
    enemy_right=0
    res_SN=0
    if p<N-1:
        for i in range(p+1,N):
            if table[i][q]==0:
                enemy_left=0
                break
            if table[i][q]==ME:
                if j<N-1:
                    continue
                else:
                    res_SN=1
                    break
            if table[i][q]==ENEMY:
                enemy_left=-1
                break

    else:
        res_SN=1
    #North
    if res_SN!=1:
        if p>0:
            for i in range(p-1,-1,-1):
                if table[i][q]==0:
                    enemy_right=0
                    break
                if table[i][q]==ME:
                    if i>0:
                        continue
                    else:
                        res_SN=1
                if table[i][q]==ENEMY:
                    enemy_right=-1
                    break

        else:
            res_SN=1
    if res_SN!=1:
        res_SN=enemy_left*enemy_right

    #East-West
    enemy_left=0
    enemy_right=0
    res_EW=0
    #East
    if q<N-1:
        for j in range(q+1,N):
            if table[p][j]==0:
                enemy_left=0
                break
            if table[p][j]==ME:
                if j<N-1:
                    continue
                else:
                    res_EW=1
                    break
            if table[p][j]==ENEMY:
                enemy_left=-1
                break
    else:
        res_EW=1
    #West
    if q>0:
        for j in range(q-1,-1,-1):
            if table[p][j]==0:
                enemy_right=0
                break
            if table[p][j]==ME:
                if j>0:
                    continue
                else:
                    res_EW=1
                    break
            if table[i][q]==ENEMY:
                enemy_right=-1
                break
    else:
        res_EW=1

    if res_EW!=1:
        res_EW=enemy_left*enemy_right

    #Southeast-Northwest
    enemy_left=0
    enemy_right=0
    res_SENW=0
    #Southeast
    i=0
    j=0
    if p<N-1 and q<N-1:
        i=p+1
        j=q+1
        while(i<N and j<N):
            if table[i][j]==0:
                enemy_left=0
                break
            if table[i][j]==ME:
                if i<N-1 and j<N-1:
                    i+=1
                    j+=1
                    continue
                else:
                    res_EW=1
                    break
            if table[i][j]==ENEMY:
                enemy_left=-1
                break
    else:
        res_SENW=1
    #northwest
    i=0
    j=0
    if p>0 and q>0:
        i=p-1
        j=q-1
        while(i>=0 and j>=0):
            if table[i][j]==0:
                enemy_right=0
                break
            if table[i][j]==ME:
                if i>0 and j>0:
                    i-=1
                    j-=1
                    continue
                else:
                    res_SENW=1
                    break
            if table[i][j]==ENEMY:
                enemy_right=-1
                break
    else:
        res_SENW=1
    if res_SENW!=1:
        res_SENW=enemy_left*enemy_right

    #Southwest-Northeast
    enemy_left=0
    enemy_right=0
    res_SWNE=0
    #southwest
    i=0
    j=0
    if p<N-1 and q>0:
        i=p+1
        j=q-1
        while(i<N and j>=0):
            if table[i][j]==0:
                enemy_left=0
                break
            if table[i][j]==ME:
                if i<N-1 and j>0:
                    i+=1
                    j-=1
                    continue
                else:
                    res_SWNE=1
                    break
            if table[i][j]==ENEMY:
                enemy_left=-1
                break
    else:
        res_SWNE=1
    #northeast
    i=0
    j=0
    if p>0 and q<N-1:
        i=p-1
        j=q+1
        while(i>=0 and j<N):
            if table[i][j]==0:
                enemy_right=0
                break
            if table[i][j]==ME:
                if i>0 and j<N-1:
                    i-=1
                    j+=1
                    continue
                else:
                    res_SWNE=1
                    break
            if table[i][j]==ENEMY:
                enemy_right=-1
                break
    else:
        res_SWNE=1
    if res_SWNE!=1:
        res_SWNE=enemy_left*enemy_right

    #Total
    return res_SN*res_EW*res_SENW*res_SWNE

def maximum_constant(table,color):
    
