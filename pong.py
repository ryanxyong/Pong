# Author: Ryan Yong
# Date: October 2, 2020
# Purpose: To recreate the pong game found in Atari

from cs1lib import *

# Defines constants
WINDOW_SIZE = 400
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_MOVE_SPEED = 10
BALL_RADIUS = 10
INITIAL_BALL_VX = 5
INITIAL_BALL_VY = 7

# Defines variables for ball
ball_x = WINDOW_SIZE/2
ball_y = WINDOW_SIZE/2
ball_vx = INITIAL_BALL_VX
ball_vy = INITIAL_BALL_VY

# Defines variables for paddle
left_paddle_y = 0
right_paddle_y = WINDOW_SIZE

# Defines key presses
a_pressed = False
z_pressed = False
k_pressed = False
m_pressed = False
q_pressed = False
space_pressed = False


# Sets the background to black
def set_background_black():
    set_clear_color(0, 0, 0)
    clear()


# Draws the pong paddles
def draw_paddles():
    set_fill_color(.5, .5, .5)
    draw_rectangle(0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(WINDOW_SIZE, right_paddle_y, -PADDLE_WIDTH, -PADDLE_HEIGHT)


# Draws the pong ball
def draw_ball():
    set_fill_color(1, 1, 1)
    draw_circle(ball_x, ball_y, BALL_RADIUS)


# Checks if specific key is pressed
def my_kpress(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, q_pressed, space_pressed

    if key == "a":
        a_pressed = True
    if key == "z":
        z_pressed = True
    if key == "k":
        k_pressed = True
    if key == "m":
        m_pressed = True
    if key == "q":
        q_pressed = True
    if key == " ":
        space_pressed = True


# Checks if specific key is released
def my_krelease(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, q_pressed, space_pressed

    if key == "a":
        a_pressed = False
    if key == "z":
        z_pressed = False
    if key == "k":
        k_pressed = False
    if key == "m":
        m_pressed = False
    if key == "q":
        q_pressed = False
    if key == " ":
        space_pressed = False


# Determines if the ball hit a wall
def hit_wall(position):
    contact = False

    # Sees if the ball's outer edge hits a wall (left or right side of the window)
    if position <= BALL_RADIUS or position >= WINDOW_SIZE - BALL_RADIUS:
        contact = True

    return contact


# Determines if the ball hit a paddle
def hit_paddle(position_x, position_y):
    contact = False

    # Sees if the ball's outer edge hits the left paddle
    if position_x <= PADDLE_WIDTH + BALL_RADIUS and left_paddle_y <= position_y <= left_paddle_y + PADDLE_HEIGHT:
        contact = True
    # Sees if the ball's outer edge hits the right paddle
    elif position_x >= WINDOW_SIZE - PADDLE_WIDTH - BALL_RADIUS and right_paddle_y - PADDLE_HEIGHT <= position_y <= right_paddle_y:
        contact = True

    return contact


# Main draw function for the pong game
def my_pong():
    global ball_x, ball_y, ball_vx, ball_vy, right_paddle_y, left_paddle_y

    set_background_black()
    draw_paddles()
    draw_ball()

    # Bounces the ball in the opposite horizontal direction if it hits a paddle
    if hit_paddle(ball_x, ball_y):
        ball_vx *= -1
        ball_x += ball_vx

    # Stops the ball if it hits a vertical (left or right side) wall and ends the game with game over text
    if hit_wall(ball_x):
        ball_vx = 0
        ball_vy = 0
        set_stroke_color(1, 1, 1)
        draw_text("Game Over! Press the space bar to restart.", WINDOW_SIZE/5, WINDOW_SIZE/2)
    # Lets the ball continue moving if it does not hit a wall
    else:
        ball_x += ball_vx

    # Bounces the ball in the opposite vertical direction if it hits a horizontal (top or bottom side) wall
    if hit_wall(ball_y):
        ball_vy *= -1
        ball_y += ball_vy
    # Lets the ball continue moving if it does not hit a wall
    else:
        ball_y += ball_vy

    # Moves the left paddle up if "a" is pressed
    if a_pressed and (left_paddle_y - PADDLE_MOVE_SPEED) >= 0:
        left_paddle_y -= PADDLE_MOVE_SPEED
    # Moves the left paddle down if "z" is pressed
    if z_pressed and (left_paddle_y + PADDLE_HEIGHT + PADDLE_MOVE_SPEED) <= WINDOW_SIZE:
        left_paddle_y += PADDLE_MOVE_SPEED
    # Moves the right paddle up if "k" is pressed
    if k_pressed and (right_paddle_y - PADDLE_HEIGHT - PADDLE_MOVE_SPEED) >= 0:
        right_paddle_y -= PADDLE_MOVE_SPEED
    # Moves the right paddle down if "m" is pressed
    if m_pressed and (right_paddle_y + PADDLE_MOVE_SPEED) <= WINDOW_SIZE:
        right_paddle_y += PADDLE_MOVE_SPEED
    # Quits the game when "q" is pressed
    if q_pressed:
        cs1_quit()
    # Restarts the game when the space bar is pressed
    if space_pressed:
        left_paddle_y = 0
        right_paddle_y = WINDOW_SIZE

        ball_x = WINDOW_SIZE/2
        ball_y = WINDOW_SIZE/2

        ball_vx = INITIAL_BALL_VX
        ball_vy = INITIAL_BALL_VY


start_graphics(my_pong, key_press=my_kpress, key_release=my_krelease)
