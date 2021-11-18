
def solution(m, f):

    m = int(m)
    f = int(f)


    counter = 0

    while m > 1 and f > 1:

        # If number of Mach bombs and Facula bombs are same
        # Then, It is impossible to replicate to the desired
        # Total number of bombs

        if m % f == 0:
            return "impossible"

        else:
            counter += int(max(m, f) / min(m, f))

            temp = m
            m = max(m, f) % min(m, f)
            f = min(temp, f)

    return str(counter + max(m, f) - 1)

print(solution("4", "7"))
