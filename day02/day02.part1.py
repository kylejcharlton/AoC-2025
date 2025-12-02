f = None
with open("./input.txt") as content_file:
    f = content_file.read().split(",")

sum = 0
for rng in f:
    arr = rng.split("-")
    start = int(arr[0])
    end = int(arr[1])
    while start <= end:
        id = str(start)
        if id[:int((len(id)/2))] == id[int((len(id)/2)):]:
            sum += int(id)
            # print(id)
        start += 1

print(sum)