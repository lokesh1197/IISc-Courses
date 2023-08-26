"""
Imports:
Snake.py which contains the Snake class
Food.py which contains the Food class
Turtle module to implement game graphics
"""

import Snake
import Food
import turtle
import time

""""
The main file for the program that implements the Python game using 
the turtle module. 

Global variables:

DELAY: The value after which the main game loop reruns. This sets how 
fast the snake moves. This value is to be slowly decremented as the 
game progresses.

COUNTER: Variable to keep count of the number of elapsed frames since
the last decrement of the DELAY variable.
"""
DELAY = 100
COUNTER = 0


def game_loop() -> None:

    """
    Function that implements the main game loop. All updations are to be
    done in this function. Function should also implement GAME OVER logic
    and do the decrement in DELAY appropriately.
    :return: None
    """

    ############ DO NOT CHANGE ###########
    global DELAY
    global COUNTER
    ######################################
    ########## WRITE BELOW ###############

    def restart_game():
        snake_obj.shape = [(0,0), (20,0)]
        snake_obj.direction = "right"
        snake_obj.GAME_OVER = False

        food_turtle.goto(food_obj.position)
        snake_obj.update_snake()

        screen.listen()
        screen.onkey(snake_obj.go_up, "Up")
        screen.onkey(snake_obj.go_down, "Down")
        screen.onkey(snake_obj.go_right, "Right")
        screen.onkey(snake_obj.go_left, "Left")
        return 100, 0

    food_turtle.goto(food_obj.position)
    snake_obj.update_snake()
    if snake_obj.GAME_OVER:
        time = 15 * (100 - DELAY) + COUNTER
        reply = turtle.textinput(
            "Game Over (Score: " + str(time) + ")",
            "Restart? (Reply with 'y' for yes and anything else for 'no')"
        )
        if reply is "y":
            DELAY, COUNTER = restart_game()
        else:
            turtle.bye()
            return

    if snake_obj.check_food_collision(food_obj.position):
        food_obj.update_random_food_position()
        food_turtle.goto(food_obj.position)

    snake_obj.keep_snake_onscreen()
    snake_turtle.clearstamps()

    for segment in snake_obj.shape:
        snake_turtle.goto(segment[0], segment[1])
        snake_turtle.stamp()

    ######################################
    ########### DO NOT CHANGE ############
    screen.update()

    if DELAY > 10 and COUNTER == 15:
        DELAY -= 1
        COUNTER = 0

    COUNTER += 1

    turtle.ontimer(game_loop, DELAY)
    #######################################



if __name__ == "__main__":
    """
    The main for the program.
    DO NOT CHANGE    
    """
    
    ############ DO NOT CHANGE ############
    screen_height = 500
    screen_width = 500
    start_time = time.time()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Python in Python")
    screen.bgcolor("blue")
    screen.tracer(0)

    snake_obj = Snake.Snake(window_size=(screen_width, screen_height))
    food_obj = Food.Food(window_size=(screen_width, screen_height))
    food_obj.update_random_food_position()

    snake_turtle = turtle.Turtle("square")
    snake_turtle.color(snake_obj.color)
    snake_turtle.penup()

    food_turtle = turtle.Turtle()
    food_turtle.shape(food_obj.shape)
    food_turtle.color(food_obj.color)
    food_turtle.pensize(food_obj.size)
    food_turtle.penup()

    screen.listen()
    screen.onkey(snake_obj.go_up, "Up")
    screen.onkey(snake_obj.go_down, "Down")
    screen.onkey(snake_obj.go_right, "Right")
    screen.onkey(snake_obj.go_left, "Left")

    game_loop()
    turtle.done()
    #########################################
