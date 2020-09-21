arr = list('abcdefg')

leaf_size = 2**len(bin(len(arr)-1)[2:])
tree = ['']*2*leaf_size
print(leaf_size, len(tree))
offset = leaf_size
for i in range(len(arr)):
    tree[offset+i] = arr[i]

print(tree)
def join(left, right, tree_idx):
    if left == right:
        return tree[tree_idx]
    m = (left+right)//2
    tree[tree_idx] = join(left, m, tree_idx*2)+join(m+1, right, tree_idx*2+1)
    return tree[tree_idx]
join(1, leaf_size, 1)
print(tree)
def get(left, right, start, end, tree_idx):
    print(left, right, start, end)
    if start <= left and right <= end:
        print('getting part', tree[tree_idx])
        return tree[tree_idx]
    if end < left or right < start:
        return ''
    m = (left+right)//2
    return get(left, m, start, end, tree_idx*2)+get(m+1, right, start, end, tree_idx*2+1)
print('getting', get(1, leaf_size, 2, 5, 1))
