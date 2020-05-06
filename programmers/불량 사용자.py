import re

def solution(user_id, banned_id):
    MASKED = '*'
    NBID = len(banned_id)

    unique = set()

    def dfs(count, selected=set()):
        if count == NBID:
            unique.add(tuple(sorted(selected)))
            return

        pat = re.compile(f"^{banned_id[count].replace(MASKED, '.')}$")
        for i, uid in enumerate(user_id):
            if uid not in selected and pat.match(uid):
                selected.add(uid)
                dfs(count + 1, selected)
                selected.remove(uid)

    dfs(0)
    return len(unique)