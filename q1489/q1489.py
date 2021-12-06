import sys

# incomplete


def findCriticalAndPseudoCriticalEdges(
        n: int,
        edges):
    # cretate 2 way dict
    matrix = {}
    for i in range(n):
        matrix.update({i: {}})
    for edge in edges:
        start = edge[0]
        end = edge[1]
        weight = edge[2]
        matrix[start].update({end: weight})
        matrix[end].update({start: weight})

    # recursion from last edge in previous loop
    global min_weight
    min_weight = 100  # sys.maxsize
    global mst_list
    mst_list = [[]]

    def recurse(org, mst, weight):
        global min_weight
        for dest in matrix[org].keys():
            if dest not in mst:
                mst.append(dest)
                weight += matrix[org][dest]
                recurse(dest, mst, weight)
                if weight <= min_weight and len(mst) >= len(mst_list[-1]):
                    mst_list.append([*mst])
                    min_weight = weight
                mst.pop()
                weight -= matrix[org][dest]
    recurse(org=start, mst=[start], weight=0)


findCriticalAndPseudoCriticalEdges(n=5, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [
                                   0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]])
