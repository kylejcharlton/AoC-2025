f = None
with open("./input.txt") as content_file:
    f = content_file.readlines()

def find_max(str):
    m = -1
    pos = -1

    for i in range(len(str)):
        val = int(str[i])
        if val > m:
            m = val
            pos = i

    return { 'max': m, 'pos': pos }


max_joltage = 0
for line in f:
    line = line.strip()
    if line == '':
        break
    
    out1 = find_max(line[:-1])
    out2 = find_max(line[out1['pos']+1:])

    max_joltage += int(f'{out1['max']}{out2['max']}')

print(max_joltage)