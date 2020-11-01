from rb_tree import *

def class_map(Y, C):
    n = len(Y)

    # m initialization

    rb = RedBlackTree()
    for c in C:
        rb.add(c)
    m = 0
    s = rb.__iter__()
    for i in s:
        m += 1

    mv = [[0 for j in range(10)] for i in range(m)]
    for i in range(n):
        mv[C[i]][Y[i]] += 1

    map_ = {}
    for i in range(m):
        max_ = -1
        res = -1
        for j in range(10):
            if (mv[i][j] > max_):
                max_ = mv[i][j]
                res = j
        map_[i] = res

    return [map_[C[i]] for i in range(n)]

