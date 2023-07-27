import machine, os, lv_spi, sdcard
from ili9XXX import st7735, COLOR_MODE_RGB, MADCTL_MX, MADCTL_MY, PORTRAIT, LANDSCAPE
import lvgl as lv



disp = st7735(
        miso=-1, mosi=19, clk=18, cs=13, dc=12, rst=4, backlight_on=2, mhz=40,  hybrid=True, width=160, height=80, start_x=0, start_y=20,
        colormode=COLOR_MODE_RGB, invert=False, rot=LANDSCAPE, double_buffer=True, half_duplex=True,
        asynchronous=False, initialize=True)

scr = lv.scr_act()
scr_style = lv.style_t()
scr_style.set_bg_color(lv.color_hex(0x003a00))
scr.add_style(scr_style,0)
          
label = lv.label(lv.scr_act())
label_style = lv.style_t()
label_style.set_text_color(lv.color_hex(0xffffff))
label.set_text("Hello world")
label.add_style(label_style,0)
label.align(lv.ALIGN.CENTER, 0, 0)

lv.scr_load(scr)
