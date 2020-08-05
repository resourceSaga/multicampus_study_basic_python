N = int(input())
S = list(input())

score_list = [0]*N
bonus_list = 0

print(N)
print(type(N))
print(S)
print(type(S))

for i in S:
    if i == 'O':
        score_list[i] = 1

