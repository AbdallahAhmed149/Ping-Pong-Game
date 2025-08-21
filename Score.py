from turtle import Turtle


class Scoreboard(Turtle):
    """
    A Scoreboard class for displaying scores in the Ping Pong game.
    
    This class extends the Turtle class to create a text-based scoreboard
    that can display player scores and game messages. The turtle shape is
    hidden to show only the text.
    
    Inherited Methods:
        write(): Display text on the screen
        clear(): Clear the current text
        goto(): Position the scoreboard at specific coordinates
    
    Example:
        >>> scoreboard = Scoreboard()
        >>> scoreboard.goto(100, 250)  # Position for player 1 score
        >>> scoreboard.write("5", font=("Arial", 50, "normal"))
        >>> scoreboard.clear()  # Clear the score
        >>> scoreboard.write("6", font=("Arial", 50, "normal"))
    """
    
    def __init__(self):
        """
        Initialize a new Scoreboard object.
        
        Creates an invisible turtle object that can be used to write text
        on the screen. The turtle shape is hidden so only the text appears,
        and the pen is lifted to prevent drawing lines when moving.
        """
        super().__init__()
        self.shape("turtle")   # Set initial shape (will be hidden)
        self.color("white")    # Set text color to white
        self.penup()          # Lift pen to avoid drawing trails
        self.hideturtle()     # Hide the turtle shape, show only text
