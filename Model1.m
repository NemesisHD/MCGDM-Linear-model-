A1L=[6 4 3 6 2;5 1 4 4 5;3 6 2 7 5;4 2 5 3 4];
A1U=[9 5 5 7 4;6 3 5 6 8;5 7 4 9 6;5 4 7 4 5];
A2L=[4 5 1 4 1;2 2 6 3 5;2 3 2 3 6;4 5 3 2 5];
A2U=[5 6 3 6 3;4 3 7 5 6;5 4 3 5 8;6 8 4 4 8];
A3L=[3 4 1 2 5;4 2 5 4 4;1 4 3 5 4;3 3 5 1 3];
A3U=[4 6 3 3 6;5 4 6 5 5;3 6 4 6 5;4 5 6 2 5];
A4L=[8 4 2 3 6;4 3 7 5 5;5 7 2 3 3;2 5 7 5 2];
A4U=[9 6 3 4 8;5 4 8 7 8;6 8 4 5 4;3 6 8 6 3];
R1L=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R1U=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R2L=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R2U=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R3L=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R3U=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R4L=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
R4U=optimvar('R1L',4,5,'Type','integer',"LowerBound",1,"UpperBound",9);
%answer=Manhatten(A1L,R1L,A1U,R1U,4,5)+Manhatten(A2L,R2L,A2U,R2U,4,5)+Manhatten(A3L,R3L,A3U,R3U,4,5)+Manhatten(A4L,R4L,A4U,R4U,4,5);
matrixprob = optimproblem('Objective',Manhatten(A1L,R1L,A1U,R1U,4,5)+Manhatten(A2L,R2L,A2U,R2U,4,5)+Manhatten(A3L,R3L,A3U,R3U,4,5)+Manhatten(A4L,R4L,A4U,R4U,4,5),'ObjectiveSense',"max");
%value=Manhatten(RCL,R1L,RCU,R1U,4,5)+Manhatten(RCL,R2L,RCU,R2U,4,5)+Manhatten(RCL,R3L,RCU,R3U,4,5)+Manhatten(RCL,R4L,RCU,R4U,4,5);
matrixprob.Constraints.c1 = Manhatten(RCL,R1L,RCU,R1U,4,5)+Manhatten(RCL,R2L,RCU,R2U,4,5)+Manhatten(RCL,R3L,RCU,R3U,4,5)+Manhatten(RCL,R4L,RCU,R4U,4,5) <=  0.1;
matrixprob.Constraints.c2 = R1L<=R1U;
matrixprob.Constraints.c3 = R2L<=R2U;
matrixprob.Constraints.c4 = R3L<=R3U;
matrixprob.Constraints.c5 = R4L<=R4U;
matrixprob.Constraints.c6 = RCL ==(R1L + R2L + R3L + R4L)*0.25;
matrixprob.Constraints.c7 = RCU ==(R1U + R2U + R3U + R4U)*0.25;
problem = prob2struct(matrixprob);
[sol,fval,exitflag,output] = linprog(problem)
matrixprob.Variables
