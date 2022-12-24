import sys

def prio(tag):
    if tag >= 'a' and tag <='z':
        return ord(tag) - ord('a') + 1
    if tag >= 'A' and tag <='Z':
        return ord(tag) - ord('A') + 1 + 26

total = 0
group = []
group_total = 0
for l in sys.stdin:
    ls = l.strip()
    el = int((len(ls))/2)
    left = l[0:el]
    right = l[el:-1]
    common = list(set(left).intersection(set(right)))
    weight = 0
    if len(common) > 0:
        weight = prio(common[0])
    total += weight
    print(ls, left, right, common, weight, weight)
    if len(group) == 2:
        group.append(ls)
        badge = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        group_total += prio(list(badge)[0])
        print("GROUP", badge, prio(list(badge)[0]), group_total)
        group=[]
    else:
        group.append(ls)


print(total)
print(group_total)
# pqgZZSZgcZJqpz
# BbqTbbLjBDBLhB

# bdgHbZJHgMHgJg
# JctDtVssVcpFtq
