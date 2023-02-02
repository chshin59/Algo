def solution(a, b):
    answer = 0
    if a == b:
        return a
    
    avg = (a + b)/2
    count = b-a
    if count < 0:
        count = -count
    count += 1
    
    answer = avg * count
    
    return answer