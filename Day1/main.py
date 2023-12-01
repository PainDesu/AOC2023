f = open("input.txt", "r")
lines = f.readlines()
f.close()
ans = 0
dict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

for line in lines:
    for a in dict:
        line = line.replace(a, dict[a])
    first = "a"
    last = "a"
    for char in line:
        if char.isdigit():
            if first == "a":
                first = char
                continue
            last = char
    if last.isalpha():
        last = first
    num = int(first + last)
    ans = ans + num

print(ans)
