"""
Created by Alejandro Barroso num:499081 in 04 Mar 2024
Universidad Carlos III de Madrid
"""
"""
Created by Juan José Rosales (100499176) in feb 2024
Universidad Carlos III de Madrid
"""

"""
Snake Eater
Made with PyGame
Last modification in January 2024 by José Carlos Pulido
Machine Learning Classes - University Carlos III of Madrid
"""

import pygame, sys, time, random,math

# DIFFICULTY settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120

DIFFICULTY = 15

# Window size
FRAME_SIZE_X = 480
FRAME_SIZE_Y = 480

# Colors (R, G, B)
BLACK = pygame.Color(51, 51, 51)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(204, 51, 0)
GREEN = pygame.Color(204, 255, 153)
BLUE = pygame.Color(0, 51, 102)


# GAME STATE CLASS
class GameState:
    def __init__(self, FRAME_SIZE):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        self.food_pos = [random.randrange(1, (FRAME_SIZE[0] // 10)) * 10,
                         random.randrange(1, (FRAME_SIZE[1] // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        # Add a variable with the length of the body
        self.body_length = len(self.snake_body)
        self.body_up = False
        self.body_down = False
        self.body_left = True
        self.body_right = False
        self.previous_dir = 'RIGHT'
        self.previous_dist = 0


# Game Over
def game_over(game):
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, WHITE)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (FRAME_SIZE_X / 2, FRAME_SIZE_Y / 4)
    game_window.fill(BLUE)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(game, 0, WHITE, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(game, choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(game.score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (FRAME_SIZE_X / 8, 15)
    else:
        score_rect.midtop = (FRAME_SIZE_X / 2, FRAME_SIZE_Y / 1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Move the snake
def move_keyboard(game, event):
    # Whenever a key is pressed down
    change_to = game.direction
    current_dir = game.direction
    if event.type == pygame.KEYDOWN:
        # W -> Up; S -> Down; A -> Left; D -> Right
        if (event.key == pygame.K_UP or event.key == ord(
                'w')) and game.direction != 'DOWN':
            change_to = 'UP'
        if (event.key == pygame.K_DOWN or event.key == ord(
                's')) and game.direction != 'UP':
            change_to = 'DOWN'
        if (event.key == pygame.K_LEFT or event.key == ord(
                'a')) and game.direction != 'RIGHT':
            change_to = 'LEFT'
        if (event.key == pygame.K_RIGHT or event.key == ord(
                'd')) and game.direction != 'LEFT':
            change_to = 'RIGHT'

    if change_to != game.direction:
        game.previous_dir = game.direction

    return change_to


# TODO: IMPLEMENT HERE THE NEW INTELLIGENT METHOD
def move_tutorial_1(game):

    direction = game.direction
    if game.direction == "UP":
        if game.food_pos[0] < game.snake_pos[0]:  # food left
            if game.food_pos[1] < game.snake_pos[1]:  # food up
                if not free_position(game.direction):
                    direction = possible_loop("LEFT")
            else:  # food down
                direction = possible_loop("LEFT")

        else:  # food right
            if game.food_pos[1] < game.snake_pos[1]:  # food up
                if not free_position(game.direction):
                    direction = possible_loop("RIGHT")
            else:  # food down
                direction = possible_loop("RIGHT")

    if game.direction == "DOWN":  # ****************************************
        if game.food_pos[0] < game.snake_pos[0]:  # food left
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                if not free_position(game.direction):
                    direction = possible_loop("LEFT")
            else:  # food up
                direction = possible_loop("LEFT")

        else:  # food right
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                if not free_position(game.direction):
                    direction = possible_loop("RIGHT")

            else:  # food up
                direction = possible_loop("RIGHT")

    if game.direction == "RIGHT":  # ****************************************
        if game.food_pos[0] > game.snake_pos[0]:  # food right
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                if not free_position(game.direction):
                    direction = possible_loop("DOWN")
            else:  # food up
                if not free_position(game.direction):
                    direction = possible_loop("UP")

        else:  # food left
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                direction = possible_loop("DOWN")

            else:  # food up
                direction = possible_loop("UP")

    if game.direction == "LEFT":  # ****************************************
        if game.food_pos[0] < game.snake_pos[0]:  # food left
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                if not free_position(game.direction):
                    direction = possible_loop("DOWN")
            else:  # food up
                if not free_position(game.direction):
                    direction = possible_loop("UP")

        else:  # food right
            if game.food_pos[1] > game.snake_pos[1]:  # food down
                direction = possible_loop("DOWN")

            else:  # food up
                direction = possible_loop("UP")

    # Call to the function possible_direction to check if the decision is correct
    # If not correct choose a correct random position
    available = possible_direction(game)
    if len(available) != 0 and direction not in available:
        direction = available[random.randint(0, len(available) - 1)]

    if direction != game.direction:
        game.previous_dir = game.direction

    return direction


def free_position(dir):
    '''
    Check if there is danger on the next possible snake position.
    :param dir: direction of next intended movement
    :return: a boolean saying if the next intended position is free or not.
    '''
    is_free = True
    if dir == "UP":
        next_x = game.snake_pos[0]
        next_y = game.snake_pos[1] - 10
    elif dir == "DOWN":
        next_x = game.snake_pos[0]
        next_y = game.snake_pos[1] + 10
    elif dir == "RIGHT":
        next_x = game.snake_pos[0] + 10
        next_y = game.snake_pos[1]
    else:
        next_x = game.snake_pos[0] - 10
        next_y = game.snake_pos[1]

    if next_x >= FRAME_SIZE_X or next_y >= FRAME_SIZE_Y:
        is_free = False
    else:
        for element in game.snake_body:
            if element[0] == next_x and element[1] == next_y:
                is_free = False
    return is_free


def possible_loop(dir):
    """
    Insert the intended new direction and see if there is a danger of
    entering a loop
    :param dir: intended new direction
    :return:
    """
    if free_position(dir):
        new_dir = dir
    else:
        new_dir = game.direction
    for element in game.snake_body:
        if dir == "UP" and element[0] == game.snake_pos[0] and element[1] < \
                game.snake_pos[1]:
            if free_position("DOWN"):
                new_dir = "DOWN"

        if dir == "DOWN" and element[0] == game.snake_pos[0] and element[1] > \
                game.snake_pos[1]:
            if free_position("UP"):
                new_dir = "UP"

        if dir == "LEFT" and element[1] == game.snake_pos[1] and element[0] < \
                game.snake_pos[0]:
            if free_position("RIGHT"):
                new_dir = "RIGHT"

        if dir == "RIGHT" and element[1] == game.snake_pos[1] and element[0] \
                > game.snake_pos[0]:
            if free_position("LEFT"):
                new_dir = "LEFT"

    return new_dir


# FUNCTION TO CHECK WHAT DIRECTIONS ARE POSSIBLE.
def possible_direction(game,posX = 0,posY = 0):
    possibilities = []
    posX = game.snake_pos[0] + posX
    posY = game.snake_pos[1] + posY

    if (posY - 10 >= 0) and ([posX, posY - 10] not
                                          in game.snake_body):
        if free_position("UP"):
            possibilities.append("UP")
    if posX + 10 <= 470 and ([posX + 10, posY] not
                                          in game.snake_body):
        if free_position("RIGHT"):
            possibilities.append("RIGHT")
    if posX - 10 >= 0 and ([posX - 10, posY] not
                                        in game.snake_body):
        if free_position("LEFT"):
            possibilities.append("LEFT")
    if posY + 10 <= 470 and ([posX, posY + 10] not
                                          in game.snake_body):
        if free_position("DOWN"):
            possibilities.append("DOWN")
    return possibilities



# PRINTING DATA FROM GAME STATE
def print_state(game):
    print("--------GAME STATE--------")
    print("FrameSize:", FRAME_SIZE_X, FRAME_SIZE_Y)
    print("Previous Direction:", game.previous_dir)
    print("Direction:", game.direction)
    print("Snake X:", game.snake_pos[0], ", Snake Y:", game.snake_pos[1])
    print("Snake Body:", game.snake_body)
    print("Food X:", game.food_pos[0], ", Food Y:", game.food_pos[1])
    print("Score:", game.score)
    print("Length:", game.body_length)
    print("Body Up:", game.body_up)
    print("Body Down:", game.body_down)
    print("Body Left:", game.body_left)
    print("Body Right:", game.body_right)


# ARFF file creation
def print_line_data(game):

    header = '''@RELATION snake_game
@ATTRIBUTE snake_posX NUMERIC
@ATTRIBUTE snake_posY NUMERIC
@ATTRIBUTE food_posX NUMERIC
@ATTRIBUTE food_posY NUMERIC
@ATTRIBUTE RIGHT {1,0}
@ATTRIBUTE LEFT {1,0}
@ATTRIBUTE UP {1,0}
@ATTRIBUTE DOWN {1,0}
@ATTRIBUTE good_move {RIGHT,LEFT,UP,DOWN}
@ATTRIBUTE body_up {1,0}
@ATTRIBUTE body_down {1,0}
@ATTRIBUTE body_left {1,0}
@ATTRIBUTE body_right {1,0}
@ATTRIBUTE body_length NUMERIC
@ATTRIBUTE previous_direction {1,2,3,4}
@ATTRIBUTE distance_to_food NUMERIC
@ATTRIBUTE distance_x NUMERIC
@ATTRIBUTE distance_y NUMERIC
@ATTRIBUTE rel_pos {1,2,3,4}
@ATTRIBUTE x_rel_pos {RIGHT,LEFT,SAME}
@ATTRIBUTE y_rel_pos {UP,DOWN,SAME}
@ATTRIBUTE same_x {1,0}
@ATTRIBUTE same_y {1,0}
@ATTRIBUTE closer_to_food {1,0}
@ATTRIBUTE score NUMERIC
@ATTRIBUTE direction {1,2,3,4}
@ATTRIBUTE next_score NUMERIC
@DATA
    '''
    if f.tell() == 0:
        f.write(header + "\n")

    data_entry_template = '{},{},{},{},{},{},{},{},{},{},' \
                          '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'

    # Assuming `possible_direction` returns a list of possible directions
    possible_directions = possible_direction(game)

    # Convert boolean values to lowercase strings
    right = int("RIGHT" in possible_directions)
    left = int("LEFT" in possible_directions)
    up = int("UP" in possible_directions)
    down = int("DOWN" in possible_directions)

    # Codify game direction: UP-1 ; RIGHT-2 ; DOWN-3 ; LEFT-4 (clockwise)
    if game.direction == "UP":
        dir = "1"
    elif game.direction == "RIGHT":
        dir = "2"
    elif game.direction == "DOWN":
        dir = "3"
    else:
        dir = "4"

    # Codify game direction: UP-1 ; RIGHT-2 ; DOWN-3 ; LEFT-4 (clockwise)
    if game.previous_dir == "UP":
        previous_dir = "1"
    elif game.previous_dir == "RIGHT":
        previous_dir = "2"
    elif game.previous_dir == "DOWN":
        previous_dir = "3"
    else:
        previous_dir = "4"

    # Calculate distance to food
    def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    distance_to_food = distance(game.snake_pos[0], game.snake_pos[1],
                                game.food_pos[0], game.food_pos[1])

    # Calculate distance in X-axis and Y-axis
    distance_x = game.snake_pos[0] - game.food_pos[0]
    distance_y = game.snake_pos[1] - game.food_pos[1]

    # Determine x an y food positions with respect to snake's head:
    if game.snake_pos[0] < game.food_pos[0]:
        x_rel_pos = "RIGHT"
    elif game.snake_pos[0] > game.food_pos[0]:
        x_rel_pos = "LEFT"
    else:
        # Same x
        x_rel_pos = "SAME"

    if game.snake_pos[1] < game.food_pos[1]:
        y_rel_pos = "DOWN"
    elif game.snake_pos[1] > game.food_pos[1]:
        y_rel_pos = "UP"
    else:
        # Same y
        y_rel_pos = "SAME"


    # Check if the movement has brought the snake closer to the food
    closer_to_food = 1 if distance_to_food < game.previous_dist else 0

    # Update previous distance to food for the next iteration
    game.previous_dist = distance_to_food

    # Define discretization function
    def discretize_coordinate(value, max_size, interval):
        interval_size = max_size / interval  # Divide the range into 4 intervals
        return min(int(value / interval_size), interval-1)  # Ensure the
        # maximum value is 3

    # Discretize variables
    discrete_snake_posX = discretize_coordinate(game.snake_pos[0], 480,4)
    discrete_snake_posY = discretize_coordinate(game.snake_pos[1], 480,4)
    discrete_food_posX = discretize_coordinate(game.food_pos[0], 480,4)
    discrete_food_posY = discretize_coordinate(game.food_pos[1], 480,4)
    #discrete_distance_to_food = discretize_coordinate(int(
    # distance_to_food), 480,10)

    # Relative position of food from snakes head (quadrant number if snake
    # head was the 0,0) -->
    if game.snake_pos[0] < game.food_pos[0] and game.snake_pos[1] >= \
            game.food_pos[1]:
        rel_pos = 1 # 1st quadrant
    elif game.snake_pos[0] >= game.food_pos[0] and game.snake_pos[1] > \
            game.food_pos[1]:
        rel_pos = 2 # 2nd quadrant
    elif game.snake_pos[0] > game.food_pos[0] and game.snake_pos[1] <= \
            game.food_pos[1]:
        rel_pos = 3 # 3rd quadrant
    else:
        rel_pos = 4 # 4th quadrant

    # good_move --> when snake reduces distance to food in that dir
    # without dying
    if right and x_rel_pos == "RIGHT":
        good_move = "RIGHT"
    elif left and x_rel_pos == "LEFT":
        good_move = "LEFT"
    elif up and y_rel_pos == "UP":
        good_move = "UP"
    elif down and y_rel_pos == "DOWN":
        good_move = "DOWN"
    # If we cannot get closer to the apple due to collisions:
    elif right:
        good_move = "RIGHT"
    elif left:
        good_move = "LEFT"
    elif up:
        good_move = "UP"
    elif down:
        good_move = "DOWN"
    # no direction available:
    else:
        good_move = "RIGHT"

    same_x = 1 if game.snake_pos[0] == game.food_pos[0] else 0
    same_y = 1 if game.snake_pos[1] == game.food_pos[1] else 0

    # Construct the data entry string
    data_entry = data_entry_template.format(
        game.snake_pos[0],
        game.snake_pos[1],
        game.food_pos[0],
        game.food_pos[1],
        right,
        left,
        up,
        down,
        good_move,
        int(game.body_up),
        int(game.body_down),
        int(game.body_right),
        int(game.body_left),
        game.body_length,
        previous_dir,
        distance_to_food,
        distance_x,
        distance_y,
        rel_pos,
        x_rel_pos,
        y_rel_pos,
        same_x,
        same_y,
        closer_to_food,
        game.score,
        dir,
    )

    if game.score == -1 and game.body_length == 3:
        # The first instance of a new game
        result = "\n" + data_entry
    elif (dir == "1" and up) or (dir == "2" and right) or (dir == "3"
        and down) or (dir == "4" and left):
        # Good move, still alive
        result = str(game.score) + "\n" + data_entry
    else:
        # Does not print last tick (when it dies)
        # result = str(game.score)
        # Prints last tick
        result = str(game.score) + "\n" + data_entry + str(game.score)

    return result


# Checks for errors encounteRED
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Snake Eater - Machine Learning (UC3M)')
game_window = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Open csv file, with parameter "a" we create a new one just if it does not already exist.
f = open("data_test.arff", "a")




# Main logic
game = GameState((FRAME_SIZE_X, FRAME_SIZE_Y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        # CALLING MOVE METHOD
        game.direction = move_keyboard(game, event)

    # UNCOMMENT WHEN METHOD IS IMPLEMENTED
    # game.direction = move_tutorial_1(game)

    # Moving the snake
    if game.direction == 'UP':
        game.snake_pos[1] -= 10
    if game.direction == 'DOWN':
        game.snake_pos[1] += 10
    if game.direction == 'LEFT':
        game.snake_pos[0] -= 10
    if game.direction == 'RIGHT':
        game.snake_pos[0] += 10

    # Detection of body
    game.body_up = False
    game.body_down = False
    game.body_left = False
    game.body_right = False
    for element in game.snake_body:
        if element[0] == game.snake_pos[0] and element[1] < game.snake_pos[1]:
            game.body_up = True
        if element[0] == game.snake_pos[0] and element[1] > game.snake_pos[1]:
            game.body_down = True
        if element[1] == game.snake_pos[1] and element[0] < game.snake_pos[0]:
            game.body_left = True
        if element[1] == game.snake_pos[1] and element[0] > game.snake_pos[0]:
            game.body_right = True

    # Snake body growing mechanism
    game.snake_body.insert(0, list(game.snake_pos))
    if game.snake_pos[0] == game.food_pos[0] and game.snake_pos[1] == game.food_pos[1]:
        game.score += 100
        game.food_spawn = False
        # Add 1 to length.
        game.body_length += 1
    else:
        game.snake_body.pop()
        game.score -= 1

    # Spawning food on the screen
    if not game.food_spawn:
        game.food_pos = [random.randrange(1, (FRAME_SIZE_X // 10)) * 10,
                         random.randrange(1, (FRAME_SIZE_Y // 10)) * 10]
    game.food_spawn = True

    # GFX
    game_window.fill(BLUE)
    for pos in game.snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, RED,
                     pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if game.snake_pos[0] < 0 or game.snake_pos[0] > FRAME_SIZE_X - 10:
        game_over(game)
    if game.snake_pos[1] < 0 or game.snake_pos[1] > FRAME_SIZE_Y - 10:
        game_over(game)
    # Touching the snake body
    for block in game.snake_body[1:]:
        if game.snake_pos[0] == block[0] and game.snake_pos[1] == block[1]:
            game_over(game)

    show_score(game, 1, WHITE, 'consolas', 15)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(DIFFICULTY)
    # PRINTING STATE
    print_state(game)
    #Write information into the csv file
    f.write(print_line_data(game))



#Close the file
f.close()
