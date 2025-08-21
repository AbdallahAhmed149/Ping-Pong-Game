# Ping Pong Game - Usage Guide

This comprehensive guide provides detailed instructions, examples, and best practices for using and extending the Ping Pong Game.

## Table of Contents
- [Quick Start](#quick-start)
- [Detailed Setup](#detailed-setup)
- [Game Controls](#game-controls)
- [Code Examples](#code-examples)
- [Customization Guide](#customization-guide)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)

---

## Quick Start

### Prerequisites
- Python 3.6 or higher
- Turtle graphics library (included with Python)

### Running the Game
1. Download all game files to a directory
2. Open a terminal/command prompt
3. Navigate to the game directory
4. Run the game:
   ```bash
   python Main.py
   ```

### Basic Gameplay
- **Player 1 (Right):** Use ↑ and ↓ arrow keys
- **Player 2 (Left):** Use W and S keys
- **Objective:** Score 10 points to win
- **Exit:** Click the game window when finished

---

## Detailed Setup

### File Structure
```
ping-pong-game/
├── Main.py           # Main game file
├── Ball.py           # Ball class definition
├── Brackets.py       # Paddle class definition
├── Score.py          # Scoreboard class definition
├── README.md         # Project overview
├── API_DOCUMENTATION.md  # API reference
└── USAGE_GUIDE.md    # This file
```

### Installation Steps

1. **Clone or Download**
   ```bash
   git clone https://github.com/your-username/ping-pong-game.git
   cd ping-pong-game
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # Should show Python 3.6 or higher
   ```

3. **Test Turtle Graphics**
   ```python
   # Run this in Python to test turtle
   import turtle
   screen = turtle.Screen()
   screen.exitonclick()
   ```

4. **Run the Game**
   ```bash
   python Main.py
   ```

---

## Game Controls

### Player Controls

| Player | Control | Action |
|--------|---------|--------|
| Player 1 (Right Paddle) | ↑ Arrow Key | Move paddle up |
| Player 1 (Right Paddle) | ↓ Arrow Key | Move paddle down |
| Player 2 (Left Paddle) | W Key | Move paddle up |
| Player 2 (Left Paddle) | S Key | Move paddle down |

### Game Flow Controls

| Action | Method |
|--------|--------|
| Start Game | Run `python Main.py` |
| Pause Game | Alt+Tab (minimize window) |
| Resume Game | Click game window |
| Exit Game | Click window after game ends |

### Control Response
- **Paddle Movement:** 40 pixels per key press
- **Key Repeat:** Hold keys for continuous movement
- **Response Time:** Immediate (no delay)

---

## Code Examples

### 1. Basic Game Initialization

```python
from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard
import time

# Create game window
window = Screen()
window.title("My Ping Pong Game")
window.bgcolor("black")
window.setup(width=1000, height=700)
window.tracer(0)  # Disable automatic updates

# Create game objects
ball = Ball()
paddle1 = Paddles()
paddle2 = Paddles()
scoreboard = Scoreboard()

print("Game initialized successfully!")
```

### 2. Custom Ball Creation and Movement

```python
from Ball import Ball

# Create and customize ball
ball = Ball()
ball.color("red")           # Change color
ball.move_x = 15           # Faster horizontal speed
ball.move_y = 5            # Slower vertical speed

# Manual ball movement
def move_ball():
    current_x = ball.xcor()
    current_y = ball.ycor()
    new_x = current_x + ball.move_x
    new_y = current_y + ball.move_y
    ball.goto(new_x, new_y)
    print(f"Ball position: ({new_x}, {new_y})")

# Move ball one frame
move_ball()
```

### 3. Paddle Setup and Control

```python
from turtle import Screen
from Brackets import Paddles

# Setup
window = Screen()
paddle = Paddles()
paddle.goto(470, 0)  # Right side position

# Enable keyboard input
window.listen()

# Bind controls
window.onkey(paddle.move_up, "Up")
window.onkey(paddle.move_down, "Down")

# Alternative: Custom movement with boundary checking
def safe_move_up():
    if paddle.ycor() < 300:  # Check boundary
        paddle.move_up()
        print(f"Paddle moved to: ({paddle.xcor()}, {paddle.ycor()})")
    else:
        print("Paddle at top boundary")

window.onkey(safe_move_up, "Up")

# Keep window open
window.exitonclick()
```

### 4. Scoreboard Implementation

```python
from Score import Scoreboard

# Create scoreboards for both players
player1_board = Scoreboard()
player2_board = Scoreboard()
message_board = Scoreboard()

# Position scoreboards
player1_board.goto(100, 250)   # Right side
player2_board.goto(-100, 250)  # Left side
message_board.goto(0, 0)        # Center

# Display initial scores
score1, score2 = 0, 0
player1_board.write(f"{score1}", font=("Arial", 50, "bold"))
player2_board.write(f"{score2}", font=("Arial", 50, "bold"))

# Update score function
def update_score(player, new_score):
    if player == 1:
        player1_board.clear()
        player1_board.write(f"{new_score}", font=("Arial", 50, "bold"))
    else:
        player2_board.clear()
        player2_board.write(f"{new_score}", font=("Arial", 50, "bold"))

# Example usage
update_score(1, 3)  # Player 1 scores 3
update_score(2, 1)  # Player 2 scores 1
```

### 5. Collision Detection

```python
from Ball import Ball
from Brackets import Paddles

ball = Ball()
paddle = Paddles()
paddle.goto(470, 0)

# Wall collision detection
def check_wall_collision():
    if ball.ycor() >= 340 or ball.ycor() <= -340:
        ball.move_y *= -1
        print("Ball bounced off wall!")
        return True
    return False

# Paddle collision detection
def check_paddle_collision():
    # Right paddle collision
    if (ball.xcor() >= 450 and 
        ball.distance(paddle) <= 50):
        ball.move_x *= -1
        print("Ball hit right paddle!")
        return True
    return False

# Scoring detection
def check_scoring():
    if ball.xcor() > 510:
        print("Player 2 scores!")
        return 2
    elif ball.xcor() < -510:
        print("Player 1 scores!")
        return 1
    return 0

# Example game loop
while True:
    # Move ball
    ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
    
    # Check collisions
    check_wall_collision()
    check_paddle_collision()
    
    # Check scoring
    scorer = check_scoring()
    if scorer:
        ball.goto(0, 0)  # Reset ball
        break
```

---

## Customization Guide

### 1. Changing Game Appearance

#### Window Customization
```python
# In Main.py, modify these lines:
window.bgcolor("blue")              # Change background color
window.setup(width=1200, height=800)  # Change window size
window.title("Super Ping Pong!")    # Change window title
```

#### Ball Customization
```python
# In Ball.py __init__ method:
self.color("yellow")        # Change ball color
self.shape("square")        # Change ball shape
self.shapesize(1.5)        # Make ball larger
```

#### Paddle Customization
```python
# In Brackets.py __init__ method:
self.color("green")         # Change paddle color
self.shapesize(6, 1.5)     # Change paddle size (height, width)
```

### 2. Modifying Game Mechanics

#### Speed Adjustments
```python
# In Main.py:
speed = 0.05               # Faster game (lower = faster)
ball.move_x = 8           # Slower ball horizontal speed
ball.move_y = 12          # Faster ball vertical speed

# After scoring, change speed increase:
speed *= 0.8              # Less speed increase (was 0.5)
```

#### Movement Adjustments
```python
# In Brackets.py methods:
def move_up(self):
    self.goto(self.xcor(), self.ycor() + 60)  # Larger movement

def move_down(self):
    self.goto(self.xcor(), self.ycor() - 60)  # Larger movement
```

#### Scoring Changes
```python
# In Main.py, change win condition:
if score1 == 5:  # Win at 5 points instead of 10
    # ... win logic
```

### 3. Adding New Features

#### Sound Effects (requires additional setup)
```python
import winsound  # Windows only

# Add to collision detection:
def play_bounce_sound():
    winsound.Beep(800, 100)  # 800Hz for 100ms

# In collision detection:
if ball.ycor() >= 340 or ball.ycor() <= -340:
    ball.move_y *= -1
    play_bounce_sound()
```

#### Pause Functionality
```python
# Add to Main.py:
game_paused = False

def toggle_pause():
    global game_paused
    game_paused = not game_paused
    print("Game paused" if game_paused else "Game resumed")

window.onkey(toggle_pause, "space")

# In game loop:
while game_on:
    if not game_paused:
        # ... existing game logic
        pass
    window.update()
```

#### Power-ups
```python
from turtle import Turtle

class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.goto(0, random.randint(-200, 200))

# Add power-up collision detection in main loop
```

---

## Troubleshooting

### Common Issues

#### 1. Game Won't Start
**Problem:** `python Main.py` doesn't work

**Solutions:**
```bash
# Try these alternatives:
python3 Main.py
py Main.py
./Main.py  # If executable permission set

# Check Python installation:
python --version
which python
```

#### 2. Import Errors
**Problem:** `ModuleNotFoundError` or `ImportError`

**Solutions:**
- Ensure all files are in the same directory
- Check file names match exactly (case-sensitive)
- Verify Python path:
```python
import sys
print(sys.path)
```

#### 3. Controls Not Working
**Problem:** Paddle doesn't move when keys are pressed

**Solutions:**
- Click the game window to focus it
- Check if `window.listen()` is called
- Verify key bindings:
```python
# Debug key presses
def debug_key():
    print("Key pressed!")
    
window.onkey(debug_key, "Up")
```

#### 4. Game Too Fast/Slow
**Problem:** Game speed is uncomfortable

**Solutions:**
```python
# Adjust speed variable in Main.py:
speed = 0.2    # Slower game
speed = 0.05   # Faster game

# Adjust ball speed:
ball.move_x = 5   # Slower horizontal
ball.move_y = 5   # Slower vertical
```

#### 5. Ball Disappears
**Problem:** Ball goes off screen and doesn't return

**Solutions:**
- Check boundary values match window size
- Add debug prints:
```python
print(f"Ball position: ({ball.xcor()}, {ball.ycor()})")
print(f"Ball movement: ({ball.move_x}, {ball.move_y})")
```

### Performance Issues

#### Slow Performance
```python
# Reduce update frequency
window.tracer(2)  # Update every 2 frames instead of 1

# Simplify graphics
ball.shape("circle")  # Simpler than custom shapes
```

#### High CPU Usage
```python
# Increase sleep time
time.sleep(0.02)  # Instead of 0.01

# Reduce collision checks
if frame_count % 2 == 0:  # Check every other frame
    check_collisions()
```

---

## Advanced Usage

### 1. Creating Game Variants

#### Three-Player Mode
```python
# Add third paddle
paddle3 = Paddles()
paddle3.goto(0, -320)  # Bottom paddle
paddle3.shapesize(1, 5)  # Horizontal paddle

# Rotate paddle for horizontal movement
def move_left():
    paddle3.goto(paddle3.xcor() - 40, paddle3.ycor())

def move_right():
    paddle3.goto(paddle3.xcor() + 40, paddle3.ycor())

window.onkey(move_left, "a")
window.onkey(move_right, "d")
```

#### Tournament Mode
```python
class Tournament:
    def __init__(self):
        self.matches = []
        self.current_match = 0
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
    
    def setup_match(self, player1, player2):
        print(f"Match: {player1} vs {player2}")
        # Initialize game with player names
    
    def next_match(self):
        if self.current_match < len(self.matches):
            self.current_match += 1
            # Setup next match
```

### 2. Data Collection and Analytics

#### Game Statistics
```python
class GameStats:
    def __init__(self):
        self.rallies = 0
        self.longest_rally = 0
        self.current_rally = 0
        self.player1_hits = 0
        self.player2_hits = 0
    
    def paddle_hit(self, player):
        self.current_rally += 1
        if player == 1:
            self.player1_hits += 1
        else:
            self.player2_hits += 1
    
    def rally_ended(self):
        if self.current_rally > self.longest_rally:
            self.longest_rally = self.current_rally
        self.rallies += 1
        self.current_rally = 0
    
    def print_stats(self):
        print(f"Total rallies: {self.rallies}")
        print(f"Longest rally: {self.longest_rally}")
        print(f"Player 1 hits: {self.player1_hits}")
        print(f"Player 2 hits: {self.player2_hits}")

# Usage in main game
stats = GameStats()

# In collision detection:
if paddle_collision:
    stats.paddle_hit(player_number)

# When point scored:
stats.rally_ended()
```

#### Save Game Data
```python
import json
from datetime import datetime

class GameLogger:
    def __init__(self):
        self.game_data = {
            "start_time": datetime.now().isoformat(),
            "events": []
        }
    
    def log_event(self, event_type, data):
        event = {
            "time": datetime.now().isoformat(),
            "type": event_type,
            "data": data
        }
        self.game_data["events"].append(event)
    
    def save_game(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.game_data, f, indent=2)

# Usage
logger = GameLogger()
logger.log_event("score", {"player": 1, "score": score1})
logger.log_event("ball_hit", {"position": [ball.xcor(), ball.ycor()]})
logger.save_game(f"game_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
```

### 3. AI Player Implementation

#### Simple AI Paddle
```python
class AIPlayer:
    def __init__(self, paddle, difficulty="medium"):
        self.paddle = paddle
        self.difficulty = difficulty
        self.reaction_delay = {
            "easy": 0.3,
            "medium": 0.15,
            "hard": 0.05
        }[difficulty]
        self.last_update = 0
    
    def update(self, ball, current_time):
        if current_time - self.last_update < self.reaction_delay:
            return
        
        # Simple AI: move toward ball
        ball_y = ball.ycor()
        paddle_y = self.paddle.ycor()
        
        if ball_y > paddle_y + 20:
            self.paddle.move_up()
        elif ball_y < paddle_y - 20:
            self.paddle.move_down()
        
        self.last_update = current_time

# Usage
ai_player = AIPlayer(paddle2, "medium")

# In game loop
ai_player.update(ball, time.time())
```

### 4. Network Multiplayer (Basic Framework)

```python
import socket
import threading
import json

class NetworkGame:
    def __init__(self, is_host=True, host_ip="localhost", port=12345):
        self.is_host = is_host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if is_host:
            self.socket.bind((host_ip, port))
            self.socket.listen(1)
            print("Waiting for player 2...")
            self.conn, addr = self.socket.accept()
            print(f"Player 2 connected from {addr}")
        else:
            self.socket.connect((host_ip, port))
            self.conn = self.socket
    
    def send_data(self, data):
        message = json.dumps(data) + "\n"
        self.conn.send(message.encode())
    
    def receive_data(self):
        try:
            data = self.conn.recv(1024).decode()
            return json.loads(data.strip())
        except:
            return None
    
    def close(self):
        self.conn.close()
        self.socket.close()

# Usage (simplified)
# Host: network = NetworkGame(is_host=True)
# Client: network = NetworkGame(is_host=False, host_ip="192.168.1.100")
```

This comprehensive usage guide provides everything needed to understand, run, customize, and extend the Ping Pong Game. For additional questions or advanced implementations, refer to the API documentation or Python's turtle graphics documentation.