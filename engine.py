def blit_sprite(oled, sprite, x, y, width, color=1):
    for dy, row in enumerate(sprite):
        for dx in range(width):
            if row >> (width - 1 - dx) & 1:
                oled.pixel(x + dx, y + dy, color)
