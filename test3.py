
def solution(s):
    s = int(s)
    counter = 0

    while s > 1:
        counter += 1
        if s % 2 == 0:
            s /= 2
        elif ((s - 1) / 2) % 2 == 0 or s == 3:
            s -= 1
        else:
            s += 1
    return counter

print(solution("3"))