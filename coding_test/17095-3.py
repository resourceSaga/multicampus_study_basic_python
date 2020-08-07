N = input()
A = list(map(int, input().split(' ')))

min_num = min(A)
max_num = max(A)
min_num_list = [i for i, x in enumerate(A) if x == min_num]
max_num_list = [i for i, x in enumerate(A) if x == max_num]

min_index_1 = min_num_list.pop()
min_num_list.reverse()
min_index_2 = min_num_list.pop()
max_index_1 = max_num_list.pop()
max_num_list.reverse()
max_index_2 = max_num_list.pop()

result = [abs(min_index_1-max_index_1),abs(min_index_1-max_index_2),abs(min_index_2-max_index_1),abs(min_index_2-max_index_2)]
result_min = min(result) +1
print(result_min)