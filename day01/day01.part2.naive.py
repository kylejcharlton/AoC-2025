f = None
with open("./input.txt") as content_file:
    f = content_file.read().splitlines()


pos = 50
direction = 0
count = 0

for line in f:
    if line[0] == "L":
        direction = -1
    else:
        direction = 1

    num_turn = int(line[1:])
    while num_turn > 0:
        num_turn -= abs(direction)
        pos += direction
        pos %= 100
        if pos == 0:
            count += 1

print(count)