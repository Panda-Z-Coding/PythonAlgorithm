import sys
import bisect

input = sys.stdin.read
data = input().split()


class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.tree = [None] * (4 * n)
        self.build(1, n, 1, arr)

    def build(self, l, r, rt, arr):
        self.tree[rt] = {'l': l, 'r': r, 'ma': 0, 'se': -1, 'id1': -1, 'id2': -1}
        if l == r:
            self.tree[rt]['ma'] = arr[l - 1]
            self.tree[rt]['id1'] = l
            return
        mid = (l + r) // 2
        self.build(l, mid, rt * 2, arr)
        self.build(mid + 1, r, rt * 2 + 1, arr)
        self.push_up(rt)

    def push_up(self, rt):
        vec = [
            (self.tree[rt * 2]['ma'], self.tree[rt * 2]['id1']),
            (self.tree[rt * 2]['se'], self.tree[rt * 2]['id2']),
            (self.tree[rt * 2 + 1]['ma'], self.tree[rt * 2 + 1]['id1']),
            (self.tree[rt * 2 + 1]['se'], self.tree[rt * 2 + 1]['id2'])
        ]
        vec.sort(key=lambda x: (-x[0], x[1]))
        ma, se = (-1, -1), (-1, -1)
        for i in vec:
            if i[0] > ma[0]:
                se = ma
                ma = i
            elif i[0] == ma[0]:
                continue
            elif i[0] > se[0]:
                se = i
        self.tree[rt]['ma'] = ma[0]
        self.tree[rt]['id1'] = ma[1]
        self.tree[rt]['se'] = se[0]
        self.tree[rt]['id2'] = se[1]

    def update(self, pos, val, rt):
        l, r = self.tree[rt]['l'], self.tree[rt]['r']
        if l == r:
            self.tree[rt]['ma'] = val
            self.tree[rt]['se'] = -1
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(pos, val, rt * 2)
        else:
            self.update(pos, val, rt * 2 + 1)
        self.push_up(rt)

    def query_max(self, L, R, rt):
        l, r = self.tree[rt]['l'], self.tree[rt]['r']
        if L <= l and r <= R:
            return [
                (self.tree[rt]['ma'], self.tree[rt]['id1']),
                (self.tree[rt]['se'], self.tree[rt]['id2'])
            ]
        mid = (l + r) // 2
        p1 = [(-1, -1), (-1, -1)]
        p2 = [(-1, -1), (-1, -1)]
        if L <= mid:
            p1 = self.query_max(L, R, rt * 2)
        if R > mid:
            p2 = self.query_max(L, R, rt * 2 + 1)
        vec = p1 + p2
        vec.sort(key=lambda x: (-x[0], x[1]))
        ma, se = (-1, -1), (-1, -1)
        for i in vec:
            if i[0] > ma[0]:
                se = ma
                ma = i
            elif i[0] == ma[0]:
                continue
            elif i[0] > se[0]:
                se = i
        return [ma, se]


n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:n + 2]))
b = [-2] * (n + 1)

seg_tree = SegmentTree(n, a)

for i in range(1, n + 1):
    p = seg_tree.query_max(i, min(n, i + k)
                           , 1)
    if p[0][0] == b[i - 1]:
        b[i] = p[1][0]
        seg_tree.update(p[1][1], -1, 1)
        if b[i] == -1:
            continue
        k -= abs(i - p[1][1])
    else:
        b[i] = p[0][0]
        seg_tree.update(p[0][1], -1, 1)
        if b[i] == -1:
            continue
        k -= abs(i - p[0][1])

print(' '.join(map(str, b[1:])))
