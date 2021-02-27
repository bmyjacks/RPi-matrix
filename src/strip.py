from rpi_ws281x import Adafruit_NeoPixel, Color


class Strip:
    def __init__(self, led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness):
        self.graph = Adafruit_NeoPixel(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness)

    def begin(self):
        return self.graph.begin()

    def show(self):
        return self.graph.show()

    def num_pixels(self):
        return self.graph.numPixels()

    def set_pixel_color(self, x, y, color_red, color_green, color_blue):
        if x % 2:
            position = (31 - x) * 8 + (8 - y - 1)
        else:
            position = (31 - x) * 8 + y
        self.graph.setPixelColor(position, Color(color_red, color_green, color_blue))

    def fill_rect(self, position, rect_length, color_red, color_green, color_blue):
        for loc in range(position, (position + rect_length), 1):
            self.graph.setPixelColor(loc, Color(color_red, color_green, color_blue))
