# -*- coding:utf-8 -*-

N=8 ## table size

"""
0:null
1:my spot
2:enemy spot
"""

def evaluate_sum(table,p,q):
    score=0
    #below
    score_bl=0
    vect_bl=[0,0]
    if p<N-1:
        for i in range(p+1,N):
            if table[i][q]==1:
                score_bl=0
                break
            if table[i][q]==0:
                if score_bl>0:
                    vect_bl[0]=i
                    vect_bl[1]=q
                    break
                else:
                    break
            if table[i][q]==2:
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
            if table[i][q]==1:
                score_ol=0
                break
            if table[i][q]==0:
                if score_ol>0:
                    vect_ol[0]=i
                    vect_ol[1]=q
                    break
                else:
                    break
            if table[i][q]==2:
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
            if table[p][j]==1:
                score_rc=0
                break
            if table[p][j]==0:
                if score_rc>0:
                    vect_rc[0]=p
                    vect_rc[1]=j
                    break
                else:
                    break
            if table[p][j]==2:
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
            if table[p][j]==1:
                score_lc=0
                break
            if table[p][j]==0:
                if score_lc>0:
                    vect_lc[0]=p
                    vect_lc[1]=j
                    break
                else:
                    break
            if table[i][q]==2:
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
        j=p+1
        while(i<N and j<N):
            if table[i][j]==1:
                score_se=0
                break
            if table[i][j]==0:
                if score_se>0:
                    vect_se[0]=i
                    vect_se[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_sw=0
                break
            if table[i][j]==0:
                if score_sw>0:
                    vect_sw[0]=i
                    vect_sw[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_ne=0
                break
            if table[i][j]==0:
                if score_ne==0:
                    vect_ne[0]=i
                    vect_ne[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_nw=0
                break
            if table[i][j]==0:
                if score_nw==0:
                    vect_nw[0]=i
                    vect_nw[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
        MY=1
        ENEMY=2
    else:
        MY=2
        ENEMY=1
    res=table
    #South
    line_south=[]#大きさ2の配列のリスト(座標のリスト)
    score_bl=0
    vect_bl=[0,0]
    if p<N-1:
        for i in range(p+1,N):
            if table[i][q]==ME:
                score_bl=0
                break
            if table[i][q]==0:
                if score_bl>0:
                    line_south.append([i,q])
                    break
                else:
                    break
            if table[i][q]==2:
                if i!=N-1:
                    score_bl+=1
                    line_south.append([i,q])
                else:
                    score_bl=0
                    break
    for i in range(len(line_south)):
        res[line_southx[0]][line_south[1]]=ME
    
            
    #North
    score_ol=0
    line_north=[]
    if p>0:
        for i in range(p-1,-1,-1):
            if table[i][q]==ME:
                score_ol=0
                break
            if table[i][q]==0:
                if score_ol>0:
                    line_north.append([i,q])
                    break
                else:
                    break
            if table[i][q]==ENEMY:
                if i!=N-1:
                    score_bl+=1
                    line_north.append([i,q])
                else:
                    score_bl=0
                    break
    for i in range(len(line_north)):
        res[line_north[0]][line_north[1]]=ME
    #East
    score_rc=0
    line_east=[]
    vect_rc=[0,0]
    if q<N-1:
        for j in range(q+1,N):
            if table[p][j]==1:
                score_rc=0
                break
            if table[p][j]==0:
                if score_rc>0:
                    line_east.append([p,j])
                    break
                else:
                    break
            if table[p][j]==2:
                if i!=N-1:
                    #Extend the target area here only
                    score_rc+=1
                    line_east.append([p,j])
                else:
                    score_rc=0
                    break
    for i in range(len(line_east)):
        res[line_east[0]][line_east[1]]=ME
    #West
    score_lc=0
    line_west=[]
    if q>0:
        for j in range(q-1,-1,-1):
            if table[p][j]==1:
                score_lc=0
                break
            if table[p][j]==0:
                if score_lc>0:
                    line_west.append([p,j])
                    break
                else:
                    break
            if table[i][q]==2:
                if i!=N-1:
                    score_lc+=1
                    line_west.append([p,j])
                else:
                    score_lc=0
                    break
    for i in range(len(line_west)):
        res[line_west[0]][line_west[1]]=ME
    #southeast
    score_se=0
    line_SE=[]
    i=0
    j=0
    if p<N-1 and q<N-1:
        i=p+1
        j=p+1
        while(i<N and j<N):
            if table[i][j]==1:
                score_se=0
                break
            if table[i][j]==0:
                if score_se>0:
                    vect_se[0]=i
                    vect_se[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_sw=0
                break
            if table[i][j]==0:
                if score_sw>0:
                    vect_sw[0]=i
                    vect_sw[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_ne=0
                break
            if table[i][j]==0:
                if score_ne==0:
                    vect_ne[0]=i
                    vect_ne[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
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
            if table[i][j]==1:
                score_nw=0
                break
            if table[i][j]==0:
                if score_nw==0:
                    vect_nw[0]=i
                    vect_nw[1]=j
                    break
                else:
                    break
            if table[i][j]==2:
                if i!=0 and j!=N-1:
                    score_nw+=1
                    i-=1
                    j-=1
                else:
                    score_nw=0
                    break
            
    return score_bl+score_ol+score_rc+score_lc+score_se+score_sw+score_nw+score_ne

    
    
def greedy_eval(table):
    mx=0
    s_vect=[0,0]
    for i in range(0,N):
        for j in range(0,N):
            score=evaluate_sum(table,i,j)
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
