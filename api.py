from fastapi import FastAPI
import sqlite3

from database import create_tables, create_game, save_move

app = FastAPI()

print("Creating tables...")
create_tables()
print("Tables created!")


@app.get("/")
def home():
    return {"message": "Chess API Running"}


@app.post("/create-game")
def new_game():
    game_id = create_game(
        "Player 1",
        "Player 2"
    )

    return {
        "game_id": game_id,
        "status": "created"
    }


@app.post("/save-move")
def move(
    game_id: int,
    player_color: str,
    piece: str,
    from_row: int,
    from_col: int,
    to_row: int,
    to_col: int
):
    save_move(
        game_id,
        player_color,
        piece,
        from_row,
        from_col,
        to_row,
        to_col
    )

    return {"message": "Move Saved"}


@app.get("/moves/{game_id}")
def get_moves(game_id: int):

    conn = sqlite3.connect("chess.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM moves WHERE game_id = ?",
        (game_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return {"moves": data}