# 17095 _ Min-Max Subsequence
import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split())) # 1 1 2 3 3

min_num, max_num = min(l), max(l)
min_l, max_l = list(), list()
min_l = [i for i, val in enumerate(l) if val == min_num]
max_l = [i for i, val in enumerate(l) if val == max_num]
print(min_l, max_l)
ans = 100000
for i in min_l:
    for j in max_l:
        ans = min(abs(j-i), ans)
print(ans+1)