Script started on Mon Dec  3 00:38:19 2018
[01;32methan@cedl1[00m:[01;34m~/Tseng/AI/N-Queen-problem[00m$ clear
[H[2J[01;32methan@cedl1[00m:[01;34m~/Tseng/AI/N-Queen-problem[00m$ htop
[?1049h[1;59r(B[m[4l[?7h[?1h=[?25l[39;49m[?1000h[39;49m(B[m[H[2J[2d  [36m1  [39m(B[0;1m[[30m               0.0%[39m](B[m    [36m4  [39m(B[0;1m[[30m               0.0%[39m](B[m   [36m7  [39m(B[0;1m[(B[0m[31m|||||||||||||100.0%[39m(B[0;1m](B[m    [36m10 [39m(B[0;1m[[30m               0.0%[39m][3;3H(B[0m[36m2  [39m(B[0;1m[[30m               0.0%[39m](B[m    [36m5  [39m(B[0;1m[[30m               0.0%[39m](B[m   [36m8  [39m(B[0;1m[[30m               0.0%[39m](B[m    [36m11 [39m(B[0;1m[(B[0m[32m|||||||||||||100.0%[39m(B[0;1m][4;3H(B[0m[36m3  [39m(B[0;1m[(B[0m[32m|||||||||||||100.0%[39m(B[0;1m](B[m    [36m6  [39m(B[0;1m[[30m               0.0%[39m](B[m   [36m9  [39m(B[0;1m[[30m               0.0%[39m](B[m    [36m12 [39m(B[0;1m[[30m               0.0%[39m][5;3H(B[0m[36mMem[39m(B[0;1m[(B[0m[32m|||[34m|||[33m||||||||||||||||||||||||||||||3.72G(B[0;1m[30m/62.8G[39m](B[m   [36mTasks: (B[0;1m[36m187(B[0m[36m, (B[0;1m[32m419(B[0m[32m thr[36m; (B[0;1m[32m3(B[0m[36m running[6;3HSwp[39m(B[0;1m[(B[0m[31m|||||||||(B[0;1m[30m                           11.4G/63.8G[39m](B[m   [36mLoad average: [39m(B[0;1m1.10 [36m1.13 (B[0m[36m1.15 [7;58HUptime: (B[0;1m[36m98 days, 08:35:58
[H[2J[01;32methan@cedl1[00m:[01;34m~/Tseng/AI/N-Queen-problem[00m$ clear[1Phtopclearscreen -r[K[1Pcd ..lear[3Plscd result/ls[Kcleard ..screen -r[4Pclear[1Phtopclear[Kpython main.py 
Problem (1): 8-queen problem (n = 8)
    Hill Climbing
	Average Runtime : 0.0062422672907511394
	Average Number of Attacks : 0.7333333333333333
	Success Rate : 0.3
Fontconfig warning: ignoring UTF-8: not a valid region tag
^CTraceback (most recent call last):
  File "main.py", line 54, in <module>
    ga.loop()
  File "/home/ethan/Tseng/AI/N-Queen-problem/ga.py", line 93, in loop
    child = self.reproduce(x, y)
  File "/home/ethan/Tseng/AI/N-Queen-problem/ga.py", line 56, in reproduce
    while x[acc] in c2[s:e+1]:
KeyboardInterrupt
[01;32methan@cedl1[00m:[01;34m~/Tseng/AI/N-Queen-problem[00m$ python main.py [Kpython main.py [Kgit pull
remote: Enumerating objects: 5, done.[K
remote: Counting objects:  20% (1/5)   [K
remote: Compressing objects: 100% (1/1)   [K
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0[K
Unpacking objects:  33% (1/3)   
From https://github.com/WeiChengTseng/N-Queen-problem
   5fd6f65..4bf23e5  master     -> origin/master
Updating 5fd6f65..4bf23e5
Fast-forward
 main.py | 2 [32m+[m[31m-[m
 1 file changed, 1 insertion(+), 1 deletion(-)
[01;32methan@cedl1[00m:[01;34m~/Tseng/AI/N-Queen-problem[00m$ git pullpython main.py 
Problem (1): 8-queen problem (n = 8)
    Hill Climbing