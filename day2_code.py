f, points = [t.split(" ") for t in open("day2_input.txt", "r").read().split("\n")], 0
point = {"X": ("C", "A", 1), "Y": ("A", "B", 2), "Z": ("B", "C", 3)}
for i, j in f:
    if point[j][0] == i:
        points += 6 + point[j][2]
    elif point[j][1] == i:
        points += 3 + point[j][2]
    else:
        points += point[j][2]
print(points)
