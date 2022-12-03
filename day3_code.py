import string
f = [(t[:len(t) // 2], t[len(t) // 2:]) for t in open("day3_input.txt", "r").read().splitlines()]
alphabet = list(string.ascii_letters)
double_types_in_both_compartments = [[x for x in i for y in j if x == y] for i, j in f]
priorities = [alphabet.index(i[0]) + 1 for i in double_types_in_both_compartments]
f = open("day3_input.txt", "r").read().splitlines()
content = [f[i:i+3] for i in range(0, len(f) - 2, 3)]
badges = [[x for x in i for y in j for z in k if x == y == z] for i, j, k in content]
priority2 = [alphabet.index(i[0]) + 1 for i in badges]
print(sum(priorities))
print(sum(priority2))
