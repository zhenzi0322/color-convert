#coding=UTF-8

def hex_to_rgb(hex):
    """
    功能：16进制颜色格式颜色转换为RGB格式
    :param hex: 16进制颜色值，如：#fff000
    :return: rgb(255,182,193)
    """
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    rgb = str(r) + ',' + str(g) + ',' + str(b)
    return 'rgb({})'.format(rgb)


def hex_to_rgba(hex_str):
    """
    功能：带透明度的16进制颜色值转换为 RGBA 格式
    :param hex_str: #eefff3a8 转换成 rgba(238,255,243,0.66) 或者 #ffffff 转换成 rgba(255,255,255,1)
    :return: rgba(255,255,255,1)
    """
    hex_str = hex_str.replace('#', '')
    if len(hex_str) != 6:
        hex_str = hex_str + '0'
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    a = 1
    if len(hex_str) > 6:
        alpha = int(hex_str[6:10], 16) / 255 * 1
        a = round(alpha, 2)
    return 'rgba({},{},{},{})'.format(r, g, b, a)


def ten_to_hex(num):
    """
    功能：十进制颜色格式转换为十六进制格式。
    :param num: 十进制颜色值，如：16711680
    :return: #ffffff
    """
    color = str(hex(int(num)))
    return color.replace('0x', '#')


def ten_to_rgb(num):
    """
    功能：十进制颜色值转换为RGB格式
    :param num: 十进制颜色值，如：16711680
    :return: 255,0,0
    """
    try:
        str1 = hex(int(str(num), 10)).replace('0x', '#')
        return hex_to_rgba(str1)
    except Exception as e:
        raise Exception(e)


def my_function(a, b):
    """函数功能说明
     >>> my_function(2, 3)
     6
     >>> my_function('a', 3)
     'aaa'
    """
    return a * b