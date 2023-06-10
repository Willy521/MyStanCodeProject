"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gwindow import GWindow

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
BALL_RADIUS = 10


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    first_click = True
    life_time = 0
    original_position = True

    # Add the animation loop here!
    while True:
        if graphics.click:

            # if it is a first click
            if first_click:
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                first_click = False
            graphics.ball.move(vx, vy)

            # out of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                life_time += 1
                graphics.window.add(graphics.ball, graphics.window.width / 2 - graphics.ball.width / 2,
                                    graphics.window.height / 2 - graphics.ball.height / 2)
                graphics.click = False
                first_click = True
                if life_time > NUM_LIVES - 1:
                    break

            # collide condition
            if_collide = True
            for i in range(0, graphics.ball.width + 1, graphics.ball.width):
                for j in range(0, graphics.ball.height + 1, graphics.ball.height):
                    collide_object = graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j)
                    if collide_object is not None:
                        if collide_object is graphics.paddle:
                            if vy > 0:
                                vy = -vy
                        else:
                            if if_collide is True:
                                vy = - vy
                                graphics.window.remove(collide_object)
                                if_collide = False
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
