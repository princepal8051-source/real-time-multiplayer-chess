# ♟️ Chess Game — Real-Time Multiplayer

A multiplayer Chess Game developed using **Python, Pygame, Socket Programming, and SQLite**. The project provides a two-player chess experience with real-time move synchronization over a local network.

The application implements core chess rules and game-state validation, including **legal move validation, piece capture, check, checkmate, stalemate, castling, pawn promotion, turn management, and move-history storage**.

---


## 📑 Table of Contents

• Project Overview
• Objectives
• Key Features
• System Architecture
• Technologies Used
• Project Structure
• Chess Rules
• Multiplayer Workflow
• Database
• Installation
• Running the Game
• Gameplay
• Screenshots
• Challenges
• Future Improvements
• Team Members
• Project Status
• License


# 📖 Project Overview

The **Real-Time Multiplayer Chess Game** is a desktop-based chess application designed to allow two players to play chess against each other using a client-server architecture.

The project combines several areas of software development:

* **Game Development** using Pygame
* **Chess Rule Processing** using Python
* **Network Programming** using Python sockets
* **Database Management** using SQLite
* **Version Control** using Git and GitHub

The game provides a graphical chess board where players can move pieces, capture opponent pieces, and play according to standard chess rules implemented by the application.

---

# 🎯 Objectives

The main objectives of this project are:

1. To develop a functional chess game using Python.
2. To create an interactive graphical interface using Pygame.
3. To implement chess movement and rule validation.
4. To support two-player multiplayer gameplay.
5. To synchronize player moves over a network.
6. To maintain game and move history using SQLite.
7. To demonstrate client-server communication.
8. To provide a foundation for future online multiplayer and AI functionality.

---

# 🚀 Key Features

## ♟️ Core Chess Features

* ✅ Complete 8×8 chess board
* ✅ All standard chess pieces
* ✅ Pawn movement
* ✅ Rook movement
* ✅ Knight movement
* ✅ Bishop movement
* ✅ Queen movement
* ✅ King movement
* ✅ Legal move validation
* ✅ Piece capture
* ✅ Turn-based gameplay
* ✅ Check detection
* ✅ Checkmate detection
* ✅ Stalemate detection
* ✅ Castling
* ✅ Pawn promotion

---

# 🌐 Multiplayer Features

The game uses a **client-server architecture** for multiplayer gameplay.

### Features

* ✅ Two-player support
* ✅ Client-server communication
* ✅ Real-time move synchronization
* ✅ White and Black player assignment
* ✅ Network communication using Python sockets
* ✅ Shared game state between players

### Player Assignment

```text
              Chess Server
                   │
          ┌────────┴────────┐
          │                 │
      Player 1           Player 2
          │                 │
        White             Black
```

---

# 🏗️ System Architecture

The overall application can be represented as:

```text
                    ┌───────────────────┐
                    │   Chess Server    │
                    │                   │
                    │ Socket Networking │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │    Player 1     │       │    Player 2     │
        │                 │       │                 │
        │     Pygame      │       │     Pygame      │
        │     Client      │       │     Client      │
        │                 │       │                 │
        │     White       │       │      Black      │
        └─────────────────┘       └─────────────────┘
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                       ┌─────────────┐
                       │   SQLite    │
                       │  Database   │
                       └─────────────┘
```

### Architecture Components

**Client**

Handles the player's graphical interface and interaction with the chess board.

**Server**

Manages multiplayer communication and coordinates connected players.

**Chess Engine / Rules**

Validates chess moves and determines game states such as check, checkmate, and stalemate.

**SQLite Database**

Stores game and move information.

---

# 🛠️ Technologies Used

| Technology             | Purpose                                |
| ---------------------- | -------------------------------------- |
| **Python**             | Core programming language              |
| **Pygame**             | Graphical interface and game rendering |
| **Socket Programming** | Multiplayer communication              |
| **SQLite**             | Game and move-history storage          |
| **Git**                | Version control                        |
| **GitHub**             | Source-code hosting and collaboration  |

---

# 📁 Project Structure

```text
Chess-Game/
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
└── README.md
```

### Important Files

| File          | Purpose                               |
| ------------- | ------------------------------------- |
| `main.py`     | Main game/application entry point     |
| `server.py`   | Multiplayer server                    |
| `client.py`   | Client-side communication             |
| `network.py`  | Network communication functionality   |
| `board.py`    | Chess board functionality             |
| `pieces.py`   | Chess piece functionality             |
| `rules.py`    | Chess rules and legal move validation |
| `move.py`     | Move-related functionality            |
| `history.py`  | Move history functionality            |
| `database.py` | SQLite database operations            |
| `game.py`     | Game management                       |
| `settings.py` | Application settings                  |
| `chess.db`    | SQLite database                       |

---

# ♜ Chess Rules Supported

## Piece Movement

The game supports movement for:

* Pawn
* Rook
* Knight
* Bishop
* Queen
* King

## Special Rules

### Castling

The project supports castling as a special king-and-rook move.

### Pawn Promotion

When a pawn reaches the opposite end of the board, pawn promotion is supported.

### Check

The game detects when a player's king is under attack.

### Checkmate

The game checks whether a player is in check and has no legal move available.

```text
Player makes a move
        ↓
Check opponent's king
        ↓
Is the king attacked?
        ↓
       YES
        ↓
Check
        ↓
Are legal moves available?
      ↙       ↘
    YES        NO
     ↓          ↓
 Continue    Checkmate
```

### Stalemate

The game also supports stalemate detection when a player has no legal moves but is not in check.

---

# 🔄 Multiplayer Workflow

The multiplayer game follows this general workflow:

```text
Start Server
     ↓
Wait for Players
     ↓
Player 1 Connects
     ↓
Player 1 → White
     ↓
Player 2 Connects
     ↓
Player 2 → Black
     ↓
Game Starts
     ↓
Player Makes Move
     ↓
Move Validation
     ↓
Move Sent Through Network
     ↓
Opponent Receives Move
     ↓
Board Updated
     ↓
Next Player's Turn
```

This allows both players to maintain an updated game state while playing.

---

# 🗄️ Database

The project uses **SQLite** for storing game-related information and move history.

Database file:

```text
chess.db
```

Example move history:

```text
Game ID: 1

White: e2 → e4
Black: e7 → e5
White: Nf3
Black: Nc6
```

### Database Functions

* Game tracking
* Move history storage
* Automatic move logging
* Persistent game information

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/princepal8051-source/real-time-multiplayer-chess.git
```

Then:

```bash
cd real-time-multiplayer-chess
```

## 2. Install Dependencies

Install the required Python packages used by the project.

For example:

```bash
pip install pygame
```

If your project has a `requirements.txt`, install dependencies using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Multiplayer Chess

## Step 1 — Start the Server

Open Terminal:

```bash
python3 server.py
```

Expected output:

```text
Chess Server Started...
Waiting for players...
```

---

## Step 2 — Start Player 1

Open another terminal:

```bash
python3 main.py
```

Player 1 is assigned:

```text
White
```

---

## Step 3 — Start Player 2

Open another terminal:

```bash
python3 main.py
```

Player 2 is assigned:

```text
Black
```

The two players can then play the game through the multiplayer connection.

---

# 🎮 Gameplay

The basic gameplay cycle is:

<<<<<<< HEAD
B.Tech CSE (Cloud Computing & Machine Learning)
University Roll number -- 1240438034

### GitHub

https://github.com/princepal8051-source

---

## 📜 License

This project is developed for educational and learning purposes.

---

## ✅ Project Status

### Completed Features

* Chess Engine
* Multiplayer Support
* Move Validation
* Check Detection
* Checkmate Detection
* Stalemate Detection
=======
```text
Select Piece
     ↓
Display / Validate Legal Moves
     ↓
Select Destination
     ↓
Validate Move
     ↓
Move Piece
     ↓
Capture if Required
     ↓
Check Game State
     ↓
Synchronize With Opponent
     ↓
Change Turn
```

The application also handles special game states such as:

* Check
* Checkmate
* Stalemate
>>>>>>> testing-my-setup
* Castling
* Pawn Promotion

---

# 📸 Screenshots

Screenshots can be added to demonstrate the major parts of the project.

### Main Chess Board

```md
![Chess Board](screenshots/gameplay.png)
```

### Multiplayer Gameplay

```md
![Multiplayer Gameplay](screenshots/multiplayer.png)
```

### Checkmate

```md
![Checkmate](screenshots/checkmate.png)
```

### Pawn Promotion

```md
![Pawn Promotion](screenshots/promotion.png)
```

---

# 🧩 Challenges Faced

During development, several technical areas required implementation and testing.

### 1. Chess Rule Validation

Each chess piece has different movement rules, so legal moves need to be validated before they are executed.

### 2. King Safety

The game must prevent a player from making a move that leaves their own king in check.

### 3. Check and Checkmate Detection

The application needs to determine whether the king is attacked and whether the player has any legal moves remaining.

### 4. Multiplayer Synchronization

Moves need to be communicated between players so that both game windows remain synchronized.

### 5. Database Management

Game and move information needs to be stored and retrieved correctly.

### 6. Version Control

Git and GitHub are used to manage development, branches, commits, and collaboration.

---

# 🔮 Future Improvements

Possible future improvements include:

* 🌐 Online multiplayer
* 🤖 AI chess opponent
* 🔐 Player authentication
* 🔄 Game replay system
* 👀 Spectator mode
* 🏆 ELO rating system
* ⏱️ Chess timer / clock
* 🔁 Draw by repetition
* ♟️ En passant
* 📊 Player statistics
* 👤 User profiles
* 🎮 Improved graphical interface
* 📱 Mobile or web-based version

---

# 👨‍💻 Team Members

This project was developed as a team.

| No. | Team Member        |
| --: | ------------------ |
|   1 | **Prince Pal**     |
|   2 | **Prince Sonkar**  |
|   3 | **Vaibhav Tiwari** |
|   4 | **Shivaji**        |
|   5 | **Saurabh Singh**  |

### Team Contribution

The project combines contributions across areas such as:

* Chess-game development
* Python programming
* User-interface development
* Chess-rule implementation
* Multiplayer networking
* Database management
* Testing and debugging
* Git/GitHub version control
* Documentation

> **Note:** Specific individual responsibilities should be added according to the actual work performed by each team member.

---

# 📊 Project Learning Outcomes

Through this project, the team gained practical experience in:

* Python application development
* Object-oriented programming concepts
* Game development with Pygame
* Socket-based networking
* Client-server architecture
* Database management with SQLite
* Chess algorithm and rule implementation
* Debugging and testing
* Git and GitHub
* Team-based software development

---

# 🌱 Project Development Workflow

```text
Planning
   ↓
Design
   ↓
Chess Board Development
   ↓
Piece Movement
   ↓
Rule Validation
   ↓
Multiplayer Networking
   ↓
Database Integration
   ↓
Testing & Debugging
   ↓
Documentation
   ↓
Deployment / Demonstration
```

---

# 📜 License

This project is developed for **educational and learning purposes**.

---

# ✅ Project Status

### Completed

* ✅ Chess Board
* ✅ Chess Pieces
* ✅ Legal Move Validation
* ✅ Piece Capture
* ✅ Turn-Based Gameplay
* ✅ Check Detection
* ✅ Checkmate Detection
* ✅ Stalemate Detection
* ✅ Castling
* ✅ Pawn Promotion
* ✅ Multiplayer Support
* ✅ Socket Communication
* ✅ SQLite Database
* ✅ Move History

### Current Version

**Version 1.0**

---

# 🙏 Acknowledgement

We would like to thank everyone who supported the development and testing of this project.

This project helped the team combine **game development, networking, database management, software engineering, and collaborative development** into a single practical application.

---

# ⭐ Conclusion

The **Real-Time Multiplayer Chess Game** demonstrates how Python can be used to build a complete interactive multiplayer application.

By combining **Pygame, Python Socket Programming, SQLite, chess-rule validation, and Git/GitHub**, the project provides a foundation that can be extended into a larger online chess platform with AI opponents, player accounts, ratings, game history, and additional chess functionality.
