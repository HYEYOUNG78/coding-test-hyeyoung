def solution(n):
    answer = [int(str(n)[::-1][i]) for i in range(len(str(n)))]
    return answer