print(max([sum([int(i) for i in calorie1.split("\n") if type(i) == int or i.isdigit()]) for calorie1 in open("day1_input.txt", "r").read().split("\n\n")]))
