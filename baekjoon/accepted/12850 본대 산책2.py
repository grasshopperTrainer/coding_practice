def solution(N):
    graph = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 1, 0]]

    def mul_matrix(m1, m2):
        m3 = [[0] * len(m2[0]) for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
                m3[i][j] %= 1_000_000_007
        return m3

    def calculate(n):
        if n == 1:
            return graph

        if n % 2 == 0:
            r = calculate(n // 2)
            return mul_matrix(r, r)
        else:
            n = n - 1
            r = calculate(n // 2)
            return mul_matrix(mul_matrix(r, r), graph)

    return calculate(N)[0][0]


print(solution(int(input())))
