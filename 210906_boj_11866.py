n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]
sequence = []

index = 0
count = 1

while queue:
    if count != k:
        count += 1
        index += 1
        if index >= len(queue):
            index = 0
    else:
        count = 1
        sequence.append(queue.pop(index))
        if index >= len(queue):
            index = 0

print('<', end = "")
for i in range(n):
    print(sequence[i], end = "")
    if i != (n - 1):
        print(", ", end = "")
print(">")