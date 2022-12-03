f, points, points2 = [t.split(" ") for t in open("day2_input.txt", "r").read().splitlines()], 0, 0
reverse_win = {"A": "Y", "B": "Z", "C": "X"}
reverse_draw = {"A": "X", "B": "Y", "C": "Z"}
reverse_loose = {"A": "Z", "B": "X", "C": "Y"}
point = {"X": ("C", "A", 1), "Y": ("A", "B", 2), "Z": ("B", "C", 3)}
for i, j in f:
    if point[j][0] == i:
        points += 6 + point[j][2]
    elif point[j][1] == i:
        points += 3 + point[j][2]
    else:
        points += point[j][2]

for i, j in f:
    if j == "X":
        points2 += point[reverse_loose[i]][2]
    if j == "Y":
        points2 += 3 + point[reverse_draw[i]][2]
    if j == "Z":
        points2 += 6 + point[reverse_win[i]][2]

print(points)
print(points2)
