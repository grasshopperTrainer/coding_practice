def find_min(nums, target):
    s, e = 0, len(nums)-1
    if s == e:
        return 0
    # !!! fix and remember this pattern for finding min max !!!
    while s <= e:
        m = (s + e) // 2
        if nums[m] < target:    # !!!
            s = m + 1
        else:
            e = m - 1
    return s                    # !!!

def find_max(nums, target):
    s, e = 0, len(nums)-1
    if s == e:
        return 0
    # !!! fix and remember this pattern for finding min max !!!
    while s <= e:
        m = (s + e) // 2
        if nums[m] <= target:   # !!!
            s = m + 1
        else:
            e = m - 1           # !!!
    return e

nums = [0, 0, 0, 1, 1, 2, 3, 8]
print(find_min(nums, 0))
print(find_max(nums, 0))