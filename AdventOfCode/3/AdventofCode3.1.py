import csv
with open('input.txt') as csvfile:
    slope = list(csv.reader(csvfile))

x=0
y=0
trees=0

width = len(slope[0][0])
height = len(slope)

while y < height:
    if slope[y][0][x] == "#":
        trees += 1

    x += 3
    y += 1

    if x >= width:
        x = x - width

print (trees)
