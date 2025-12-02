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
    
    dist_to_zero = pos if direction == -1 else 100 - pos
    if dist_to_zero == 0:
        dist_to_zero = 100
    
    if dist_to_zero <= num_turn:
        count += ((num_turn - dist_to_zero) // 100) + 1
    
    pos = (pos + (direction * num_turn)) % 100

print(count)