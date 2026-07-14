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


def rgb_to_hex(r, g, b):
    """
    功能：RGB格式颜色转换为十六进制格式
    :param r: 红色通道值 (0-255)
    :param g: 绿色通道值 (0-255)
    :param b: 蓝色通道值 (0-255)
    :return: #ffffff
    """
    return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))


def rgba_to_hex(r, g, b, a=1):
    """
    功能：RGBA格式颜色转换为十六进制格式（带透明度）
    :param r: 红色通道值 (0-255)
    :param g: 绿色通道值 (0-255)
    :param b: 蓝色通道值 (0-255)
    :param a: 透明度 (0-1)
    :return: #ffffffa8
    """
    alpha = int(round(a * 255))
    return '#{:02x}{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b), alpha)


def rgb_to_hsl(r, g, b):
    """
    功能：RGB格式颜色转换为HSL格式
    :param r: 红色通道值 (0-255)
    :param g: 绿色通道值 (0-255)
    :param b: 蓝色通道值 (0-255)
    :return: hsl(120, 100%, 50%)
    """
    r, g, b = int(r) / 255.0, int(g) / 255.0, int(b) / 255.0
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2.0

    if max_c == min_c:
        h = s = 0.0
    else:
        d = max_c - min_c
        s = d / (2.0 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6.0

    return 'hsl({}, {}%, {}%)'.format(round(h * 360), round(s * 100), round(l * 100))


def hsl_to_rgb(h, s, l):
    """
    功能：HSL格式颜色转换为RGB格式
    :param h: 色相 (0-360)
    :param s: 饱和度 (0-100)
    :param l: 亮度 (0-100)
    :return: rgb(255,255,255)
    """
    h, s, l = float(h) / 360.0, float(s) / 100.0, float(l) / 100.0

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return 'rgb({}, {}, {})'.format(round(r * 255), round(g * 255), round(b * 255))


def rgb_to_hsv(r, g, b):
    """
    功能：RGB格式颜色转换为HSV格式
    :param r: 红色通道值 (0-255)
    :param g: 绿色通道值 (0-255)
    :param b: 蓝色通道值 (0-255)
    :return: hsv(120, 100%, 100%)
    """
    r, g, b = int(r) / 255.0, int(g) / 255.0, int(b) / 255.0
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    v = max_c
    d = max_c - min_c
    s = 0 if max_c == 0 else d / max_c

    if max_c == min_c:
        h = 0.0
    else:
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6.0

    return 'hsv({}, {}%, {}%)'.format(round(h * 360), round(s * 100), round(v * 100))


def hsv_to_rgb(h, s, v):
    """
    功能：HSV格式颜色转换为RGB格式
    :param h: 色相 (0-360)
    :param s: 饱和度 (0-100)
    :param v: 明度 (0-100)
    :return: rgb(255,255,255)
    """
    h, s, v = float(h) / 360.0, float(s) / 100.0, float(v) / 100.0

    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    mod = i % 6
    if mod == 0:
        r, g, b = v, t, p
    elif mod == 1:
        r, g, b = q, v, p
    elif mod == 2:
        r, g, b = p, v, t
    elif mod == 3:
        r, g, b = p, q, v
    elif mod == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q

    return 'rgb({}, {}, {})'.format(round(r * 255), round(g * 255), round(b * 255))


def rgb_to_cmyk(r, g, b):
    """
    功能：RGB格式颜色转换为CMYK格式
    :param r: 红色通道值 (0-255)
    :param g: 绿色通道值 (0-255)
    :param b: 蓝色通道值 (0-255)
    :return: cmyk(0%, 0%, 0%, 0%)
    """
    r, g, b = int(r) / 255.0, int(g) / 255.0, int(b) / 255.0
    k = 1 - max(r, g, b)
    if k == 1:
        return 'cmyk(0%, 0%, 0%, 100%)'
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return 'cmyk({}%, {}%, {}%, {}%)'.format(round(c * 100), round(m * 100), round(y * 100), round(k * 100))


def cmyk_to_rgb(c, m, y, k):
    """
    功能：CMYK格式颜色转换为RGB格式
    :param c: 青色 (0-100)
    :param m: 品红 (0-100)
    :param y: 黄色 (0-100)
    :param k: 黑色 (0-100)
    :return: rgb(255,255,255)
    """
    c, m, y, k = float(c) / 100.0, float(m) / 100.0, float(y) / 100.0, float(k) / 100.0
    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))
    return 'rgb({}, {}, {})'.format(r, g, b)


def hex_to_hsl(hex_str):
    """
    功能：十六进制颜色格式转换为HSL格式
    :param hex_str: 16进制颜色值，如：#fff000
    :return: hsl(56, 100%, 50%)
    """
    hex_str = hex_str.replace('#', '')
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return rgb_to_hsl(r, g, b)


def hex_to_hsv(hex_str):
    """
    功能：十六进制颜色格式转换为HSV格式
    :param hex_str: 16进制颜色值，如：#fff000
    :return: hsv(56, 100%, 100%)
    """
    hex_str = hex_str.replace('#', '')
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return rgb_to_hsv(r, g, b)


def my_function(a, b):
    """函数功能说明
     >>> my_function(2, 3)
     6
     >>> my_function('a', 3)
     'aaa'
    """
    return a * b