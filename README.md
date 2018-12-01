# Artificial Intelligence Homework - Then-Queen Problem
## Introduction
The N queens puzzle is the problem of placing eight chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. The solutions exist for all natural numbers n with the exception of n=2 and n=3.

## Environment  
* python 3.6
* packages: matplotlib, numpy, multiprocessing
* installation  
`pip install -r requirements.txt`

## Report 
### 1. 8-queen problem (n = 8) 
(a) List all the results (average #attacks in the final configuration) from the two methods.  
|Methods         |the Final Number of Attacks|  
|----------------|---------------------------|
|Hill Climbing   |1.167| 
|Geneic Algorithm|the Final Number of Attacks| 
(b) Compare the average running time for the three methods to get a solution.  
|Methods         |Average Runtime|  
|----------------|---------------------------|
|Hill Climbing   |0.224 seconds| 
|Geneic Algorithm|the Final Number of Attacks| 
(c) Compare the success rate (SR) of HC and GA.
|Methods         |Success Rate|  
|----------------|---------------------------|
|Hill Climbing   |0.1667| 
|Geneic Algorithm|the Final Number of Attacks| 
### 2. 50-queen problem (n = 50)
|Methods         |the Final Number of Attacks|  
|----------------|---------------------------|
|Hill Climbing   |3.266| 
|Geneic Algorithm|the Final Number of Attacks| 
(b) Compare the average running time for the three methods to get a solution.  
|Methods         |Average Runtime|  
|----------------|---------------------------|
|Hill Climbing   |75.884 seconds| 
|Geneic Algorithm|the Final Number of Attacks| 
(c) Compare the success rate (SR) of HC and GA.
|Methods         |Success Rate|  
|----------------|---------------------------|
|Hill Climbing   |0.0| 
|Geneic Algorithm|the Final Number of Attacks| 

## Source Code
* main.py
* problem.py
* environment.py
* ga.py
* HC.py
