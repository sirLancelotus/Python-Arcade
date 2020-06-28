from arcade import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
SQUARE_HEIGHT = 50
SQUARE_WIDTH = 50

def on_draw(delta_time):
    start_render()

    draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
                          SQUARE_WIDTH, SQUARE_HEIGHT,
                          color=(227, 105, 5))

    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    if on_draw.center_x < SQUARE_WIDTH // 2 \
       or on_draw.center_x > SCREEN_WIDTH - SQUARE_WIDTH // 2:
        on_draw.delta_x *= -1

    if on_draw.center_y < SQUARE_HEIGHT // 2  \
       or on_draw.center_y > SCREEN_HEIGHT - SQUARE_HEIGHT // 2:
        on_draw.delta_y *= -1

def main():
    open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "BOUNCING SQUARE")
    set_background_color(color=(124, 235, 200))
    schedule(on_draw, 1/80)
    run()

on_draw.center_x = 300
on_draw.center_y = 300
on_draw.delta_x = 115
on_draw.delta_y = 130

main()
