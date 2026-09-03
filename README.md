# Chess Game ♟️

A multiplayer Chess Game built using Python, Pygame, Socket Programming, SQLite, and FastAPI. The project supports real-time two-player gameplay over a local network with complete chess rules including Check, Checkmate, Castling, Pawn Promotion, Move Validation, Move History Storage, and REST API Integration.

---

## 🚀 Features

### Core Chess Features

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

---

## 🌐 Live API

### API URL

https://real-time-multiplayer-chess.onrender.com

### API Documentation

https://real-time-multiplayer-chess.onrender.com/docs

---

## 🔌 API Endpoints

### Health Check

GET /

Response:

```json
{
  "message": "Chess API Running"
}
```

### Initialize Database

GET /init-db

Response:

```json
{
  "message": "Database initialized"
}
```

### Create Game

POST /create-game

Response:

```json
{
  "game_id": 1,
  "status": "created"
}
```

### Save Move

POST /save-move

Example:

```bash
curl -X POST "https://real-time-multiplayer-chess.onrender.com/save-move?game_id=1&player_color=white&piece=pawn&from_row=6&from_col=4&to_row=4&to_col=4"
```

Response:

```json
{
  "message": "Move Saved"
}
```

### Get Move History

GET /moves/{game_id}

Example:

```bash
curl https://real-time-multiplayer-chess.onrender.com/moves/1
```

---

## 🌐 Multiplayer Features

✅ Client-Server Architecture

✅ Two Player Support

✅ Real-Time Move Synchronization

✅ White and Black Player Assignment

✅ Network Communication using Python Sockets

---

## 🗄️ Database Features

✅ SQLite Integration

✅ Move History Storage

✅ Game Tracking

✅ Automatic Move Logging

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Pygame | GUI and Game Rendering |
| Socket Programming | Multiplayer Communication |
| SQLite | Move History Storage |
| FastAPI | REST API Development |
| Uvicorn | API Server |
| Git & GitHub | Version Control |
| Render | Cloud Deployment |

---

## 📁 Project Structure

```text
Chess-Game/
│
├── api.py
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
├── requirements.txt
└── render.yaml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/princepal8051-source/real-time-multiplayer-chess.git
cd real-time-multiplayer-chess
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Multiplayer Chess

### Step 1: Start Server

```bash
python3 server.py
```

Expected Output:

```text
Chess Server Started...
Waiting for players...
```

### Step 2: Start Player 1

Open a new terminal:

```bash
python3 main.py
```

### Step 3: Start Player 2

Open another terminal:

```bash
python3 main.py
```

Automatic Assignment:

```text
Player 1 → White
Player 2 → Black
```

---

## 🎮 Gameplay Rules Supported

### Movement

- Pawn
- Rook
- Knight
- Bishop
- Queen
- King

### Special Rules

- Castling
- Pawn Promotion
- Check
- Checkmate
- Stalemate

---

## 🗄️ Database

Moves are automatically stored in SQLite.

Example:

```text
Game ID: 1

White: e2 → e4
Black: e7 → e5
White: Nf3
Black: Nc6
```

Database File:

```text
chess.db
```

---

## 📸 Screenshots

Add screenshots of:

- Main Board
- Multiplayer Gameplay
- Checkmate Screen
- Pawn Promotion
- API Documentation (Swagger UI)

Example:

```md
![Gameplay](screenshots/gameplay.png)
```

---

## ☁️ Deployment

The Chess API is deployed on Render.

### Live URL

https://real-time-multiplayer-chess.onrender.com

### Swagger Documentation

https://real-time-multiplayer-chess.onrender.com/docs

---

## 📈 Future Improvements

- Online Multiplayer
- AI Opponent
- Player Authentication
- Game Replay System
- Spectator Mode
- ELO Rating System
- Timer / Chess Clock
- Draw by Repetition
- En Passant
- Browser-Based Chess UI
- WebSocket Support

---

## 👨‍💻 Author

### Prince Pal

B.Tech CSE (Cloud Computing & Machine Learning)

### Skills

- Python
- Data Analytics
- Data Science
- MySQL
- Power BI
- Machine Learning
- Socket Programming
- FastAPI
- Game Development

### GitHub

https://github.com/princepal8051-source

---

## 📜 License

This project is developed for educational and learning purposes.

---

## ✅ Project Status

### Completed Features

- Chess Engine
- Multiplayer Support
- Move Validation
- Check Detection
- Checkmate Detection
- Stalemate Detection
- Castling
- Pawn Promotion
- SQLite Database
- FastAPI Integration
- REST API Endpoints
- Cloud Deployment on Render

### Current Version

**Version 1.0**