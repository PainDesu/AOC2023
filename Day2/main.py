input = "input.txt"
example = "example.txt"

f = open(input, "r")
lines = f.readlines()
f.close()
ans = 0
power = 0

for line in lines:
    possible = True
    r = 0
    g = 0
    b = 0


    line = line.split(":")
    game_number = int(line[0].split(" ")[1])

    for draw in line[1].split(";"):
        for boxes in draw.split(","):
            count = int(boxes.split(" ")[1])
            if boxes.split(" ")[2].__contains__("blue"):
                if count > b:
                    b = count
            if boxes.split(" ")[2].__contains__("red"):
                if count > r:
                    r = count
            if boxes.split(" ")[2].__contains__("green"):
                if count > g:
                    g = count

            if b > 14 or r > 12 or g > 13:
                possible = False

    power = power + (r * g * b)
    if possible:
        ans = ans + game_number

print("Part 1: " + str(ans))
print("Part 2: " + str(power))
