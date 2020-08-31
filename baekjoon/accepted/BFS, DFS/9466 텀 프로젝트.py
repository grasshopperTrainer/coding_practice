from sys import stdin, setrecursionlimit


setrecursionlimit(100_100)
def solution(N, selection):

    checked = set()
    def dfs(at, visited):
        if at in checked:
            return (0, 0)
        if at in visited:
            return (at, 0)
        else:
            visited.add(at)
            cycle_gate = dfs(selection[at-1], visited)
            checked.add(at)
            if cycle_gate[0]:
                if at == cycle_gate[0]:
                    return 0, 0
                return cycle_gate
            else:
                return 0, cycle_gate[1]+1

    score = 0
    for i in range(N):
        if i+1 not in checked:
            score += dfs(i+1, set())[1]
    return score


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    selection = [int(c) for c in stdin.readline().strip().split(' ')]
    print(solution(N, selection))
