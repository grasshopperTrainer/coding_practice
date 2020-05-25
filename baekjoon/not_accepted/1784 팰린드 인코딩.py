# not good need dp
def solution(palindrome):
    cache = {}
    palindrome = tuple(palindrome)

    def search(chars):
        if len(chars) == 2:
            if chars[0] == chars[1]:
                return 1
            else:
                return 2

        if tuple(chars) in cache:
            return cache[tuple(chars)]

        min_value = len(chars)
        seen_chars = []
        for i, c in enumerate(chars):
            seen_chars.append(c)
            count = 1
            # find part palindrome
            while True:
                right_start = len(seen_chars) - count
                left_start = right_start - count
                if left_start < 0:
                    break

                left, right = seen_chars[left_start:right_start], seen_chars[right_start:]
                right.reverse()
                if left == right:
                    new_string = chars[:right_start] + chars[i+1:]
                    result = search(new_string)
                    min_value = min([min_value, result])
                    cache[tuple(new_string)] = result
                count += 1

        return min_value

    return search(palindrome)


print(solution(input().strip()))