A = input()
B = list(map(int, input().split(' ')))
tmp_list = list()
for i in range(len(B)):
    tmp_num = B[i]*(i+1)
    if i == 0:
        tmp_list.append(tmp_num)
    else:
        for j in range(len(tmp_list)):
            tmp_num -= tmp_list[j]
        tmp_list.append(tmp_num)

for i in tmp_list:
    print(i, end=' ')