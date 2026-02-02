def solution(brown, yellow):
    n = brown + yellow
    for h in range(1, int(n**0.5 + 1)) :
        if n % h == 0 :
            w = n // h
            if (w - 2) * (h - 2) == yellow :
                return [w, h]