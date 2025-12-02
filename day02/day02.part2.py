import textwrap

f = None
with open("./input.txt") as content_file:
    f = content_file.read().split(",")

sum = 0
for rng in f:
    arr = rng.split("-")
    start = int(arr[0])
    end = int(arr[1])
    while start <= end:
        if start >= 10:
            id = str(start)
            for i in range((len(id) // 2), 0, -1):
                if len(id) % i != 0:
                    continue
                arr = textwrap.wrap(id, i)
                if len(arr) < 2:
                    continue
                if all(x == arr[0] for x in arr[1:]):
                    sum += int(id)
                    break
        start += 1

print(sum)