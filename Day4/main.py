example = "example.txt"
input = "input.txt"
example2 = "example2.txt"

f = open(input, "r")
lines = f.readlines()
f.close()
ans = 0
ans2 = 0

wins = []
card_count = []

for line in lines:
    card_count.append(1)
    win_count = 0
    line = line.split(":")[1]
    winning = line.split("|")[0]
    winning = winning.split(" ")
    while "" in winning:
        winning.remove("")

    nums = line.split("|")[1]
    nums = nums.split(" ")
    nums = nums.split(" ")
    while "" in nums:
        nums.remove("")
    nums[-1] = nums[-1].replace("\n", "")

    for num in nums:
        if num in winning:
            win_count = win_count + 1

    wins.append(win_count)
    if win_count == 0:
        continue

    ans = ans + pow(2, win_count - 1)

print("Solution to part 1: " + str(ans))

for i, x in enumerate(wins):
    for a in range(card_count[i]):
        for b in range(1, wins[i] + 1):
            card_count[i + b] = card_count[i + b] + 1

for num in card_count:
    ans2 = ans2 + num


print("Solution to part 2: " + str(ans2))
