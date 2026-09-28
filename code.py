import board
import busio
import adafruit_ssd1306
import os
import hardware


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

oled, buttons = hardware.setup()

oled.contrast = 255
selected_game = 0
while True:
    oled.fill(0)
    oled.text("Installed Games:", 0, 0, 1)
    for i in range(len(installed_games)):
        if i == selected_game:
            text_colour = 0
            oled.fill_rect(0, (i + 1) * 8, 128, 8, 1)
        else:
            text_colour = 1
        oled.text(installed_games[i], 0, (i + 1) * 8, text_colour)
    oled.show()
