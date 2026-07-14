
<p align="center">
  <h1>color-convert</h1>
  <b>颜色格式转换工具，支持 HEX、RGB、RGBA、HSL、HSV、CMYK、十进制等多种颜色格式之间的相互转换。</b>
  <br><br>
  <a href="https://pypi.org/project/color-convert/"><img src="https://img.shields.io/pypi/v/color-convert.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/color-convert/"><img src="https://img.shields.io/pypi/pyversions/color-convert.svg" alt="Python"></a>
  <a href="https://github.com/zhenzi0322/color-convert/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/color-convert.svg" alt="License"></a>
  <a href="https://zhenzi0322.readthedocs.io/zh-cn/latest/color-convert/"><img src="https://readthedocs.org/projects/zhenzi0322/badge/?version=latest" alt="Documentation Status"></a>
</p>

## 安装

```bash
pip install color-convert
```

## 支持的颜色格式

| 格式 | 示例 |
|------|------|
| HEX（十六进制） | `#fff000` |
| RGB | `rgb(255, 240, 0)` |
| RGBA | `rgba(255, 240, 0, 1)` |
| HSL | `hsl(56, 100%, 50%)` |
| HSV | `hsv(56, 100%, 100%)` |
| CMYK | `cmyk(0%, 6%, 100%, 0%)` |
| Decimal（十进制） | `16711680` |

## 使用示例

### 十六进制 → RGB

```python
from color_convert import color

rgb = color.hex_to_rgb('#fff000')
print(rgb)  # rgb(255,240,0)
```

### 十六进制 → RGBA

```python
from color_convert import color

rgba = color.hex_to_rgba('#fff000')
print(rgba)  # rgba(255,240,0,1)

rgba = color.hex_to_rgba('#fff000a8')
print(rgba)  # rgba(255,240,0,0.66)
```

### 十六进制 → HSL

```python
from color_convert import color

hsl = color.hex_to_hsl('#fff000')
print(hsl)  # hsl(56, 100%, 50%)
```

### 十六进制 → HSV

```python
from color_convert import color

hsv = color.hex_to_hsv('#fff000')
print(hsv)  # hsv(56, 100%, 100%)
```

### 十进制 → 十六进制

```python
from color_convert import color

hex_val = color.ten_to_hex(16711680)
print(hex_val)  # #ff0000
```

### 十进制 → RGBA

```python
from color_convert import color

rgba = color.ten_to_rgb(16711680)
print(rgba)  # rgba(255,0,0,1)
```

### RGB → 十六进制

```python
from color_convert import color

hex_val = color.rgb_to_hex(255, 240, 0)
print(hex_val)  # #fff000
```

### RGBA → 十六进制

```python
from color_convert import color

hex_val = color.rgba_to_hex(255, 240, 0, 0.66)
print(hex_val)  # #fff000a8
```

### RGB → HSL

```python
from color_convert import color

hsl = color.rgb_to_hsl(255, 240, 0)
print(hsl)  # hsl(56, 100%, 50%)
```

### HSL → RGB

```python
from color_convert import color

rgb = color.hsl_to_rgb(56, 100, 50)
print(rgb)  # rgb(255, 238, 0)
```

### RGB → HSV

```python
from color_convert import color

hsv = color.rgb_to_hsv(255, 240, 0)
print(hsv)  # hsv(56, 100%, 100%)
```

### HSV → RGB

```python
from color_convert import color

rgb = color.hsv_to_rgb(56, 100, 100)
print(rgb)  # rgb(255, 238, 0)
```

### RGB → CMYK

```python
from color_convert import color

cmyk = color.rgb_to_cmyk(255, 240, 0)
print(cmyk)  # cmyk(0%, 6%, 100%, 0%)
```

### CMYK → RGB

```python
from color_convert import color

rgb = color.cmyk_to_rgb(0, 6, 100, 0)
print(rgb)  # rgb(255, 240, 0)
```

## API 参考

| 函数名 | 说明 | 参数 | 返回值示例 |
|--------|------|------|------------|
| `hex_to_rgb(hex)` | 十六进制 → RGB | `hex`: 如 `#fff000` | `rgb(255,240,0)` |
| `hex_to_rgba(hex_str)` | 十六进制 → RGBA（支持带透明度） | `hex_str`: 如 `#fff000` 或 `#fff000a8` | `rgba(255,240,0,1)` |
| `hex_to_hsl(hex_str)` | 十六进制 → HSL | `hex_str`: 如 `#fff000` | `hsl(56, 100%, 50%)` |
| `hex_to_hsv(hex_str)` | 十六进制 → HSV | `hex_str`: 如 `#fff000` | `hsv(56, 100%, 100%)` |
| `ten_to_hex(num)` | 十进制 → 十六进制 | `num`: 如 `16711680` | `#ff0000` |
| `ten_to_rgb(num)` | 十进制 → RGBA | `num`: 如 `16711680` | `rgba(255,0,0,1)` |
| `rgb_to_hex(r, g, b)` | RGB → 十六进制 | `r, g, b`: 0-255 | `#fff000` |
| `rgba_to_hex(r, g, b, a)` | RGBA → 十六进制（带透明度） | `r, g, b`: 0-255, `a`: 0-1 | `#fff000a8` |
| `rgb_to_hsl(r, g, b)` | RGB → HSL | `r, g, b`: 0-255 | `hsl(56, 100%, 50%)` |
| `hsl_to_rgb(h, s, l)` | HSL → RGB | `h`: 0-360, `s`: 0-100, `l`: 0-100 | `rgb(255, 238, 0)` |
| `rgb_to_hsv(r, g, b)` | RGB → HSV | `r, g, b`: 0-255 | `hsv(56, 100%, 100%)` |
| `hsv_to_rgb(h, s, v)` | HSV → RGB | `h`: 0-360, `s`: 0-100, `v`: 0-100 | `rgb(255, 238, 0)` |
| `rgb_to_cmyk(r, g, b)` | RGB → CMYK | `r, g, b`: 0-255 | `cmyk(0%, 6%, 100%, 0%)` |
| `cmyk_to_rgb(c, m, y, k)` | CMYK → RGB | `c, m, y, k`: 0-100 | `rgb(255, 240, 0)` |

## License

[MIT License](LICENSE)
