from sys import stdin


def solution(queries, stack):
    MAXVAL = 10 ** 9
    for query in queries:
        try:
            if query.startswith('NUM'):
                stack.append(int(query.replace('NUM ', '')))
            else:
                if query == 'POP':
                    stack.pop()
                elif query == 'INV':
                    stack.append(-stack.pop())
                elif query == 'DUP':
                    stack.append(stack[-1])
                elif query == 'SWP':
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                elif query == 'ADD':
                    stack.append(stack.pop() + stack.pop())
                elif query == 'SUB':
                    f, s = stack.pop(), stack.pop()
                    stack.append(s - f)
                elif query == 'MUL':
                    stack.append(stack.pop() * stack.pop())
                elif query == 'DIV':
                    f, s = stack.pop(), stack.pop()
                    r = abs(s) // abs(f)
                    if (0 < f and s < 0) or (f < 0 and 0 < s):
                        r = -r
                    stack.append(r)
                elif query == 'MOD':
                    f, s = stack.pop(), stack.pop()
                    r = abs(s) % abs(f)
                    if s < 0:
                        r = -r
                    stack.append(r)
            if stack and MAXVAL < abs(stack[-1]):
                raise
        except:
            return 'ERROR'

    if len(stack) != 1:
        return 'ERROR'
    return stack[0]


while True:
    queries = [stdin.readline().strip()]

    if queries[0] == 'QUIT':
        break

    while True:
        if queries[-1] == 'END':
            break
        query = stdin.readline().strip()
        queries.append(query)

    for _ in range(int(stdin.readline())):
        val = int(stdin.readline())
        print(solution(queries, [val]))
    print()

    stdin.readline().strip()  # remove empty line

"""
NUM -4
MOD
END
1
-13

QUIT
"""
"""
POP
END
1
-13

QUIT
"""
"""
END
1
1

QUIT
"""