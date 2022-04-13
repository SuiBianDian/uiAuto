import os

import yaml

from config import bath_path


def read_yaml(fileName):
    arrs = []
    # file_path = './data/mp_data.yaml'
    file_path = bath_path + os.sep + 'data' + os.sep + fileName  # os.sep （会自动获取当前系统的分隔符 '/' or '\'）
    print(bath_path)
    """
    注意此处的文件地址，因为我用的命令行执行，所以是uiAuto目录下，那么直接进入data就行了。
    但是，如果是用的点击运行，那就不行了，那此时是在scripts目录下，想进入data需要返回上一级在进入
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for val in yaml.safe_load(f).values():
            """
            yaml.safe_load(f) 加载进来是一个字典，我们在取values。
            然后读出来是一个 dict_values 形式, 必须把变量键值对取出来
            所以遍历，而且只会得到一个字典形式，然后再取这个字典的值，又是 dict_values 形式
            在转成元组就行
            """
            arrs.append(tuple(val.values()))
    return arrs


if __name__ == '__main__':
    print(read_yaml('mp_data.yaml'))
