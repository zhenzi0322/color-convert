Color Conversion Tool
=====================

Hexadecimal to rgb

.. code:: python

    from color_convert import color

    rgb = color.hex_to_rgb('#fff000')
    print(rgb)  # rgb(255,240,0)

Hexadecimal to rgba

.. code:: python

    from color_convert import color

    rgba = color.hex_to_rgba('#fff000')
    print(rgba)  # rgba(255,240,0,1)

Decimal to hexadecimal

.. code:: python

    from color_convert import color

    hex = color.ten_to_hex(16711680)
    print(hex)  # #ff0000

Decimal to rgb

.. code:: python

    from color_convert import color

    hex_rgb = color.ten_to_rgb(16711680)
    print(hex_rgb)  # rgba(255,0,0,1)
