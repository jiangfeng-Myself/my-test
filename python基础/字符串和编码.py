# python的字符串编码
print(ord('A'))  # 编码
print(chr(66))  # 解码


# eg：
s = 'Python中文'
b = s.encode('utf-8')
print(b)
s = b.decode('utf-8')
print(s)
