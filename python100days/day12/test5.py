"""
不良内容过滤
"""
import re
import pyperclip

def main():
    sentence = pyperclip.paste()
    print(sentence, 'sentence')
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*',sentence,  flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    main()
