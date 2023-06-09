"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import randoml


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width / 2 - BALL_RADIUS, window_height / 2 - BALL_RADIUS)

        # Default initial velocity for the ball
        onmouseclicked(self.start)
        self.click = False
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.reset_position)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                if i < 2:
                    self.bricks = GRect(brick_width, brick_height)
                    self.bricks.filled = True
                    self.bricks.fill_color = 'red'
                    self.color = False  # no out line
                    self.window.add(self.bricks, (brick_spacing + brick_width) * j,
                                    brick_offset + (brick_spacing + brick_height) * i)
                elif 1 < i < 4:
                    self.bricks = GRect(brick_width, brick_height)
                    self.bricks.filled = True
                    self.bricks.fill_color = 'orange'
                    self.color = False  # no out line
                    self.window.add(self.bricks, (brick_spacing + brick_width) * j,
                                    brick_offset + (brick_spacing + brick_height) * i)
                elif 3 < i < 6:
                    self.bricks = GRect(brick_width, brick_height)
                    self.bricks.filled = True
                    self.bricks.fill_color = 'yellow'
                    self.color = False  # no out line
                    self.window.add(self.bricks, (brick_spacing + brick_width) * j,
                                    brick_offset + (brick_spacing + brick_height) * i)
                elif 5 < i < 8:
                    self.bricks = GRect(brick_width, brick_height)
                    self.bricks.filled = True
                    self.bricks.fill_color = 'green'
                    self.color = False  # no out line
                    self.window.add(self.bricks, (brick_spacing + brick_width) * j,
                                    brick_offset + (brick_spacing + brick_height) * i)
                elif 7 < i < 10:
                    self.bricks = GRect(brick_width, brick_height)
                    self.bricks.filled = True
                    self.bricks.fill_color = 'blue'
                    self.color = False  # no out line
                    self.window.add(self.bricks, (brick_spacing + brick_width) * j,
                                    brick_offset + (brick_spacing + brick_height) * i)

    def reset_position(self, event):
        if self.paddle.width / 2 < event.x < (
                (BRICK_COLS * (BRICK_WIDTH + BRICK_SPACING)) - BRICK_SPACING) - self.paddle.width / 2:
            new_x = event.x - self.paddle.width / 2  # calculate new position of the paddle
            self.paddle.x = new_x  # renew the position of the paddle

    def start(self, event):
        # Set initial horizontal speed with random direction
        self.click = True
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        #print(self.__dx, self.__dy)

    # set getter for user
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy
