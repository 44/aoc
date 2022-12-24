import sys

current = ('unknown')
files = dict()
for ls in sys.stdin:
    l = ls.strip()
    if l.startswith('$'):
        cmd = l[2:]
        # print('cmd:', cmd)
        if cmd.startswith('cd '):
            d = cmd[3:]
            # print('cd', d)
            if d == '/':
                # print('go to root')
                current = ()
            elif d == '..':
                # print('go up')
                current = current[:-1]
            else:
                # print('go down', d)
                current = current + (d,)
        elif cmd == 'ls':
            pass
            # print('Listing', current)
    else:
        import re
        fre = re.compile(r'^(\d+) (.*)$')
        m = fre.match(l)
        if m:
            sz = int(m.group(1))
            files[ (current) + (m.group(2),)] = sz
        pass

from collections import defaultdict

dirs = defaultdict(int)
for i in files.keys():
    d = (i[:-1])
    for j in range(len(d)):
        fd = "/" + "/".join(i[0:j+1])
        dirs[fd] += files[i]
    dirs['/'] += files[i]
        #print('Adding', files[i], 'to', fd)

total = 0
for d in dirs.keys():
    s = dirs[d]
    if s <= 100000:
        print(d, s)
        total += s

print(total)

fs_size = 70000000
required = 30000000
fs_used = sum(files.values())
fs_to_free = required - (fs_size - fs_used)
print('Occupied:', fs_used, 'free:', (fs_size - fs_used), 'need_to_free:', required - (fs_size - fs_used))
print('/', dirs['/'])

by_size = sorted(dirs.values())
for d in by_size:
    if d > fs_to_free:
        print(d)
