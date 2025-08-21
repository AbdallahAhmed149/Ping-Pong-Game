# Ping Pong Game 🏓

## Overview
This is a classic two-player Ping Pong game built using Python's Turtle graphics library. The game features two paddles controlled by players, a bouncing ball, and a scoreboard to track points. The objective is to score points by getting the ball past the opponent's paddle, with the first player to reach 10 points declared the winner! 🎉

## Features
- **Two-Player Gameplay**: Player 1 uses the `Up` and `Down` arrow keys to control the right paddle, while Player 2 uses the `w` and `s` keys for the left paddle. 👥
- **Dynamic Ball Movement**: The ball bounces off the top and bottom walls and the paddles, with increasing speed after each score. ⚡
- **Score Tracking**: Scores are displayed at the top of the screen, updating in real-time as players score points. 📊
- **Game Over Screen**: The game ends when a player reaches 10 points, displaying a victory message with a colored background (red for Player 1, blue for Player 2). 🏆

## Files
- `Main.py`: The main script that sets up the game window, initializes game objects, and runs the game loop. 🖥️
- `Ball.py`: Defines the `Ball` class, which handles the ball's appearance and movement. ⚽
- `Brackets.py`: Defines the `Paddles` class, which manages paddle creation and movement. 🏸
- `Score.py`: Defines the `Scoreboard` class, which handles score display. 🖌️

## How to Play
1. **Setup**: Ensure you have Python installed with the Turtle library (included in standard Python installations). 🐍
2. **Run the Game**: Execute `Main.py` to start the game. 🚀
3. **Controls**:
   - **Player 1 (Right Paddle)**: Use `Up` and `Down` arrow keys to move. ⬆️⬇️
   - **Player 2 (Left Paddle)**: Use `w` (up) and `s` (down) keys to move. 🔼🔽
4. **Objective**: Hit the ball past the opponent's paddle to score points. The first player to reach 10 points wins! 🎯
5. **Exit**: Click the game window to close it after the game ends. ❌

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ping-pong-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ping-pong-game
   ```
3. Run the game:
   ```bash
   python Main.py
   ```

## Requirements
- Python 3.x 🐍
- Turtle graphics library (included with Python) 🐢

## Notes
- The game increases ball speed after each score for added challenge. ⏩
- The game window is set to 1000x700 pixels with a black background for optimal visibility. 🌌
- The game ends with a clear victory screen for the winning player. 🎊

## License
This project is open-source and available under the [MIT License](LICENSE). 📜
