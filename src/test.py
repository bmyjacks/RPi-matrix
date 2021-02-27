from strip import *
import params
import time

display = Strip(params.LED_COUNT, params.LED_PIN, params.LED_FREQ_HZ, params.LED_DMA, params.LED_INVERT,
                params.LED_BRIGHTNESS)

display.begin()

for x in range(32):
    for y in range(8):
        if x % 2:
            if y % 2:
                display.set_pixel_color(x, y, 255, 0, 0)
            else:
                display.set_pixel_color(x, y, 255, 255, 0)
        else:
            if y % 2:
                display.set_pixel_color(x, y, 0, 0, 255)
            else:
                display.set_pixel_color(x, y, 0, 255, 255)
        display.show()
        time.sleep(0.05)
