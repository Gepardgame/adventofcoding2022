f = open("day4_input.txt", "r").read().splitlines()
content = [[j.split("-") for j in i.split(",")] for i in f]
content = [[[int(i[0][0]), int(i[0][1])], [int(i[1][0]), int(i[1][1])]] for i in content]
contain_each_other = [1 if 1 in [1 if i[1] == j[1] else [1 if j[0] == i[0] else [[1 if i[0] < j[0] else 0][0] if i[1] > j[1] else [1 if i[0] > j[0] else 0][0]][0]][0]] else 0 for i, j in content]
contain_other = [1 if 1 in [1 if z in range(i[0], i[1] + 1) else 0 for z in range(j[0], j[1] + 1)] else 0 for i, j in content]
print(sum(contain_each_other))
print(sum(contain_other))

"""
Code, if you wrote line 4 not in one line:
for i, j in content:
    if i[1] == j[1]:
        contain_each_other.append(1)
    elif j[0] == i[0]:
        contain_each_other.append(1)
    elif i[1] > j[1]:
        if i[0] < j[0]:
            contain_each_other.append(1)
        else:
            contain_each_other.append(0)
    elif i[0] > j[0]:
        contain_each_other.append(1)
    else:
        contain_each_other.append(0)
"""