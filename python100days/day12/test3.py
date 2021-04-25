"""
验证输入用户和qq号是否有效并给出对应的提示信息
要求：
用户徐碧由字母、数字和下划线构成切长度在6~20个字符之间
qq号是5~12的数字且首位不能为0
"""

import re

def main():
    username = input('请输入用户名：')
    qq = input(' 请输入QQ号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号')
    if m1 and m2:
        print('你输入的信息有效！')

if __name__ == '__main__':
    main()