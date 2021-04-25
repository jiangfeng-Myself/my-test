import random

def generate_code(code_len =  4):
    """
    生成指定长度的验证码，包含数字、小写字母。大写字母
    :param code_len: 验证码长度
    :return: 返回验证码
    """
    all_charts = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSTUVWXYZ'
    last_pos = len(all_charts) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_charts[index]
    return code

print(generate_code())