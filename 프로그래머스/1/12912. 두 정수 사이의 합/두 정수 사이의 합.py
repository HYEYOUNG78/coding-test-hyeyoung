def solution(a, b):
    if a > b :
        temp = a
        a = b
        b = temp
    answer = sum(range(a,b+1))
    return answer