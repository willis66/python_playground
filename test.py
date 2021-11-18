
def solution(l):
    counter = [0] * len(l)
    total_count = 0

    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                counter[i] = counter[i] + 1
                total_count += counter[j]        

    return total_count
