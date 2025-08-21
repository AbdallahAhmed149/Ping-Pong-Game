# Ping Pong Game 🏓

## Overview
This is a classic two-player Ping Pong game built using Python's Turtle graphics library. The game features two paddles controlled by players, a bouncing ball, and a scoreboard to track points. The objective is to score points by getting the ball past the opponent's paddle, with the first player to reach 10 points declared the winner! 🎉

## 📚 Documentation

This project includes comprehensive documentation to help you understand, use, and extend the game:

- **[API Documentation](API_DOCUMENTATION.md)** - Complete reference for all classes, methods, and functions with detailed examples
- **[Usage Guide](USAGE_GUIDE.md)** - Comprehensive guide with setup instructions, code examples, customization options, and troubleshooting
- **[README.md](README.md)** - This file with project overview and quick start guide

### Quick Documentation Links
- 🔧 [Installation & Setup](USAGE_GUIDE.md#detailed-setup)
- 🎮 [Game Controls](USAGE_GUIDE.md#game-controls)
- 📖 [Code Examples](USAGE_GUIDE.md#code-examples)
- 🎨 [Customization Guide](USAGE_GUIDE.md#customization-guide)
- 🔍 [API Reference](API_DOCUMENTATION.md)
- 🛠️ [Troubleshooting](USAGE_GUIDE.md#troubleshooting)

## Features
- **Two-Player Gameplay**: Player 1 uses the `Up` and `Down` arrow keys to control the right paddle, while Player 2 uses the `w` and `s` keys for the left paddle. 👥
- **Dynamic Ball Movement**: The ball bounces off the top and bottom walls and the paddles, with increasing speed after each score. ⚡
- **Score Tracking**: Scores are displayed at the top of the screen, updating in real-time as players score points. 📊
- **Game Over Screen**: The game ends when a player reaches 10 points, displaying a victory message with a colored background (red for Player 1, blue for Player 2). 🏆

## Files

### Core Game Files
- `Main.py`: The main script that sets up the game window, initializes game objects, and runs the game loop. 🖥️
- `Ball.py`: Defines the `Ball` class, which handles the ball's appearance and movement. ⚽
- `Brackets.py`: Defines the `Paddles` class, which manages paddle creation and movement. 🏸
- `Score.py`: Defines the `Scoreboard` class, which handles score display. 🖌️

### Documentation Files
- `API_DOCUMENTATION.md`: Complete API reference with detailed class and method documentation 📋
- `USAGE_GUIDE.md`: Comprehensive usage guide with examples, customization, and troubleshooting 📖
- `README.md`: Project overview and quick start guide (this file) 📄

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

## 🚀 Advanced Features & Customization

The game is designed to be easily customizable and extensible. Check out the documentation for:

- **Custom Game Mechanics**: Modify speed, scoring, paddle behavior
- **Visual Customization**: Change colors, shapes, sizes, and window appearance  
- **New Features**: Add sound effects, AI players, power-ups, and game modes
- **Code Examples**: Ready-to-use code snippets for common modifications

See the [Usage Guide](USAGE_GUIDE.md#customization-guide) for detailed customization instructions.

## 🤝 Contributing

Contributions are welcome! Please refer to the [API Documentation](API_DOCUMENTATION.md) to understand the codebase structure before making changes.

## 📞 Support

If you encounter issues:
1. Check the [Troubleshooting Guide](USAGE_GUIDE.md#troubleshooting)
2. Review the [API Documentation](API_DOCUMENTATION.md) for implementation details
3. Ensure all dependencies are properly installed

## License
This project is open-source and available under the [MIT License](LICENSE). 📜
