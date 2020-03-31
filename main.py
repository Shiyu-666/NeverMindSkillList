from mechanics import *


def is_float(num):
    return False if num.count('.') > 1 else num.replace('.', '').isdigit()


def attribute_edit(attrs):
    limit = attrs[4]
    print('正在编辑 %s 参数.\n参数描述: %s.' % (attrs[0], attrs[2]))
    print('参数限制: ' + {'bool': 'True / False', 'float': '数字', 'int': '整数', 'str': '字符串'}[limit])
    res = input('  请输入您想要的参数值 >> ')

    while (limit == 'bool' and res not in ['True', 'False']) or (
           limit == 'int' and not res.isdigit()) or (
           limit == 'float' and not is_float(res)) or (
           limit == 'str' and not res):
        res = input('  输入有误, 请重新输入 >> ')

    return res
