import copy
list_alpha = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

N, M = list(map(int, input().split(' ')))
name_one, name_two = list(input().split(' '))
name_mixed = list()

same_len = 0
long_name = 0
if N > M:
    same_len = M
    long_name = 1
elif N < M:
    same_len = N
    long_name = 2
else:
    same_len = M
    long_name = 0

for i in range(same_len):
    name_mixed.append(name_one[i])
    name_mixed.append(name_two[i])

if long_name == 1:
    tmp = name_one[same_len:len(name_one)]
    for k in tmp:
        name_mixed.append(k)
elif long_name == 2:
    tmp = name_two[same_len:len(name_two)]
    for k in tmp:
        name_mixed.append(k)

num_data = list()
new_num_data = list()
tmp_data = list()

for i in range(len(name_mixed)):
    num_data.append(list_alpha[(ord(name_mixed[i]) - 65)])

while True:
    for i in range(len(num_data)):
        tmp_data.append((num_data[i]) % 10)
    for j in range(len(tmp_data) - 1):
        new_num_data.append((tmp_data[j] + tmp_data[j + 1]) % 10)
    num_data = copy.deepcopy(new_num_data)
    tmp_data = list()
    new_num_data = list()

    if len(num_data) == 2:
        break
if num_data[0] == 0:
    print('{}%'.format(num_data[1]))
else:
    print('{}{}%'.format(num_data[0],num_data[1]))