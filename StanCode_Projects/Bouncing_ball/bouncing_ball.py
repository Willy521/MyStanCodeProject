"""
File: boundcing_ball
Name: Chen Wei Ting
-------------------------
To simulate the track of a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 0
DELAY = 10
GRAVITY = 0.5
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

click = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global click
    window = GWindow(800, 500, title='bouncing_ball.py')
    ball = GOval(SIZE, SIZE)
    window.add(ball, START_X, START_Y)
    ball.filled = True
    onmouseclicked(create_hole)
    vy = 0
    time = 0

    while True:
        if click:
            time += 1
            while True:
                pause(DELAY)
                if ball.x + ball.width >= window.width:
                    window.add(ball, START_X, START_Y)
                    vy = 0
                    click = False
                    break
                else:
                    vy += GRAVITY
                    ball.move(VX, vy)
                    if ball.y + ball.height >= window.height and vy > 0:
                        vy = -vy
                        vy *= REDUCE
        if time >= 3:
            break
        pause(DELAY)


def create_hole(mouse):
    global click
    click = True
    # To set a switch to ensure the ball will not be affected by the user's mouse click.


if __name__ == "__main__":
    main()
