import numpy as np
import pulp as pl

def MaT(A,B,size):
    dm=0
    for i in range(size):
        dm=dm+abs1(A[i],B[i])
    return dm

def MaT2(A,B1,B2,B3,B4,size):
    dm=0
    for i in range(size):
        dm+=abs1(A[i],(B1[i]+B2[i]+B3[i]+B4[i])/4)
    return dm

def abs1(a,b):
    if a>=b:
        return a-b
    else:
        return b-a    


A1L=[6,4,3,6,2,5,1,4,4,5,3,6,2,7,5,4,2,5,3,4]
A1U=[9,5,5,7,4,6,3,5,6,8,5,7,4,9,6,5,4,7,4,5]
A2L=[4,5,1,4,1,2,2,6,3,5,2,3,2,3,6,4,5,3,2,5]
A2U=[5,6,3,6,3,4,3,7,5,6,5,4,3,5,8,6,8,4,4,8]
A3L=[3,4,1,2,5,4,2,5,4,4,1,4,3,5,4,3,3,5,1,3]
A3U=[4,6,3,3,6,5,4,6,5,5,3,6,4,6,5,4,5,6,2,5]
A4L=[8,4,2,3,6,4,3,7,5,5,5,7,2,3,3,2,5,7,5,2]
A4U=[9,6,3,4,8,5,4,8,7,8,6,8,4,5,4,3,6,8,6,3]
size=4*5
#print(1-(MaT2(A1L,A1L,A2L,A3L,A4L,size)+MaT2(A1U,A1U,A2U,A3U,A4U,size))/(16*size))
problem=pl.LpProblem("Model_1",pl.LpMinimize)
R1L=pl.LpVariable.dicts("R1L",list(range(size)),1,9,cat=pl.LpInteger)
R1U=pl.LpVariable.dicts("R1U",list(range(size)),1,9,cat=pl.LpInteger)
R2L=pl.LpVariable.dicts("R2L",list(range(size)),1,9,cat=pl.LpInteger)
R2U=pl.LpVariable.dicts("R2U",list(range(size)),1,9,cat=pl.LpInteger)
R3L=pl.LpVariable.dicts("R3L",list(range(size)),1,9,cat=pl.LpInteger)
R3U=pl.LpVariable.dicts("R3U",list(range(size)),1,9,cat=pl.LpInteger)
R4L=pl.LpVariable.dicts("R4L",list(range(size)),1,9,cat=pl.LpInteger)
R4U=pl.LpVariable.dicts("R4U",list(range(size)),1,9,cat=pl.LpInteger)
problem+=MaT(R1L,A1L,size)+MaT(R1U,A1U,size)+MaT(R2L,A2L,size)+MaT(R2U,A2U,size)+MaT(R3L,A3L,size)+MaT(R3U,A3U,size)+MaT(R4L,A4L,size)+MaT(R4U,A4U,size)
for i in range(size):
    problem+=R1L[i]<=R1U[i]
    problem+=R2L[i]<=R2U[i]
    problem+=R3L[i]<=R3U[i]
    problem+=R4L[i]<=R4U[i]
problem+=(MaT2(R1L,R1L,R2L,R3L,R4L,size)+MaT2(R1U,R1U,R2U,R3U,R4U,size))/(16*size)<=0.1
problem+=(MaT2(R2L,R1L,R2L,R3L,R4L,size)+MaT2(R2U,R1U,R2U,R3U,R4U,size))/(16*size)<=0.1
problem+=(MaT2(R3L,R1L,R2L,R3L,R4L,size)+MaT2(R3U,R1U,R2U,R3U,R4U,size))/(16*size)<=0.1
problem+=(MaT2(R4L,R1L,R2L,R3L,R4L,size)+MaT2(R4U,R1U,R2U,R3U,R4U,size))/(16*size)<=0.1
#print(problem)
problem.solve()
for i in range(4):
    for j in range(5):
        print(R1U[i*5+j].varValue)
#print(R1U) 

