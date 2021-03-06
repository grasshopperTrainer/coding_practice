from sys import stdin, setrecursionlimit

# alt
# slower as in this problem not all palindrome answer is needed
def solution(N, nums, questions):
    dp = [[0]*N for i in range(N)]

    for end in range(N):
        for start in range(end+1):
            if start == end:
                dp[end][start] = 1
            elif start+1 == end:
                dp[end][start] = int(nums[start] == nums[end])
            else:
                dp[end][start] = int(nums[start] == nums[end] and dp[end-1][start+1])

    answers = []
    for s, e in questions:
        s, e = s-1, e-1
        answers.append(dp[e][s])
    return answers

# setrecursionlimit(1100)
# def solution(N, nums, questions):
#     called = [0]
#     record = {}
#     def is_pelindrome(x, y):
#         called[0] += 1
#         if (x, y) in record:
#             pass
#         elif x == y:
#             record[(x, y)] = 1
#         elif y-1 == x:
#             record[(x, y)] = int(nums[x] == nums[y])
#         else:
#             record[(x, y)] = int(is_pelindrome(x+1, y-1) and nums[x] == nums[y])
#         return record[(x, y)]
#     answers = []
#     for s, e in questions:
#         answers.append(is_pelindrome(s-1, e-1))
#     print(called)
#     return answers


N = int(stdin.readline())
nums = [int(c) for c in stdin.readline().strip().split(' ')]
questions = []
for _ in range(int(stdin.readline())):
    questions.append([int(c) for c in stdin.readline().strip().split(' ')])

for a in solution(N, nums, questions):
    print(a)

"""
1
2 3 2 2
1
2 4
"""
"""
4
1 2 3 4
10
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""