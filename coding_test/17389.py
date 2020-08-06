# 17389 문제
N = int(input())
S = list(input())

score_list = [0]*N
bonus_score = 0
total_score = 0

# for idx, i in enumerate(S):
#     if i == 'O':
#         score_list[idx] = 1

for idx, i in enumerate(score_list):
    if i == 1:
        total_score += idx+1
        total_score += bonus_score
        bonus_score += 1
    else:
        bonus_score = 0
print(total_score)