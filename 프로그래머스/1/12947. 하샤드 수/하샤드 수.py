def solution(x):
    answer = True
    total = 0
    for i in range(len(str(x))) :
        total += int(str(x)[i])
    if (x % total != 0) :
        answer = False
    return answer