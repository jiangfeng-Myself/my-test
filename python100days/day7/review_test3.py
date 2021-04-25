"""
获取给定文件的后缀名
"""

def get_suffix(filename, has_dot = False):
    """
    获取文件的后缀名
    :param filename: 文件名
    :param has_dot: 后缀名是否带点
    :return: 返回文件的后缀名
    """
    pos = filename.rfind(',')
    if 0< pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''