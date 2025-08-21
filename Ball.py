from turtle import Turtle


class Ball(Turtle):
    """
    A Ball class that represents the game ball in the Ping Pong game.
    
    This class extends the Turtle class to create a circular ball that moves
    across the screen with configurable horizontal and vertical movement speeds.
    
    Attributes:
        move_x (int): Horizontal movement speed in pixels per frame (default: 10)
        move_y (int): Vertical movement speed in pixels per frame (default: 10)
    
    Example:
        >>> ball = Ball()
        >>> ball.goto(0, 0)  # Position ball at center
        >>> # Ball will move 10 pixels right and 10 pixels up each frame
        >>> new_x = ball.xcor() + ball.move_x
        >>> new_y = ball.ycor() + ball.move_y
        >>> ball.goto(new_x, new_y)
    """
    
    def __init__(self):
        """
        Initialize a new Ball object.
        
        Creates a white circular ball positioned at the origin (0, 0) with
        initial movement speeds of 10 pixels per frame in both x and y directions.
        The pen is lifted to prevent drawing trails as the ball moves.
        """
        super().__init__()
        self.shape("circle")  # Set ball shape to circle
        self.color("white")   # Set ball color to white
        self.penup()         # Lift pen to avoid drawing trails
        self.move_x = 10     # Initial horizontal movement speed
        self.move_y = 10     # Initial vertical movement speed
