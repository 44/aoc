import sys

cur = 0
food = [0]
for l in sys.stdin:
    if len(l.strip()) == 0:
        food.append(0)
    else:
        food[-1] += int(l.strip())

print(sorted(food, reverse=True))
print(sum(sorted(food, reverse=True)[0:3]))
