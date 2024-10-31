number = int(input())

chunks = set()
step, prev, answer = 1, 0, 3
while prev + step <= number:
    chunks.add(prev := prev + step)
    if (number - prev) in chunks:
        answer = 2
    step += 1

if number in chunks:
    answer = 1

print(answer)