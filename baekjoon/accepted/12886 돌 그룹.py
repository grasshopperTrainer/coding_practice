from sys import stdin, setrecursionlimit


# setrecursionlimit(1_000_000)
# def solution(nums):
#     dp = set()
#
#     def search(nums, gen):
#         if tuple(nums) in dp:
#             return False
#         dp.add(tuple(nums))
#
#         if nums[0] == nums[1] == nums[2]:
#             return True
#
#         for i in range(3):
#             for j in range(i + 1, 3):
#                 if nums[i] != nums[j]:
#                     new_nums = nums.copy()
#                     if new_nums[i] < new_nums[j]:
#                         new_nums[j] -= new_nums[i]
#                         new_nums[i] += new_nums[i]
#                     else:
#                         new_nums[i] -= new_nums[j]
#                         new_nums[j] += new_nums[j]
#
#                     if search(new_nums, gen + 1):
#                         return True
#         return False
#
#     return int(search(nums, 0))

from collections import deque


def solution(nums):
    visited = set()
    moves = deque([nums])
    while moves:
        move = moves.popleft()

        if move[0] == move[1] == move[2]:
            return 1
        if tuple(move) in visited:
            continue
        visited.add(tuple(move))

        for i in range(3):
            for j in range(i + 1, 3):
                if move[i] != move[j] and move[i] != 0 and move[j] != 0:
                    new_move = move.copy()
                    if new_move[i] < new_move[j]:
                        new_move[j] -= new_move[i]
                        new_move[i] *= 2
                    else:
                        new_move[i] -= new_move[j]
                        new_move[j] *= 2
                    moves.append(new_move)
    return 0


nums = list(map(int, stdin.readline().strip().split(' ')))
print(solution(nums))
