class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################

        self.__offsets__ = {
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0),
        }
        self.shape = [(0,0), (20,0)]
        self.direction = "right"
        self.color = "yellow"
        self.window_size = window_size
        self.GAME_OVER = False

        ###########################################

    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############

        if self.direction != "down":
            self.direction = "up"

        ##########################################

    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        if self.direction != "up":
            self.direction = "down"

        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        if self.direction != "right":
            self.direction = "left"

        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        if self.direction != "left":
            self.direction = "right"

        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############

        x1, y1 = self.shape[-1]
        x2, y2 = current_food_position
        if abs(x1 - x2) < 20 and abs(y1 - y2) < 20:
            return True

        self.shape.pop(0)
        return False

        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############

        self.shape[-1] = list(self.shape[-1])
        if self.shape[-1][0] > self.window_size[0] / 2:
            self.shape[-1][0] -= self.window_size[0]
        elif self.shape[-1][0] < - self.window_size[0] / 2:
            self.shape[-1][0] += self.window_size[0]
        elif self.shape[-1][1] > self.window_size[1] / 2:
            self.shape[-1][1] -= self.window_size[1]
        elif self.shape[-1][1] < -self.window_size[1] / 2:
            self.shape[-1][1] += self.window_size[1]
        self.shape[-1] = tuple(self.shape[-1])

        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """

        ############## WRITE BELOW ###############

        next_pos = list(self.shape[-1]).copy()
        next_pos[0] = self.shape[-1][0] + self.__offsets__[self.direction][0]
        next_pos[1] = self.shape[-1][1] + self.__offsets__[self.direction][1]

        if tuple(next_pos) in self.shape[:-1]:
            self.GAME_OVER = True
        else:
            self.shape.append(tuple(next_pos))

        ##########################################









