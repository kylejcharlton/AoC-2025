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
    pos += direction * num_turn
    if pos % 100 == 0:
        count += 1

print(count)