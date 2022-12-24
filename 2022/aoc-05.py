import sys
stacks = []
for i in range(9):
    stacks.append([])
state = 'stacks'
import re
cmd = re.compile(r'move (\d+) from (\d+) to (\d+)')
for line in sys.stdin:
    l = line.strip() + ' '
    if state == 'stacks':
        if not '[' in line:
            state = 'stack_ids'
            continue
        crates = [l[i:i+4] for i in range(0, len(l), 4)]
        for i in range(len(crates)):
            if crates[i][0] == '[':
                stacks[i].insert(0, crates[i][1])
    elif state == 'stack_ids':
        print(stacks)
        state = 'command'
        continue
    else:
        m = cmd.match(l)
        if not m:
            print('Incorrect format:', l)
        else:
            num = int(m.group(1))
            source = int(m.group(2)) - 1
            target = int(m.group(3)) - 1
            print(l, ':', source, '->', target, '*', num)
            before = str(stacks[source]) + " & " + str(stacks[target])
            tmp = []
            for i in range(num):
                crate = stacks[source].pop()
                tmp.insert(0, crate)
            stacks[target] += tmp
            after = str(stacks[source]) + " & " + str(stacks[target])
            print(before, '->', after)

print(stacks)
result = ''
for s in stacks:
    result += s[-1]
print(result)
