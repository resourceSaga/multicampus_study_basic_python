# 수열의 길이 N
N = input()
# 수열 A
A = list(map(int, input().split(' ')))
# 결과 리스트, 부분 리스트의 리스트
result_list, tmp = list(), list()
# 이전 수 체크용
front_num = -1
# 최댓값-최솟값 리스트
max_min_calc = list()

for idx, i in enumerate(A):
    if idx == 0:
        tmp.append(i)
        front_num = i
    elif front_num == i-1:
        tmp.append(i)
        front_num = i        
    else:
        result_list.append(tmp)
        tmp = [i]
        front_num = i               

    if idx == len(A)-1: 
        result_list.append(tmp)

max_min_calc = [(lambda i: max(i)-min(i))(i) for i in result_list]

calc_max_num = max(max_min_calc)
calc_idx_list = [i for i, x in enumerate(max_min_calc) if x == calc_max_num]

result = 100000
for i in calc_idx_list:
    if len(result_list[i]) <= result:
        result = len(result_list[i])

print(result)