f = open("input.txt", "r")
lines = f.readlines()
f.close()
ans = 0

for line in lines:
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
