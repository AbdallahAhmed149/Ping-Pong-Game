# Ping Pong Game - API Documentation

This document provides comprehensive API documentation for all classes, methods, and functions in the Ping Pong Game project.

## Table of Contents
- [Ball Class](#ball-class)
- [Paddles Class](#paddles-class)
- [Scoreboard Class](#scoreboard-class)
- [Main Module](#main-module)
- [Usage Examples](#usage-examples)
- [Game Constants](#game-constants)

---

## Ball Class

**File:** `Ball.py`  
**Inherits from:** `turtle.Turtle`

### Description
The Ball class represents the game ball that moves across the screen and bounces off walls and paddles. It extends the Turtle class to provide movement functionality.

### Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `move_x` | `int` | `10` | Horizontal movement speed in pixels per frame |
| `move_y` | `int` | `10` | Vertical movement speed in pixels per frame |

### Constructor

#### `__init__(self)`
Initializes a new Ball object with default settings.

**Parameters:** None

**Returns:** None

**Behavior:**
- Creates a white circular ball
- Sets initial position to (0, 0)
- Sets movement speeds to 10 pixels per frame
- Lifts pen to prevent drawing trails

**Example:**
```python
from Ball import Ball

# Create a new ball
ball = Ball()
print(f"Ball position: ({ball.xcor()}, {ball.ycor()})")
print(f"Movement speeds: x={ball.move_x}, y={ball.move_y}")
```

### Inherited Methods

The Ball class inherits all methods from `turtle.Turtle`, including:

- `goto(x, y)` - Move ball to specific coordinates
- `xcor()` - Get current x-coordinate
- `ycor()` - Get current y-coordinate
- `distance(other)` - Calculate distance to another turtle object
- `color(color)` - Change ball color
- `shape(shape)` - Change ball shape

---

## Paddles Class

**File:** `Brackets.py`  
**Inherits from:** `turtle.Turtle`

### Description
The Paddles class represents player-controlled paddles used to hit the ball. Each paddle is rectangular and can move vertically.

### Constructor

#### `__init__(self)`
Initializes a new Paddles object with default settings.

**Parameters:** None

**Returns:** None

**Behavior:**
- Creates a white rectangular paddle (5x1 size ratio)
- Sets initial position to (0, 0)
- Lifts pen to prevent drawing trails

**Example:**
```python
from Brackets import Paddles

# Create a new paddle
paddle = Paddles()
paddle.goto(470, 0)  # Position on right side
```

### Methods

#### `move_up(self)`
Moves the paddle up by 40 pixels.

**Parameters:** None

**Returns:** None

**Behavior:**
- Maintains current x-coordinate
- Increases y-coordinate by 40 pixels

**Example:**
```python
paddle = Paddles()
initial_y = paddle.ycor()
paddle.move_up()
assert paddle.ycor() == initial_y + 40
```

#### `move_down(self)`
Moves the paddle down by 40 pixels.

**Parameters:** None

**Returns:** None

**Behavior:**
- Maintains current x-coordinate
- Decreases y-coordinate by 40 pixels

**Example:**
```python
paddle = Paddles()
initial_y = paddle.ycor()
paddle.move_down()
assert paddle.ycor() == initial_y - 40
```

### Inherited Methods

The Paddles class inherits all methods from `turtle.Turtle`, including:

- `goto(x, y)` - Move paddle to specific coordinates
- `xcor()` - Get current x-coordinate
- `ycor()` - Get current y-coordinate
- `distance(other)` - Calculate distance to another turtle object

---

## Scoreboard Class

**File:** `Score.py`  
**Inherits from:** `turtle.Turtle`

### Description
The Scoreboard class is used to display text on the screen, primarily for showing player scores and game messages. The turtle shape is hidden to show only text.

### Constructor

#### `__init__(self)`
Initializes a new Scoreboard object with default settings.

**Parameters:** None

**Returns:** None

**Behavior:**
- Creates an invisible turtle for text display
- Sets text color to white
- Hides the turtle shape
- Lifts pen to prevent drawing trails

**Example:**
```python
from Score import Scoreboard

# Create a scoreboard
scoreboard = Scoreboard()
scoreboard.goto(100, 250)
scoreboard.write("5", font=("Arial", 50, "normal"))
```

### Inherited Methods

The Scoreboard class inherits all methods from `turtle.Turtle`, with commonly used methods including:

#### `write(text, move=False, align="left", font=("Arial", 8, "normal"))`
Displays text on the screen.

**Parameters:**
- `text` (str): Text to display
- `move` (bool): Whether to move turtle after writing
- `align` (str): Text alignment ("left", "center", "right")
- `font` (tuple): Font specification (family, size, style)

**Example:**
```python
scoreboard.write("Player 1: 5", font=("bold", 50, "normal"))
```

#### `clear()`
Clears the text written by this turtle.

**Example:**
```python
scoreboard.clear()  # Remove current text
scoreboard.write("Player 1: 6", font=("bold", 50, "normal"))
```

---

## Main Module

**File:** `Main.py`

### Description
The main module contains the game initialization, game loop, and game logic. It coordinates all game components and handles user input, collision detection, scoring, and win conditions.

### Global Variables

| Variable | Type | Description |
|----------|------|-------------|
| `window` | `Screen` | Main game window (1000x700 pixels) |
| `board1` | `Scoreboard` | Player 1 score display |
| `board2` | `Scoreboard` | Player 2 score display |
| `score1` | `int` | Player 1 current score |
| `score2` | `int` | Player 2 current score |
| `paddle1` | `Paddles` | Player 1 paddle (right side) |
| `paddle2` | `Paddles` | Player 2 paddle (left side) |
| `ball` | `Ball` | Game ball |
| `speed` | `float` | Game speed delay (lower = faster) |
| `game_on` | `bool` | Game state flag |

### Game Logic Sections

#### 1. Game Initialization
- Creates 1000x700 pixel window with black background
- Disables automatic screen updates for manual control

#### 2. Scoreboard Setup
- Positions Player 1 scoreboard at (100, 250)
- Positions Player 2 scoreboard at (-100, 250)
- Initializes both scores to 0

#### 3. Paddle Setup and Controls
- **Player 1 (Right Paddle):**
  - Position: (470, 0)
  - Controls: Up/Down arrow keys
- **Player 2 (Left Paddle):**
  - Position: (-470, 0)
  - Controls: W/S keys

#### 4. Ball Setup
- Initial position: (0, 0)
- Initial speed: 0.1 second delay per frame

#### 5. Main Game Loop
The game loop runs continuously until a player wins, handling:

##### Ball Movement
```python
ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
```

##### Wall Collision Detection
```python
if ball.ycor() >= 340 or ball.ycor() <= -340:
    ball.move_y *= -1  # Reverse vertical direction
```

##### Paddle Collision Detection
```python
if (ball.xcor() >= 450 and ball.distance(paddle1) <= 50) or \
   (ball.xcor() <= -450 and ball.distance(paddle2) <= 50):
    ball.move_x *= -1  # Reverse horizontal direction
```

##### Scoring Logic
- **Player 2 scores** when `ball.xcor() > 510`
- **Player 1 scores** when `ball.xcor() < -510`
- After each score:
  - Speed increases (delay reduces by 50%)
  - Ball resets to center
  - Ball direction reverses

##### Win Conditions
- Game ends when either player reaches 10 points
- Winner display with colored background:
  - Player 1: Red background
  - Player 2: Blue background

---

## Usage Examples

### Basic Game Setup

```python
# Import required modules
from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard

# Create game window
window = Screen()
window.setup(width=1000, height=700)
window.bgcolor("black")

# Create game objects
ball = Ball()
paddle1 = Paddles()
paddle2 = Paddles()
scoreboard = Scoreboard()

# Position objects
paddle1.goto(470, 0)    # Right paddle
paddle2.goto(-470, 0)   # Left paddle
scoreboard.goto(0, 250) # Top center

# Display initial score
scoreboard.write("0 - 0", align="center", font=("Arial", 50, "normal"))
```

### Custom Ball Behavior

```python
from Ball import Ball

# Create ball with custom movement
ball = Ball()
ball.move_x = 15  # Faster horizontal movement
ball.move_y = 8   # Slower vertical movement

# Position ball at custom location
ball.goto(100, 50)

# Move ball one frame
ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
```

### Paddle Control Implementation

```python
from turtle import Screen
from Brackets import Paddles

window = Screen()
paddle = Paddles()

# Set up keyboard controls
window.listen()
window.onkey(paddle.move_up, "Up")
window.onkey(paddle.move_down, "Down")

# Alternative: Manual paddle control
def custom_move_up():
    if paddle.ycor() < 300:  # Boundary check
        paddle.move_up()

window.onkey(custom_move_up, "Up")
```

### Scoreboard Management

```python
from Score import Scoreboard

# Create multiple scoreboards
player1_score = Scoreboard()
player2_score = Scoreboard()
game_message = Scoreboard()

# Position scoreboards
player1_score.goto(100, 250)
player2_score.goto(-100, 250)
game_message.goto(0, 0)

# Update scores
score1 = 5
player1_score.clear()
player1_score.write(f"{score1}", font=("bold", 50, "normal"))

# Display game message
game_message.write("GAME OVER", align="center", font=("Arial", 60, "bold"))
```

---

## Game Constants

### Window Dimensions
- **Width:** 1000 pixels
- **Height:** 700 pixels
- **Background:** Black

### Paddle Specifications
- **Size:** 5x1 (height x width ratio)
- **Color:** White
- **Movement:** 40 pixels per key press
- **Player 1 Position:** x = 470 (right side)
- **Player 2 Position:** x = -470 (left side)

### Ball Specifications
- **Shape:** Circle
- **Color:** White
- **Initial Speed:** 10 pixels per frame (both x and y)
- **Initial Position:** (0, 0)

### Collision Boundaries
- **Top Wall:** y = 340
- **Bottom Wall:** y = -340
- **Right Scoring Line:** x = 510
- **Left Scoring Line:** x = -510
- **Paddle Collision Distance:** 50 pixels
- **Right Paddle Collision Zone:** x ≥ 450
- **Left Paddle Collision Zone:** x ≤ -450

### Game Settings
- **Initial Speed Delay:** 0.1 seconds
- **Speed Increase Factor:** 0.5 (50% faster after each score)
- **Winning Score:** 10 points
- **Victory Colors:** Red (Player 1), Blue (Player 2)

### Control Mappings
- **Player 1:** Up Arrow (move up), Down Arrow (move down)
- **Player 2:** W key (move up), S key (move down)
- **Exit:** Click game window