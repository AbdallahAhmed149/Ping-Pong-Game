"""
Ping Pong Game - Main Module

This is the main entry point for a two-player Ping Pong game built using Python's
Turtle graphics library. The game features real-time gameplay with ball physics,
collision detection, score tracking, and win conditions.

Game Features:
- Two-player controls (arrow keys and WASD)
- Real-time ball physics with wall and paddle collisions
- Dynamic scoring system with speed increases
- Win condition at 10 points with victory screen
- 1000x700 pixel game window with black background

Controls:
- Player 1 (Right Paddle): Up/Down arrow keys
- Player 2 (Left Paddle): W/S keys
- Exit: Click the game window after game ends

Dependencies:
- turtle (Python standard library)
- time (Python standard library)
- Ball.py (custom Ball class)
- Brackets.py (custom Paddles class)  
- Score.py (custom Scoreboard class)

Author: Ping Pong Game Developer
Version: 1.0
"""

from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard
import time

# ============================================================================
# GAME INITIALIZATION
# ============================================================================

# Initialize the game window
window = Screen()
window.title("Welcome to the PingPong Game!")
window.bgcolor("black")              # Set background color to black
window.setup(width=1000, height=700) # Set window dimensions
window.tracer(0)                     # Turn off animation for manual updates

# ============================================================================
# SCOREBOARD SETUP
# ============================================================================

# Player 1 scoreboard (right side)
board1 = Scoreboard()
score1 = 0                           # Initialize Player 1 score
board1.goto(100, 250)               # Position scoreboard on right
board1.write(f"{score1}", font=("bold", 50, "normal"))

# Player 2 scoreboard (left side)  
board2 = Scoreboard()
score2 = 0                           # Initialize Player 2 score
board2.goto(-100, 250)              # Position scoreboard on left
board2.write(f"{score2}", font=("bold", 50, "normal"))

# ============================================================================
# PADDLE SETUP AND CONTROLS
# ============================================================================

# Player 1 paddle (right side) - Arrow key controls
paddle1 = Paddles()
paddle1.goto(470, 0)                # Position paddle on right side
window.listen()                      # Enable keyboard input
window.onkey(paddle1.move_up, "Up")    # Bind Up arrow to paddle movement
window.onkey(paddle1.move_down, "Down") # Bind Down arrow to paddle movement

# Player 2 paddle (left side) - WASD controls
paddle2 = Paddles()
paddle2.goto(-470, 0)               # Position paddle on left side
window.onkey(paddle2.move_up, "w")     # Bind W key to paddle movement
window.onkey(paddle2.move_down, "s")   # Bind S key to paddle movement

# ============================================================================
# BALL SETUP AND GAME VARIABLES
# ============================================================================

ball = Ball()                        # Create the game ball
speed = 0.1                         # Initial game speed (delay between frames)

# ============================================================================
# MAIN GAME LOOP
# ============================================================================

game_on = True
while game_on:
    # Update the display and control frame rate
    window.update()                  # Refresh the screen with new positions
    time.sleep(speed)               # Control game speed (lower = faster)
    
    # Move the ball based on current velocity
    ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
    
    # ========================================================================
    # WALL COLLISION DETECTION (Top and Bottom)
    # ========================================================================
    
    # Bounce ball off top and bottom walls (y-axis boundaries)
    if ball.ycor() >= 340 or ball.ycor() <= -340:
        ball.move_y *= -1           # Reverse vertical direction
    
    # ========================================================================
    # PADDLE COLLISION DETECTION
    # ========================================================================
    
    # Check collision with right paddle (Player 1) or left paddle (Player 2)
    # Ball must be near paddle position AND within collision distance
    if (ball.xcor() >= 450 and ball.distance(paddle1) <= 50) or (
        ball.xcor() <= -450 and ball.distance(paddle2) <= 50
    ):
        ball.move_x *= -1           # Reverse horizontal direction
    
    # ========================================================================
    # SCORING SYSTEM
    # ========================================================================
    
    # Player 2 scores (ball passes right boundary)
    if ball.xcor() > 510:
        score2 += 1                 # Increment Player 2 score
        board2.clear()              # Clear old score display
        board2.write(f"{score2}", font=("bold", 50, "normal"))
        speed *= 0.5                # Increase game speed (reduce delay)
        ball.goto(0, 0)            # Reset ball to center
        ball.move_x *= -1          # Change ball direction
    
    # Player 1 scores (ball passes left boundary)
    if ball.xcor() < -510:
        score1 += 1                 # Increment Player 1 score
        board1.clear()              # Clear old score display
        board1.write(f"{score1}", font=("bold", 50, "normal"))
        speed *= 0.5                # Increase game speed (reduce delay)
        ball.goto(0, 0)            # Reset ball to center
        ball.move_x *= -1          # Change ball direction
    
    # ========================================================================
    # WIN CONDITIONS
    # ========================================================================
    
    # Player 1 wins (reaches 10 points)
    if score1 == 10:
        game_on = False             # End the game loop
        window.clear()              # Clear the game screen
        window.bgcolor("red")       # Set victory background color
        board1.goto(0, 0)          # Center the victory message
        board1.write(
            "*******Player_1 WIN*******", 
            font=("bold", 50, "italic"), 
            align="center"
        )
    
    # Player 2 wins (reaches 10 points)
    if score2 == 10:
        game_on = False             # End the game loop
        window.clear()              # Clear the game screen
        window.bgcolor("blue")      # Set victory background color
        board2.goto(0, 0)          # Center the victory message
        board2.write(
            "*******Player_2 WIN*******", 
            font=("bold", 50, "italic"), 
            align="center"
        )

# ============================================================================
# GAME EXIT
# ============================================================================

window.exitonclick()                # Close game window when clicked
