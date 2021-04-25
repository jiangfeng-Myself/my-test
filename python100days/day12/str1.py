"""
字符串常用操作
"""

import pyperclip

# 转义字符
print(' My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和数字
print(str.isalnum())
# 字符串是否只包含数字
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list))# 将列表转换成str，并且用-来隔开
sentence = 'You go your way I will go mine'
word_list = sentence.split()
print(word_list)
email = '    jackfrued@126.com'
print(email)
print(email.strip()) # 清除两边的空格
print(email.lstrip()) # 清除左边的空格

# 将文本放入系统剪切板中
# pyperclip.copy('老虎不发威你当我是病猫呀')
# 从系统剪切板获取文本
print(pyperclip.paste())