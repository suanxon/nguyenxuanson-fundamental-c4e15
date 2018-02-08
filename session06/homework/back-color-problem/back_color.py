from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    i = randint(0, len(shapes) - 1)
    shapes_dictionary = shapes[i]
    text = shapes_dictionary['text']
    j = randint(0, len(shapes) - 1)
    shapes_color = shapes[j]
    color = shapes_color['color']


    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    print(x, y, text, color, quiz_type)
    list_rect =[]
    for i in range(4):
        shapes_dictionary = shapes[i]
        rect = shapes_dictionary['rect']
        list_rect.append(rect)
    blue_rect = list_rect[0]
    red_rect = list_rect[1]
    yellow_rect = list_rect[2]
    green_rect = list_rect[3]
    if quiz_type == 0:
        if text == "blue" and x >= blue_rect[0] and x <= blue_rect[0] + blue_rect[2] and y >= blue_rect[1] and y <= blue_rect[1] + blue_rect[3]:
            return True
        elif text == "red" and x >= red_rect[0] and x <= red_rect[0] + red_rect[2] and y >= red_rect[1] and y <= red_rect[1] + red_rect[3]:
            return True
        elif text == "yellow" and x >= yellow_rect[0] and x <= yellow_rect[0] + yellow_rect[2] and y >= yellow_rect[1] and y <= yellow_rect[1] + yellow_rect[3]:
            return True
        elif text == "green" and x >= green_rect[0] and x <= green_rect[0] + green_rect[2] and y >= green_rect[1] and y <= green_rect[1] + green_rect[3]:
            return True
        else:
            return False
    else:
        if color == '#3F51B5' and x >= blue_rect[0] and x <= blue_rect[0] + blue_rect[2] and y >= blue_rect[1] and y <= blue_rect[1] + blue_rect[3]:
            return True
        elif color == '#C62828' and x >= red_rect[0] and x <= red_rect[0] + red_rect[2] and y >= red_rect[1] and y <= red_rect[1] + red_rect[3]:
            return True
        elif color == '#FFD600' and x >= yellow_rect[0] and x <= yellow_rect[0] + yellow_rect[2] and y >= yellow_rect[1] and y <= yellow_rect[1] + yellow_rect[3]:
            return True
        elif color == '#4CAF50' and x >= green_rect[0] and x <= green_rect[0] + green_rect[2] and y >= green_rect[1] and y <= green_rect[1] + green_rect[3]:
            return True
        else:
            return False

