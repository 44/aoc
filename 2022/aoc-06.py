import sys

class Reader(object):
    def __init__(self):
        self.buffer = []
        self.count = 0

    def add(self, c):
        if len(self.buffer) >= 14:
            self.buffer.pop(0)
        self.buffer.append(c)
        self.count += 1
        un = set(self.buffer)
        if len(un) == 14:
            return self.count
        return None

for l in sys.stdin:
    ls = l.strip()
    r = Reader()
    for c in ls:
        res = r.add(c)
        if not res is None:
            print(res)
            break
    break
