import board
import busio
import adafruit_ssd1306
import os
import hardware
import time


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
display_start = 0

prev_down = True
prev_up = True
dirty = True

currently_displayed = installed_games[:7]
print(currently_displayed)

while True:
    curr_down = buttons.down.value
    curr_up = buttons.up.value
    if len(installed_games) > 0:
        if prev_down and not curr_down:
            if selected_game == len(installed_games) - 1:
                selected_game = 0
            else:
                selected_game += 1
            dirty = True
        if prev_up and not curr_up:
            if selected_game == 0:
                selected_game = len(installed_games) - 1
            else:
                selected_game -= 1
            dirty = True
        if selected_game < display_start:
            display_start = selected_game
        elif selected_game >= display_start + 7:
            display_start = selected_game - 7 + 1

    prev_up = curr_up
    prev_down = curr_down

    if dirty:
        currently_displayed = installed_games[display_start : display_start + 7]
        oled.fill(0)
        oled.text(
            f"Installed Games: {selected_game + 1}/{len(installed_games)}", 0, 0, 1
        )
        for i in range(len(currently_displayed)):
            real_index = display_start + i
            if real_index == selected_game:
                text_colour = 0
                oled.fill_rect(0, (i + 1) * 8, 128, 8, 1)
            else:
                text_colour = 1
            oled.text(currently_displayed[i], 0, (i + 1) * 8, text_colour)
        oled.show()
        dirty = False

    time.sleep(0.005)
