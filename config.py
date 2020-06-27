WIDTH = 10
HEIGHT = 20
BLOCK_SIZE = 40
LINE_WIDTH = 5
FALL_MOVES = 1
CROSS_LINE_WIDTH = 10
WIN_SIZE = (
    (WIDTH + 3) * BLOCK_SIZE + LINE_WIDTH * (WIDTH + 6) + CROSS_LINE_WIDTH,
    HEIGHT * BLOCK_SIZE + LINE_WIDTH * (HEIGHT + 1)
)
FPS = 10

# Machine Learning
ACTIONS = ['L', 'R', 'U', 'D']
GAMMA = 0.95
EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.001
LEARNING_RATE = 0.001
BATCH_SIZE = 64

FIGURE_SHAPES = [
    {
        "grid_size": 3,
        "color": (123, 104, 238),
        "positions": [
            [1, 2, 4, 7],
            [3, 4, 5, 8],
            [1, 4, 7, 6],
            [0, 3, 4, 5],
        ]
    },
    {
        "grid_size": 3,
        "color": (255, 128, 0),
        "positions": [
            [0, 1, 4, 7],
            [2, 3, 4, 5],
            [1, 4, 7, 8],
            [3, 4, 5, 6],
        ]
    },
    {
        "grid_size": 3,
        "color": (186, 85, 211),
        "positions": [
            [1, 3, 4, 5],
            [1, 4, 5, 7],
            [3, 4, 5, 7],
            [1, 3, 4, 7],
        ]
    },
    {
        "grid_size": 4,
        "color": (0, 191, 255),
        "positions": [
            [1, 5, 9, 13],
            [4, 5, 6, 7],
            [2, 6, 10, 14],
            [8, 9, 10, 11],
        ]
    },
    {
        "grid_size": 3,
        "color": (0, 255, 127),
        "positions": [
            [1, 2, 3, 4],
            [1, 4, 5, 8],
            [4, 5, 6, 7],
            [0, 3, 4, 7],
        ]
    },
    {
        "grid_size": 3,
        "color": (255, 0, 0),
        "positions": [
            [0, 1, 4, 5],
            [2, 4, 5, 7],
            [3, 4, 7, 8],
            [1, 3, 4, 6],
        ]
    },
    {
        "grid_size": 2,
        "color": (255, 255, 51),
        "positions": [
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
        ]
    }
]