import time
import sys

sys.path.append("..")

import engine

BASKET = (0b100000001, 0b100000001, 0b010000010, 0b010000010, 0b001111100)


def run(oled, buttons):
    prev_home = True
    prev_left = True
    prev_right = True
    x = 64
    while True:
        # home logic
        curr_home = buttons.home.value
        curr_left = buttons.left.value
        curr_right = buttons.right.value
        if prev_home and not curr_home:
            return  # quit to launcher
        if prev_left and not curr_left:
            x -= 4
        if prev_right and not curr_right:
            x += 4
        prev_home = curr_home

        oled.fill(0)

        engine.blit_sprite(oled, BASKET, x, 59, 9, 1)

        oled.show()
        time.sleep(0.01)
