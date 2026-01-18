# 练习 3：判断子序列 (双指针法)
# 判断 s 是否为 t 的子序列
def check_subsequence():
    s = input('请输入子序列 s:')
    t = input('请输入母串 t:')

    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    if i == len(s):
        print(f'"{s}" 是 "{t}" 的子序列')
    else:
        print(f'"{s}" 不是 "{t}" 的子序列')

check_subsequence()
