import board
import busio
import adafruit_ssd1306
import os


def get_installed_games():
    try:
        # Get all files in the /games folder
        all_files = os.listdir("/games")

        # Keep only .py files, remove the .py extension, and ignore __init__.py
        games = []
        for file in all_files:
            if file.endswith(".py") and file != "__init__.py":
                games.append(file[:-3])

        return games

    except OSError:
        # This happens if the /games folder doesn't exist yet
        return []


installed_games = get_installed_games()
print(installed_games)

print("Starting")

i2c = busio.I2C(board.GP5, board.GP4)
print("I2C created")

while not i2c.try_lock():
    pass

print("Scanning:", i2c.scan())

i2c.unlock()

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
print("Display created")

oled.contrast = 255
oled.fill(1)
oled.show()

print("Done")
