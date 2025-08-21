from turtle import Turtle


class Paddles(Turtle):
    """
    A Paddles class that represents player paddles in the Ping Pong game.
    
    This class extends the Turtle class to create rectangular paddles that
    players can control to hit the ball. Each paddle is 5 times taller than
    the default turtle size and moves in 40-pixel increments.
    
    Methods:
        move_up(): Moves the paddle up by 40 pixels
        move_down(): Moves the paddle down by 40 pixels
    
    Example:
        >>> paddle = Paddles()
        >>> paddle.goto(470, 0)  # Position paddle on right side
        >>> paddle.move_up()     # Move paddle up
        >>> paddle.move_down()   # Move paddle down
    """
    
    def __init__(self):
        """
        Initialize a new Paddles object.
        
        Creates a white rectangular paddle with dimensions 5x1 (height x width)
        relative to the default turtle size. The paddle is positioned at the
        origin (0, 0) with the pen lifted to prevent drawing trails.
        """
        super().__init__()
        self.shape("square")    # Set paddle shape to square (will be stretched)
        self.color("white")     # Set paddle color to white
        self.penup()           # Lift pen to avoid drawing trails
        self.shapesize(5, 1)   # Stretch paddle: 5x height, 1x width

    def move_up(self):
        """
        Move the paddle up by 40 pixels.
        
        Moves the paddle vertically upward while maintaining its current
        horizontal position. This method is typically bound to keyboard
        input for player control.
        
        Example:
            >>> paddle = Paddles()
            >>> initial_y = paddle.ycor()
            >>> paddle.move_up()
            >>> assert paddle.ycor() == initial_y + 40
        """
        self.goto(self.xcor(), self.ycor() + 40)

    def move_down(self):
        """
        Move the paddle down by 40 pixels.
        
        Moves the paddle vertically downward while maintaining its current
        horizontal position. This method is typically bound to keyboard
        input for player control.
        
        Example:
            >>> paddle = Paddles()
            >>> initial_y = paddle.ycor()
            >>> paddle.move_down()
            >>> assert paddle.ycor() == initial_y - 40
        """
        self.goto(self.xcor(), self.ycor() - 40)
