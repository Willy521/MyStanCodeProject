"""
File: babygraphics.py
Name: Chen, Wei Ting
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # find the x coordinate of each index

    return GRAPH_MARGIN_SIZE + year_index * ((width - (2 * GRAPH_MARGIN_SIZE)) / len(YEARS))


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # straight line
    height = 575
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, font='time 15', fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for i in range(len(lookup_names)):
        for j in range(len(YEARS) - 1):
            # pre
            pre_year_x = get_x_coordinate(CANVAS_WIDTH, j)
            if str(YEARS[j]) in str(name_data[lookup_names[i]]):
                pre_rank = int(name_data[lookup_names[i]][str(YEARS[j])])  # real rank
                pre_rank_y = (int(name_data[lookup_names[i]][str(YEARS[j])])) * (
                            CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 + GRAPH_MARGIN_SIZE  # To fit canvas
                # create text
                canvas.create_text(pre_year_x + TEXT_DX, pre_rank_y, text=lookup_names[i] + ' ' + str(pre_rank),
                                   anchor=tkinter.SW, font='time 15', fill='black')
            else:
                pre_rank_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # create text
                canvas.create_text(pre_year_x + TEXT_DX, pre_rank_y, text=lookup_names[i] + ' ' + str('*'),
                                   anchor=tkinter.SW, font='time 15', fill='black')

            # post
            post_year_x = get_x_coordinate(CANVAS_WIDTH, j + 1)
            if str(YEARS[j + 1]) in str(name_data[lookup_names[i]]):
                post_rank = int(name_data[lookup_names[i]][str(YEARS[j + 1])])  # real rank
                post_rank_y = int(name_data[lookup_names[i]][str(YEARS[j + 1])]) * (
                            CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 + GRAPH_MARGIN_SIZE  # To fit canvas
                # create text
                canvas.create_text(post_year_x + TEXT_DX, post_rank_y, text=lookup_names[i] + ' ' + str(post_rank),
                                   anchor=tkinter.SW,
                                   font='time 15', fill='black')
            else:
                post_rank_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # create text
                canvas.create_text(post_year_x + TEXT_DX, post_rank_y, text=lookup_names[i] + ' ' + str('*'),
                                   anchor=tkinter.SW,
                                   font='time 15', fill='black')
            color = COLORS[i % len(COLORS)]

            # draw lines
            canvas.create_line(pre_year_x, pre_rank_y, post_year_x, post_rank_y, width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
