from collections import deque


def solution(words, queries):
    WILDCARD, END = '?', '_end'

    pref_dic, suff_dic = {}, {}
    for word in words:
        L = len(word)
        pref_root, suff_root = pref_dic.setdefault(L, {}), suff_dic.setdefault(L, {})
        for i in range(len(word)):
            pref_root = pref_root.setdefault(word[i], [0, {}])
            pref_root[0] += 1
            pref_root = pref_root[1]
            suff_root = suff_root.setdefault(word[-(i + 1)], [0, {}])
            suff_root[0] += 1
            suff_root = suff_root[1]
        pref_root[END] = END
        suff_root[END] = END

    answer = []
    for q in queries:
        L = len(q)
        if q[0] == WILDCARD:
            dic = suff_dic
            q = q[::-1]
        else:
            dic = pref_dic

        if L not in dic:
            answer.append(0)
            continue
        dic = dic[L]
        for c in q:
            if c == WILDCARD:
                counter = 0
                for count, _ in dic.values():
                    counter += count
                answer.append(counter)
                break
            else:
                if c not in dic:
                    answer.append(0)
                    break
                else:
                    dic = dic[c][1]

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))