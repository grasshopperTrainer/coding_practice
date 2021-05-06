from sys import stdin


# # brute force
# def solution(string):
#     L = len(string)
#     for size in range(L//2+1, 0, -1):
#         for ps in range(L-size*2+1):
#             patt = string[ps:ps+size]
#             for s in range(ps+size, L):
#                 match = string[s:s+size]
#                 if len(match) != len(patt):
#                     break
#                 if patt == match:
#                     return size
#     return 0

# not KMP
# def solution(string):
#     max_count = 0
#     L = len(string)
#     for i in range(L):
#         for j in range(i + 1, L):
#             pa, pb = i, j
#             count = 0
#             while pb != L:
#                 if string[pa] == string[pb]:
#                     count += 1
#                     pa += 1
#                     pb += 1
#                 else:
#                     break
#             max_count = max(max_count, count)
#     return max_count


# time over?
# KMP
def solution(string):
    L = len(string)
    len_max = 0
    for s in range(L):
        # for size in range(L-1, 0, -1):
        #     for start, end in zip(range(L - size), range(size, L + 1)):
        #         patt = string[start:end]
        size = L - s
        # patt = string[s:]
        # find pi array
        pi = [0] * size
        i, j = s + 1, s
        while i != L:
            # print(i, j)
            if string[i] == string[j]:
                pi[i - s] = j + 1 - s
                i += 1
                j += 1
            else:
                if j == s:
                    pi[i - s] = 0
                    i += 1
                else:
                    j = pi[j - 1 - s] + s
        print(pi)
        len_max = max(len_max, max(pi))
        # do KMP
        # j = 0
        # for i in range(s + 1, L):
        #     # finding fitting pos
        #     while string[i] != patt[j] and j != 0:
        #         j = pi[j-1]
        #     if string[i] == patt[j]:
        #         if j == len(patt) - 1: # if seeing last of pattern and match
        #             return size
        #             # j = pi[j] # this is for next search in same substring
        #         else:
        #             j += 1

    return len_max


string = stdin.readline().strip()
print(solution(string))
'abcdabcabbabca'
'abcdefghij'
'kakak'
'AAABABAA'
'kkkkkkkkk'
'YabccZaabc'
