f = None
with open("./input.txt") as content_file:
    f = content_file.readlines()

max_joltage = 0
for line in f:
    line = line.strip()
    if line == '':
        break
    
    i = 0
    while i < len(line)-1 and len(line) > 12:
        if line[i] < line[i+1]:
            line = line[:i] + line[i+1:]
            if i > 0:
                i -= 1
        else:
            i += 1

    max_joltage += int(line[:12])

print(max_joltage)