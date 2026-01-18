# 练习 1：字符串压缩 (Run-Length Encoding)
# 输入：aaabbc -> 输出：a3b2c1
def compress_string():
    words = input('请输入待压缩字符串:')
    if not words:
        print('输入为空')
        return

    result = []
    counts = 1

    for i in range(len(words) - 1):
        if words[i] == words[i+1]:
            counts += 1
        else:
            result.append(words[i] + str(counts))
            counts = 1
    
    # 处理最后一个字符
    result.append(words[-1] + str(counts))
    
    final_str = ''.join(result)
    print(f'压缩结果是：{final_str}')
    print(f'压缩率：{len(final_str)/len(words):.2%}')

compress_string()
