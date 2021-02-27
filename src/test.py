from strip import Strip
import params
import random


def self_test():
    print("Starting self test")
    print("Testing...")

    print("Value assignment testing...")
    display = Strip(params.LED_COUNT, params.LED_PIN, params.LED_FREQ_HZ, params.LED_DMA, params.LED_INVERT,
                    params.LED_BRIGHTNESS)
    print("Value assignment test passed.")

    display.begin()

    print("Color testing start...")
    print("Color red testing...")
    for red in range(0, 255, 1):
        display.fill_rect(0, 0, params.LED_MAX_WIDTH, params.LED_MAX_HEIGHT, red, 0, 0)
        display.show()
    print("Color red test passed.")
    print("Color green testing...")
    for green in range(0, 255, 1):
        display.fill_rect(0, 0, params.LED_MAX_WIDTH, params.LED_MAX_HEIGHT, 0, green, 0)
        display.show()
    print("Color green test passed.")
    print("Color blue testing...")
    for blue in range(0, 255, 1):
        display.fill_rect(0, 0, params.LED_MAX_WIDTH, params.LED_MAX_HEIGHT, 0, 0, blue)
        display.show()
    print("Color blue test passed.")
    print("Random color testing...")
    for rce in range(100):
        for x in range(0, params.LED_MAX_WIDTH, 1):
            for y in range(0, params.LED_MAX_HEIGHT, 1):
                display.set_pixel_color(x, y, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        display.show()

    print("Random color test passed.")
    print("Color test passed.")
    print("All tests passed.")
    display.fill_rect(0, 0, 32, 8, 0, 0, 0)
    display.show()


if __name__ == "__main__":
    self_test()
