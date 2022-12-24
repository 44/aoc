import sys
overlapping = 0
partially = 0
for l in sys.stdin:
    p = l.strip().split(',')
    g1 = [int(x) for x in p[0].split('-')]
    g2 = [int(x) for x in p[1].split('-')]
    overlap = False
    part = False
    if g1[0] <= g2[0] and g1[1] >= g2[1]:
        overlap = True
    elif g2[0] <= g1[0] and g2[1] >= g1[1]:
        overlap = True
    if overlap:
        overlapping += 1
        partially += 1
    else:
        if g1[0] >= g2[0] and g1[0] <= g2[1]:
            partially += 1
            part = True
        elif g1[1] >= g2[0] and g1[1] <= g2[1]:
            partially += 1
            part = True
        elif g2[0] >= g1[0] and g2[0] <= g1[1]:
            partially += 1
            part = True
        elif g2[1] >= g1[0] and g2[1] <= g1[1]:
            partially += 1
            part = True

    print(p, overlap, part)
print(overlapping, partially)

