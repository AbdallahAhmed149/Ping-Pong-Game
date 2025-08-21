# Ping Pong Game - Code Examples

This file contains practical code examples for common use cases, modifications, and extensions of the Ping Pong Game.

## Table of Contents
- [Basic Usage Examples](#basic-usage-examples)
- [Customization Examples](#customization-examples)
- [Advanced Features](#advanced-features)
- [Integration Examples](#integration-examples)
- [Testing Examples](#testing-examples)

---

## Basic Usage Examples

### 1. Simple Game Setup

```python
#!/usr/bin/env python3
"""
Simple Ping Pong Game Setup
Minimal code to run the basic game
"""

from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard
import time

def main():
    # Initialize game window
    window = Screen()
    window.title("Simple Ping Pong")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)
    
    # Create game objects
    ball = Ball()
    paddle1 = Paddles()
    paddle2 = Paddles()
    
    # Position paddles
    paddle1.goto(370, 0)  # Right paddle
    paddle2.goto(-370, 0)  # Left paddle
    
    # Setup controls
    window.listen()
    window.onkey(paddle1.move_up, "Up")
    window.onkey(paddle1.move_down, "Down")
    window.onkey(paddle2.move_up, "w")
    window.onkey(paddle2.move_down, "s")
    
    # Simple game loop
    while True:
        window.update()
        time.sleep(0.1)
        
        # Move ball
        ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
        
        # Basic wall collision
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.move_y *= -1
        
        # Reset if ball goes off screen
        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.goto(0, 0)
            time.sleep(1)  # Brief pause
    
    window.exitonclick()

if __name__ == "__main__":
    main()
```

### 2. Single Player vs AI

```python
"""
Single Player vs AI Example
Player controls one paddle, AI controls the other
"""

import random
import time
from turtle import Screen
from Brackets import Paddles
from Ball import Ball

class SimpleAI:
    def __init__(self, paddle, reaction_time=0.1):
        self.paddle = paddle
        self.reaction_time = reaction_time
        self.last_move = 0
    
    def update(self, ball_y, current_time):
        # Only move if enough time has passed (reaction time)
        if current_time - self.last_move < self.reaction_time:
            return
        
        paddle_y = self.paddle.ycor()
        
        # Move towards ball with some randomness
        if ball_y > paddle_y + 30 + random.randint(-10, 10):
            self.paddle.move_up()
            self.last_move = current_time
        elif ball_y < paddle_y - 30 + random.randint(-10, 10):
            self.paddle.move_down()
            self.last_move = current_time

def single_player_game():
    window = Screen()
    window.setup(800, 600)
    window.bgcolor("navy")
    window.title("Player vs AI")
    window.tracer(0)
    
    ball = Ball()
    player_paddle = Paddles()
    ai_paddle = Paddles()
    
    player_paddle.goto(370, 0)
    ai_paddle.goto(-370, 0)
    ai_paddle.color("red")  # Different color for AI
    
    # Create AI
    ai = SimpleAI(ai_paddle, reaction_time=0.15)
    
    # Player controls
    window.listen()
    window.onkey(player_paddle.move_up, "Up")
    window.onkey(player_paddle.move_down, "Down")
    
    while True:
        current_time = time.time()
        window.update()
        time.sleep(0.05)
        
        # Move ball
        ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
        
        # Update AI
        ai.update(ball.ycor(), current_time)
        
        # Wall collisions
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.move_y *= -1
        
        # Paddle collisions
        if (ball.xcor() > 350 and ball.distance(player_paddle) < 50) or \
           (ball.xcor() < -350 and ball.distance(ai_paddle) < 50):
            ball.move_x *= -1
        
        # Reset ball
        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.goto(0, 0)
            ball.move_x *= -1
    
    window.exitonclick()

if __name__ == "__main__":
    single_player_game()
```

---

## Customization Examples

### 1. Custom Game Appearance

```python
"""
Custom Appearance Example
Demonstrates how to customize colors, shapes, and sizes
"""

from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard

class CustomBall(Ball):
    def __init__(self, color="yellow", shape="square"):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.shapesize(1.5)  # Make it larger

class CustomPaddle(Paddles):
    def __init__(self, color="green", height=6, width=1):
        super().__init__()
        self.color(color)
        self.shapesize(height, width)

def custom_game():
    # Custom window
    window = Screen()
    window.setup(1200, 800)
    window.bgcolor("purple")
    window.title("🌈 Rainbow Ping Pong 🌈")
    
    # Custom ball
    ball = CustomBall(color="gold", shape="circle")
    ball.move_x = 12
    ball.move_y = 8
    
    # Custom paddles
    paddle1 = CustomPaddle(color="lime", height=7, width=1.5)
    paddle2 = CustomPaddle(color="cyan", height=7, width=1.5)
    
    paddle1.goto(570, 0)
    paddle2.goto(-570, 0)
    
    # Custom scoreboards
    score1_board = Scoreboard()
    score2_board = Scoreboard()
    score1_board.color("lime")
    score2_board.color("cyan")
    score1_board.goto(150, 350)
    score2_board.goto(-150, 350)
    
    # Display custom messages
    score1_board.write("PLAYER 1", font=("Arial", 24, "bold"))
    score2_board.write("PLAYER 2", font=("Arial", 24, "bold"))
    
    window.exitonclick()

if __name__ == "__main__":
    custom_game()
```

### 2. Speed and Physics Modifications

```python
"""
Physics Modification Example
Custom ball physics and paddle behavior
"""

class PhysicsBall(Ball):
    def __init__(self):
        super().__init__()
        self.gravity = 0.1
        self.bounce_factor = 0.9
        self.max_speed = 15
    
    def apply_physics(self):
        # Apply gravity
        self.move_y -= self.gravity
        
        # Limit maximum speed
        if abs(self.move_x) > self.max_speed:
            self.move_x = self.max_speed if self.move_x > 0 else -self.max_speed
        if abs(self.move_y) > self.max_speed:
            self.move_y = self.max_speed if self.move_y > 0 else -self.max_speed
    
    def bounce_wall(self):
        self.move_y *= -self.bounce_factor  # Lose some energy on bounce

class SmoothPaddle(Paddles):
    def __init__(self):
        super().__init__()
        self.target_y = 0
        self.move_speed = 5
    
    def smooth_move_up(self):
        self.target_y = min(300, self.target_y + 40)
    
    def smooth_move_down(self):
        self.target_y = max(-300, self.target_y - 40)
    
    def update_position(self):
        current_y = self.ycor()
        if abs(current_y - self.target_y) > self.move_speed:
            if current_y < self.target_y:
                self.goto(self.xcor(), current_y + self.move_speed)
            else:
                self.goto(self.xcor(), current_y - self.move_speed)

def physics_game():
    window = Screen()
    window.setup(1000, 700)
    window.bgcolor("black")
    window.tracer(0)
    
    ball = PhysicsBall()
    paddle1 = SmoothPaddle()
    paddle2 = SmoothPaddle()
    
    paddle1.goto(470, 0)
    paddle2.goto(-470, 0)
    
    window.listen()
    window.onkey(paddle1.smooth_move_up, "Up")
    window.onkey(paddle1.smooth_move_down, "Down")
    window.onkey(paddle2.smooth_move_up, "w")
    window.onkey(paddle2.smooth_move_down, "s")
    
    while True:
        window.update()
        time.sleep(0.02)
        
        # Apply physics to ball
        ball.apply_physics()
        ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)
        
        # Update paddle positions
        paddle1.update_position()
        paddle2.update_position()
        
        # Wall collision with physics
        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.bounce_wall()
        
        # Continue with collision detection...

if __name__ == "__main__":
    physics_game()
```

---

## Advanced Features

### 1. Power-ups System

```python
"""
Power-ups Example
Adds collectible power-ups that affect gameplay
"""

import random
from turtle import Turtle

class PowerUp(Turtle):
    def __init__(self, power_type):
        super().__init__()
        self.power_type = power_type
        self.penup()
        self.speed(0)
        
        # Different appearances for different power-ups
        if power_type == "speed":
            self.shape("triangle")
            self.color("red")
        elif power_type == "size":
            self.shape("square")
            self.color("blue")
        elif power_type == "multi":
            self.shape("circle")
            self.color("green")
        
        # Random position
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)
        
        self.active = True
        self.duration = 300  # frames
    
    def apply_effect(self, ball, paddle):
        if self.power_type == "speed":
            ball.move_x *= 1.5
            ball.move_y *= 1.5
        elif self.power_type == "size":
            paddle.shapesize(8, 1)  # Bigger paddle
        elif self.power_type == "multi":
            # Create additional balls (simplified)
            pass
    
    def remove_effect(self, ball, paddle):
        if self.power_type == "size":
            paddle.shapesize(5, 1)  # Normal size

class PowerUpGame:
    def __init__(self):
        self.window = Screen()
        self.window.setup(1000, 700)
        self.window.bgcolor("black")
        self.window.tracer(0)
        
        self.ball = Ball()
        self.paddle1 = Paddles()
        self.paddle2 = Paddles()
        
        self.paddle1.goto(470, 0)
        self.paddle2.goto(-470, 0)
        
        self.power_ups = []
        self.active_effects = []
        
        self.setup_controls()
    
    def setup_controls(self):
        self.window.listen()
        self.window.onkey(self.paddle1.move_up, "Up")
        self.window.onkey(self.paddle1.move_down, "Down")
        self.window.onkey(self.paddle2.move_up, "w")
        self.window.onkey(self.paddle2.move_down, "s")
    
    def spawn_power_up(self):
        if len(self.power_ups) < 2 and random.randint(1, 100) == 1:
            power_type = random.choice(["speed", "size", "multi"])
            power_up = PowerUp(power_type)
            self.power_ups.append(power_up)
    
    def check_power_up_collision(self):
        for power_up in self.power_ups[:]:  # Copy list to avoid modification issues
            if self.ball.distance(power_up) < 30:
                # Determine which paddle gets the effect
                if self.ball.xcor() > 0:
                    power_up.apply_effect(self.ball, self.paddle1)
                else:
                    power_up.apply_effect(self.ball, self.paddle2)
                
                # Track active effect
                self.active_effects.append({
                    'power_up': power_up,
                    'duration': power_up.duration,
                    'paddle': self.paddle1 if self.ball.xcor() > 0 else self.paddle2
                })
                
                # Remove power-up
                power_up.hideturtle()
                self.power_ups.remove(power_up)
    
    def update_effects(self):
        for effect in self.active_effects[:]:
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                effect['power_up'].remove_effect(self.ball, effect['paddle'])
                self.active_effects.remove(effect)
    
    def run(self):
        while True:
            self.window.update()
            time.sleep(0.02)
            
            # Spawn power-ups
            self.spawn_power_up()
            
            # Move ball
            self.ball.goto(self.ball.xcor() + self.ball.move_x, 
                          self.ball.ycor() + self.ball.move_y)
            
            # Check power-up collisions
            self.check_power_up_collision()
            
            # Update active effects
            self.update_effects()
            
            # Regular game collision detection...
            # (Add normal game logic here)

if __name__ == "__main__":
    game = PowerUpGame()
    game.run()
```

### 2. Tournament System

```python
"""
Tournament System Example
Multi-player tournament with brackets and statistics
"""

class Player:
    def __init__(self, name, control_type="human", ai_difficulty=None):
        self.name = name
        self.control_type = control_type
        self.ai_difficulty = ai_difficulty
        self.wins = 0
        self.total_games = 0
        self.points_scored = 0
        self.points_conceded = 0
    
    def add_game_result(self, won, points_for, points_against):
        self.total_games += 1
        if won:
            self.wins += 1
        self.points_scored += points_for
        self.points_conceded += points_against
    
    def win_rate(self):
        return self.wins / self.total_games if self.total_games > 0 else 0

class Tournament:
    def __init__(self, players):
        self.players = players
        self.matches = []
        self.current_round = 1
        self.results = {}
        
        self.generate_matches()
    
    def generate_matches(self):
        # Simple round-robin tournament
        for i, player1 in enumerate(self.players):
            for j, player2 in enumerate(self.players[i+1:], i+1):
                self.matches.append((player1, player2))
    
    def play_match(self, player1, player2):
        print(f"\n🏆 Match: {player1.name} vs {player2.name}")
        
        # Simplified match simulation
        # In a real implementation, this would run the actual game
        score1 = random.randint(0, 10)
        score2 = random.randint(0, 10)
        
        # Ensure there's a winner
        if score1 == score2:
            score1 += 1
        
        winner = player1 if score1 > score2 else player2
        loser = player2 if score1 > score2 else player1
        
        # Update statistics
        player1.add_game_result(score1 > score2, score1, score2)
        player2.add_game_result(score2 > score1, score2, score1)
        
        self.results[(player1.name, player2.name)] = (score1, score2)
        
        print(f"Result: {player1.name} {score1} - {score2} {player2.name}")
        print(f"Winner: {winner.name} 🎉")
        
        return winner
    
    def run_tournament(self):
        print("🏓 PING PONG TOURNAMENT STARTING! 🏓")
        print("=" * 40)
        
        for match in self.matches:
            self.play_match(match[0], match[1])
            input("Press Enter for next match...")
        
        self.display_final_standings()
    
    def display_final_standings(self):
        print("\n🏆 FINAL STANDINGS 🏆")
        print("=" * 50)
        
        # Sort players by wins, then by win rate
        sorted_players = sorted(self.players, 
                              key=lambda p: (p.wins, p.win_rate()), 
                              reverse=True)
        
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player.name}")
            print(f"   Wins: {player.wins}/{player.total_games}")
            print(f"   Win Rate: {player.win_rate():.1%}")
            print(f"   Points: {player.points_scored} for, {player.points_conceded} against")
            print()

# Example usage
def run_tournament():
    players = [
        Player("Alice", "human"),
        Player("Bob", "human"),
        Player("Charlie", "ai", "easy"),
        Player("Diana", "ai", "medium")
    ]
    
    tournament = Tournament(players)
    tournament.run_tournament()

if __name__ == "__main__":
    run_tournament()
```

---

## Integration Examples

### 1. Save/Load Game State

```python
"""
Save/Load Game State Example
Demonstrates how to save and restore game progress
"""

import json
import pickle
from datetime import datetime

class GameState:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.ball_position = (0, 0)
        self.ball_velocity = (10, 10)
        self.paddle1_position = (470, 0)
        self.paddle2_position = (-470, 0)
        self.game_speed = 0.1
        self.timestamp = datetime.now().isoformat()
    
    def save_to_json(self, filename):
        """Save game state as JSON"""
        data = {
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
            'ball_position': self.ball_position,
            'ball_velocity': self.ball_velocity,
            'paddle1_position': self.paddle1_position,
            'paddle2_position': self.paddle2_position,
            'game_speed': self.game_speed,
            'timestamp': self.timestamp
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Game saved to {filename}")
    
    def load_from_json(self, filename):
        """Load game state from JSON"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.player1_score = data['player1_score']
            self.player2_score = data['player2_score']
            self.ball_position = tuple(data['ball_position'])
            self.ball_velocity = tuple(data['ball_velocity'])
            self.paddle1_position = tuple(data['paddle1_position'])
            self.paddle2_position = tuple(data['paddle2_position'])
            self.game_speed = data['game_speed']
            self.timestamp = data['timestamp']
            
            print(f"Game loaded from {filename}")
            return True
        except FileNotFoundError:
            print(f"Save file {filename} not found")
            return False
        except json.JSONDecodeError:
            print(f"Invalid save file format: {filename}")
            return False
    
    def save_to_binary(self, filename):
        """Save game state as binary (pickle)"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Game saved to binary file {filename}")
    
    def load_from_binary(self, filename):
        """Load game state from binary (pickle)"""
        try:
            with open(filename, 'rb') as f:
                loaded_state = pickle.load(f)
            
            # Copy attributes from loaded state
            for attr in ['player1_score', 'player2_score', 'ball_position', 
                        'ball_velocity', 'paddle1_position', 'paddle2_position',
                        'game_speed', 'timestamp']:
                setattr(self, attr, getattr(loaded_state, attr))
            
            print(f"Game loaded from binary file {filename}")
            return True
        except FileNotFoundError:
            print(f"Save file {filename} not found")
            return False

class SaveableGame:
    def __init__(self):
        self.window = Screen()
        self.window.setup(1000, 700)
        self.window.bgcolor("black")
        self.window.tracer(0)
        
        self.ball = Ball()
        self.paddle1 = Paddles()
        self.paddle2 = Paddles()
        self.scoreboard1 = Scoreboard()
        self.scoreboard2 = Scoreboard()
        
        self.game_state = GameState()
        self.setup_controls()
        self.restore_positions()
    
    def setup_controls(self):
        self.window.listen()
        # Game controls
        self.window.onkey(self.paddle1.move_up, "Up")
        self.window.onkey(self.paddle1.move_down, "Down")
        self.window.onkey(self.paddle2.move_up, "w")
        self.window.onkey(self.paddle2.move_down, "s")
        
        # Save/Load controls
        self.window.onkey(self.save_game, "F5")      # F5 to save
        self.window.onkey(self.load_game, "F9")      # F9 to load
        self.window.onkey(self.quick_save, "F1")     # F1 for quick save
        self.window.onkey(self.quick_load, "F2")     # F2 for quick load
    
    def save_current_state(self):
        """Update game state with current positions and scores"""
        self.game_state.ball_position = (self.ball.xcor(), self.ball.ycor())
        self.game_state.ball_velocity = (self.ball.move_x, self.ball.move_y)
        self.game_state.paddle1_position = (self.paddle1.xcor(), self.paddle1.ycor())
        self.game_state.paddle2_position = (self.paddle2.xcor(), self.paddle2.ycor())
        self.game_state.timestamp = datetime.now().isoformat()
    
    def restore_positions(self):
        """Restore game objects to saved positions"""
        self.ball.goto(*self.game_state.ball_position)
        self.ball.move_x, self.ball.move_y = self.game_state.ball_velocity
        self.paddle1.goto(*self.game_state.paddle1_position)
        self.paddle2.goto(*self.game_state.paddle2_position)
        
        # Update scoreboards
        self.scoreboard1.clear()
        self.scoreboard2.clear()
        self.scoreboard1.goto(100, 250)
        self.scoreboard2.goto(-100, 250)
        self.scoreboard1.write(f"{self.game_state.player1_score}", 
                              font=("Arial", 50, "normal"))
        self.scoreboard2.write(f"{self.game_state.player2_score}", 
                              font=("Arial", 50, "normal"))
    
    def save_game(self):
        """Save game (F5)"""
        self.save_current_state()
        filename = f"savegame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        self.game_state.save_to_json(filename)
    
    def load_game(self):
        """Load most recent save game (F9)"""
        import glob
        save_files = glob.glob("savegame_*.json")
        if save_files:
            latest_save = max(save_files)  # Most recent by filename
            if self.game_state.load_from_json(latest_save):
                self.restore_positions()
    
    def quick_save(self):
        """Quick save to fixed filename (F1)"""
        self.save_current_state()
        self.game_state.save_to_json("quicksave.json")
    
    def quick_load(self):
        """Quick load from fixed filename (F2)"""
        if self.game_state.load_from_json("quicksave.json"):
            self.restore_positions()

# Usage example
if __name__ == "__main__":
    game = SaveableGame()
    print("Controls:")
    print("F1 - Quick Save")
    print("F2 - Quick Load") 
    print("F5 - Save Game")
    print("F9 - Load Latest Save")
    game.window.exitonclick()
```

---

## Testing Examples

### 1. Unit Tests

```python
"""
Unit Testing Example
Tests for individual game components
"""

import unittest
from unittest.mock import Mock, patch
from Ball import Ball
from Brackets import Paddles
from Score import Scoreboard

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()
    
    def test_initial_position(self):
        """Test ball starts at origin"""
        self.assertEqual(self.ball.xcor(), 0)
        self.assertEqual(self.ball.ycor(), 0)
    
    def test_initial_movement(self):
        """Test ball has initial movement speeds"""
        self.assertEqual(self.ball.move_x, 10)
        self.assertEqual(self.ball.move_y, 10)
    
    def test_ball_properties(self):
        """Test ball appearance properties"""
        self.assertEqual(self.ball.shape(), "circle")
        self.assertEqual(self.ball.pencolor(), "white")

class TestPaddles(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddles()
    
    def test_initial_position(self):
        """Test paddle starts at origin"""
        self.assertEqual(self.paddle.xcor(), 0)
        self.assertEqual(self.paddle.ycor(), 0)
    
    def test_move_up(self):
        """Test paddle moves up correctly"""
        initial_y = self.paddle.ycor()
        self.paddle.move_up()
        self.assertEqual(self.paddle.ycor(), initial_y + 40)
    
    def test_move_down(self):
        """Test paddle moves down correctly"""
        initial_y = self.paddle.ycor()
        self.paddle.move_down()
        self.assertEqual(self.paddle.ycor(), initial_y - 40)
    
    def test_multiple_moves(self):
        """Test multiple paddle movements"""
        self.paddle.move_up()
        self.paddle.move_up()
        self.assertEqual(self.paddle.ycor(), 80)
        
        self.paddle.move_down()
        self.assertEqual(self.paddle.ycor(), 40)

class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()
    
    def test_turtle_hidden(self):
        """Test scoreboard turtle is hidden"""
        self.assertFalse(self.scoreboard.isvisible())
    
    def test_initial_properties(self):
        """Test scoreboard initial properties"""
        self.assertEqual(self.scoreboard.pencolor(), "white")

class TestGameLogic(unittest.TestCase):
    """Test game logic functions"""
    
    def test_wall_collision_detection(self):
        """Test wall collision detection logic"""
        ball = Ball()
        
        # Test top wall collision
        ball.goto(0, 350)
        self.assertTrue(ball.ycor() >= 340)
        
        # Test bottom wall collision  
        ball.goto(0, -350)
        self.assertTrue(ball.ycor() <= -340)
    
    def test_paddle_collision_detection(self):
        """Test paddle collision detection"""
        ball = Ball()
        paddle = Paddles()
        
        # Position ball near paddle
        ball.goto(450, 0)
        paddle.goto(470, 0)
        
        # Test collision condition
        collision = (ball.xcor() >= 450 and ball.distance(paddle) <= 50)
        self.assertTrue(collision)
    
    def test_scoring_boundaries(self):
        """Test scoring boundary detection"""
        ball = Ball()
        
        # Test right boundary (Player 2 scores)
        ball.goto(520, 0)
        self.assertTrue(ball.xcor() > 510)
        
        # Test left boundary (Player 1 scores)
        ball.goto(-520, 0)
        self.assertTrue(ball.xcor() < -510)

if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
```

### 2. Integration Tests

```python
"""
Integration Testing Example
Tests for complete game scenarios
"""

import unittest
import time
from unittest.mock import patch, MagicMock
from turtle import Screen

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        # Mock turtle graphics to avoid GUI during testing
        self.screen_mock = MagicMock()
        self.ball_mock = MagicMock()
        self.paddle_mock = MagicMock()
    
    @patch('turtle.Screen')
    def test_game_initialization(self, mock_screen):
        """Test complete game setup"""
        mock_screen.return_value = self.screen_mock
        
        # Import and initialize game components
        from Ball import Ball
        from Brackets import Paddles
        
        ball = Ball()
        paddle1 = Paddles()
        paddle2 = Paddles()
        
        # Test that objects were created
        self.assertIsNotNone(ball)
        self.assertIsNotNone(paddle1)
        self.assertIsNotNone(paddle2)
    
    def test_complete_rally(self):
        """Test a complete rally scenario"""
        # Create mock objects
        ball = MagicMock()
        paddle1 = MagicMock()
        paddle2 = MagicMock()
        
        # Set up initial positions
        ball.xcor.return_value = 0
        ball.ycor.return_value = 0
        ball.move_x = 10
        ball.move_y = 5
        
        paddle1.xcor.return_value = 470
        paddle1.ycor.return_value = 0
        paddle1.distance.return_value = 30  # Within collision range
        
        # Simulate ball movement toward paddle
        ball.xcor.return_value = 450  # Near paddle
        
        # Test collision detection
        collision = (ball.xcor() >= 450 and ball.distance(paddle1) <= 50)
        self.assertTrue(collision)
        
        # After collision, ball direction should reverse
        ball.move_x *= -1
        self.assertEqual(ball.move_x, -10)
    
    def test_scoring_scenario(self):
        """Test complete scoring scenario"""
        ball = MagicMock()
        score1 = 0
        score2 = 0
        
        # Ball goes past right boundary
        ball.xcor.return_value = 520
        
        if ball.xcor() > 510:
            score2 += 1
            ball.goto(0, 0)  # Reset ball
            ball.move_x *= -1  # Reverse direction
        
        self.assertEqual(score2, 1)
        ball.goto.assert_called_with(0, 0)
    
    def test_win_condition(self):
        """Test game win condition"""
        score1 = 9
        score2 = 8
        game_on = True
        
        # Player 1 scores final point
        score1 += 1
        
        if score1 == 10:
            game_on = False
        
        self.assertEqual(score1, 10)
        self.assertFalse(game_on)

class TestPerformance(unittest.TestCase):
    """Performance testing"""
    
    def test_collision_detection_performance(self):
        """Test collision detection performance"""
        from Ball import Ball
        from Brackets import Paddles
        
        ball = Ball()
        paddle = Paddles()
        
        # Time collision detection
        start_time = time.time()
        
        for _ in range(1000):
            collision = (ball.xcor() >= 450 and ball.distance(paddle) <= 50)
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Should complete 1000 collision checks in under 1 second
        self.assertLess(duration, 1.0)
        print(f"1000 collision checks completed in {duration:.4f} seconds")

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Running the Examples

### Setup Instructions

1. **Save examples to separate files:**
   ```bash
   # Save each example as a separate .py file
   # For example: save the first example as "simple_game.py"
   ```

2. **Install dependencies (if needed):**
   ```bash
   # Most examples only need standard library
   # For testing examples:
   pip install unittest  # Usually included with Python
   ```

3. **Run examples:**
   ```bash
   python simple_game.py
   python physics_game.py
   python -m unittest test_examples.py  # For test examples
   ```

### Modification Tips

- **Start Simple:** Begin with basic examples and gradually add features
- **Test Changes:** Use the testing examples to verify your modifications
- **Performance:** Monitor game performance when adding complex features
- **Documentation:** Document your changes following the patterns shown

These examples provide a comprehensive foundation for understanding and extending the Ping Pong Game. Use them as starting points for your own customizations and features!