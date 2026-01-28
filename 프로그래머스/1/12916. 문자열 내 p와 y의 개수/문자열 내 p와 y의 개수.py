def solution(s):
    S = s.upper()
    p = 0
    y = 0
    for i in range(len(S)) :
        if S[i] == "P" :
            p += 1
        if S[i] == "Y" :
            y += 1
            
    answer = False
    if p == y :
        answer = True
    return answer