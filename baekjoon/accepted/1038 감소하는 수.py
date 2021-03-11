def solution(N):
    if N == 0:
        return 0

    digit_indx = 0
    val = 0
    mags = {}
    while True:
        this_digit = get_pos_v(val, digit_indx)
        mag = mags[digit_indx] if digit_indx in mags else 10 ** digit_indx

        if digit_indx < len(str(val)) - 1:
            high_digit = get_pos_v(val, digit_indx + 1)
            if this_digit < high_digit - 1:
                val = val - (val % mag) + mag
                digit_indx = 0
                if is_acending(val):
                    N -= 1
            else:
                digit_indx += 1
        else:
            if this_digit < 9:
                val = (this_digit + 1) * mag
            else:
                val = 10 ** (digit_indx + 1)
            digit_indx = 0
            if is_acending(val):
                N -= 1

        if 9876543210 < val:
            return -1
        if N == 0:
            break
    return val


def is_acending(val):
    prev = 10
    for i in str(val):
        if int(i) < prev:
            prev = int(i)
        else:
            break
    else:
        return True
    return False


def get_pos_v(v, i):
    return v // (10 ** i) % 10


print(solution(int(input())))
