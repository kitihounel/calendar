from datetime import datetime, timedelta
from itertools import product


def create_grid_with_two_lines(rows, cols, texts):
    """
    Creates a string representation of a grid with two lines of colored and bold text per box.

    Args:
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.
        texts (list): A list of tuples, where each tuple contains a list of two strings
                      and the color ('green' or 'black').
    """
    box_width = 12
    border_horizontal = '─'
    border_vertical = '│'
    corner_top_left = '╭'
    corner_top_right = '╮'
    corner_bottom_left = '╰'
    corner_bottom_right = '╯'
    t_junction_top = '┬'
    t_junction_bottom = '┴'
    t_junction_left = '├'
    t_junction_right = '┤'
    cross = '┼'

    green_bold_color = '\033[1;92m'
    reset_color = '\033[0m'

    grid_str = ''
    text_index = 0

    for r in range(rows):
        # Top border
        if r == 0:
            grid_str += corner_top_left + (border_horizontal * box_width + t_junction_top) * (cols - 1) + border_horizontal * box_width + corner_top_right + '\n'
        else:
            grid_str += t_junction_left + (border_horizontal * box_width + cross) * (cols - 1) + border_horizontal * box_width + t_junction_right + '\n'

        # First line of content
        row_content_line1 = ''
        for c in range(cols):
            lines, color = texts[text_index + c]
            text_padded = lines[0].center(box_width)
            color_code = green_bold_color if color == 'green' else ''
            row_content_line1 += border_vertical + color_code + text_padded + reset_color
        row_content_line1 += border_vertical + '\n'
        grid_str += row_content_line1

        # Second line of content
        row_content_line2 = ''
        for c in range(cols):
            lines, color = texts[text_index + c]
            text_padded = lines[1].center(box_width)
            color_code = green_bold_color if color == 'green' else ''
            row_content_line2 += border_vertical + color_code + text_padded + reset_color
        row_content_line2 += border_vertical + '\n'
        grid_str += row_content_line2

        text_index += cols

    # Bottom border
    grid_str += corner_bottom_left + (border_horizontal * box_width + t_junction_bottom) * (cols - 1) + border_horizontal * box_width + corner_bottom_right + '\n'

    return grid_str


date_input = input('Enter the date you saw the moon in yyyy-mm-dd format: ')
start_date = None
try:
    # Parse the input string into a datetime object
    start_date = datetime.strptime(date_input, '%Y-%m-%d')
except ValueError:
    print('Invalid format. Please use yyyy-mm-dd. For example: 2023-12-25')
    exit()

days = ['Mj', 'Mk', 'Vd', 'Az', 'Vo', 'Ak', 'Bo', 'Hn', 'Fa']
cycle_length = len(days)
cycle_count = 3

texts = []
for i, j in product(range(cycle_count), range(cycle_length)):
    delta = i * cycle_length + j
    current_date = start_date + timedelta(days=delta)
    lines = [current_date.strftime('%a %d %b'), days[j]]
    color = 'green' if j % 2 == 0 else 'black'
    texts.append((lines, color))

grid_output = create_grid_with_two_lines(cycle_count, cycle_length, texts)
print('Here are the next three cycles:')
print(grid_output)
