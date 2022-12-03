import string
f = open("day3_input.txt", "r").read().splitlines()
content1 = [(t[:len(t) // 2], t[len(t) // 2:]) for t in f]
alphabet = list(string.ascii_letters)
double_types_in_both_compartments = [[x for x in i for y in j if x == y] for i, j in content1]
priorities = [alphabet.index(i[0]) + 1 for i in double_types_in_both_compartments]
content = [f[i:i+3] for i in range(0, len(f) - 2, 3)]
badges = [[x for x in i for y in j for z in k if x == y == z] for i, j, k in content]
priority2 = [alphabet.index(i[0]) + 1 for i in badges]
print(sum(priorities))
print(sum(priority2))
