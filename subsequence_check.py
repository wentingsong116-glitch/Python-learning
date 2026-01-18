s=input('请输入字符串s:')
t=input('请输入字符串t:')

temp_t=t

for i in s:
    if i in temp_t:
        idx=temp_t.find(i)
        temp_t=temp_t[idx+1:]
    else:
        print('字符串s不是字符串t的子序列')
        break

else:
    print('字符串s是字符串t的子序列')
 
