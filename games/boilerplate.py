import time


def run(oled, buttons):
    prev_home = True
    while True:
        curr_home = buttons.home.value
        if prev_home and not curr_home:
            return  # quit to launcher
        prev_home = curr_home
        print(buttons.home.value)
        oled.fill(1)
        oled.show()
        time.sleep(0.01)
