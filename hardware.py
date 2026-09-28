import board
import digitalio
import adafruit_ssd1306
import busio

I2C_SCL = board.GP5
I2C_SDA = board.GP4

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
DISPLAY_ADDR = 0x3C


class Buttons:
    def __init__(self):
        # left button
        self.left = digitalio.DigitalInOut(board.GP6)
        self.left.direction = digitalio.Direction.INPUT
        self.left.pull = digitalio.Pull.UP

        # right button
        self.right = digitalio.DigitalInOut(board.GP7)
        self.right.direction = digitalio.Direction.INPUT
        self.right.pull = digitalio.Pull.UP

        # up button
        self.up = digitalio.DigitalInOut(board.GP8)
        self.up.direction = digitalio.Direction.INPUT
        self.up.pull = digitalio.Pull.UP

        # down button
        self.down = digitalio.DigitalInOut(board.GP9)
        self.down.direction = digitalio.Direction.INPUT
        self.down.pull = digitalio.Pull.UP

        # a button
        self.a = digitalio.DigitalInOut(board.GP10)
        self.a.direction = digitalio.Direction.INPUT
        self.a.pull = digitalio.Pull.UP

        # b button
        self.b = digitalio.DigitalInOut(board.GP11)
        self.b.direction = digitalio.Direction.INPUT
        self.b.pull = digitalio.Pull.UP

        # b button
        self.home = digitalio.DigitalInOut(board.GP12)
        self.home.direction = digitalio.Direction.INPUT
        self.home.pull = digitalio.Pull.UP


def setup_display():
    i2c = busio.I2C(I2C_SCL, I2C_SDA, frequency=400000)

    display = adafruit_ssd1306.SSD1306_I2C(
        DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c, addr=DISPLAY_ADDR
    )

    display.contrast = 255
    display.fill(0)
    display.show()

    return display


def setup():
    display = setup_display()
    buttons = Buttons()
    return display, buttons
