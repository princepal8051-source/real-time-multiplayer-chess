### Chess Game ♟️

#A multiplayer Chess Game built using Python, Pygame, Socket Programming, and SQLite. The project supports real-time two-player gameplay over a local network with complete chess rules including Check, Checkmate, Castling, Pawn Promotion, Move Validation, and Move History Storage.

##🚀 Features
Core Chess Features
✅ Complete 8x8 Chess Board
✅ All Chess Pieces Implemented
✅ Legal Move Validation
✅ Piece Capture
✅ Check Detection
✅ Checkmate Detection
✅ Stalemate Detection
✅ Castling
✅ Pawn Promotion
✅ Turn-Based Gameplay
#Multiplayer Features
✅ Client-Server Architecture
✅ Two Player Support
✅ Real-Time Move Synchronization
✅ White and Black Player Assignment
✅ Network Communication using Python Sockets
#Database Features
✅ SQLite Integration
✅ Move History Storage
✅ Game Tracking
✅ Automatic Move Logging
#🛠️ Technologies Used
Technology	Purpose
Python	Core Programming
Pygame	GUI and Game Rendering
Socket Programming	Multiplayer Communication
SQLite	Move History Storage
Git & GitHub	Version Control
📁 Project Structure
#Chess-Game/
│
├── board.py
├── client.py
├── database.py
├── game.py
├── history.py
├── main.py
├── move.py
├── network.py
├── pieces.py
├── rules.py
├── server.py
├── settings.py
│
├── chess.db
│
├── assets/
│   └── Chess Piece Images
│
├── README.md
└── requirements.txt
#⚙️ Installation
Clone Repository
git clone https://github.com/princepal87077-ai/Chess-Game.git
cd Chess-Game
Install Dependencies
pip install pygame
▶️ Running the Project
Step 1: Start Server
python3 server.py

#Expected Output:

Chess Server Started...
Waiting for players...
Step 2: Start Player 1

#Open a new terminal:

#python3 main.py
Step 3: Start Player 2

Open another terminal:

python3 main.py

The server automatically assigns:

Player 1 → White
Player 2 → Black
🎮 Gameplay Rules Supported
Movement
Pawn
Rook
Knight
Bishop
Queen
King
Special Rules
Castling
Pawn Promotion
Check
Checkmate
Stalemate
🗄️ Database

Moves are automatically stored in SQLite.

Example:

Game ID: 1

White: e2 → e4
Black: e7 → e5
White: Nf3
Black: Nc6

Database File:

chess.db
📸 Screenshots

Add screenshots of:

Main Board
Multiplayer Gameplay
Checkmate Screen
Pawn Promotion

Example:

![Gameplay](screenshots/gameplay.png)
📈 Future Improvements
Online Multiplayer
AI Opponent
Player Authentication
Game Replay System
Spectator Mode
ELO Rating System
Timer / Chess Clock
Draw by Repetition
En Passant
👨‍💻 Author

Prince Pal

B.Tech CSE (Cloud Computing & Machine Learning)

Skills:

Python
Data Analytics
Data Science
MySQL
Power BI
Machine Learning
Socket Programming
Game Development

GitHub:

https://github.com/princepal87077-ai
📜 License

This project is developed for educational and learning purposes.
