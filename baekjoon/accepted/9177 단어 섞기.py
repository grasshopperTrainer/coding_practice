from sys import stdin


def solution(i, a, b, c):
    AL, BL, CL = len(a), len(b), len(c)

    dp = [[True] * (BL+1) for _ in range(AL+1)]
    def search(aptr, bptr, cptr):
        if cptr == CL:
            return True

        if not dp[aptr][bptr]:
            return False

        char = c[cptr]
        if aptr < AL and a[aptr] == char:
            if search(aptr + 1, bptr, cptr + 1):
                return True
        if bptr < BL and b[bptr] == char:
            if search(aptr, bptr + 1, cptr + 1):
                return True

        dp[aptr][bptr] = False
        return False

    if search(0, 0, 0):
        print(f'Data set {i}: yes')
    else:
        print(f'Data set {i}: no')


for i in range(int(stdin.readline())):
    solution(i + 1, *stdin.readline().strip().split(' '))
