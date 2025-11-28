def solution(sizes):
    w = 0
    h = 0
    for i in sizes :
        if i[0] > i[1] :
            i.sort()
        if i[0] > w :
            w = i[0]
        if i[1] > h :
            h = i[1]
    return w * h