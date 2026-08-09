import sqlite3


DATABASE_NAME = "chess.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():

    connection = connect_db()
    cursor = connection.cursor()

    # Players table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL
        )
    """)

    # Games table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            white_player TEXT NOT NULL,
            black_player TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    # Moves table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER NOT NULL,
            player_color TEXT NOT NULL,
            piece TEXT NOT NULL,
            from_row INTEGER NOT NULL,
            from_col INTEGER NOT NULL,
            to_row INTEGER NOT NULL,
            to_col INTEGER NOT NULL,
            captured_piece TEXT,
            FOREIGN KEY (game_id) REFERENCES games(id)
        )
    """)

    connection.commit()
    connection.close()


def add_player(name, color):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO players (name, color)
        VALUES (?, ?)
        """,
        (name, color)
    )

    connection.commit()

    player_id = cursor.lastrowid

    connection.close()

    return player_id


def create_game(white_player, black_player):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO games (
            white_player,
            black_player,
            status
        )
        VALUES (?, ?, ?)
        """,
        (
            white_player,
            black_player,
            "playing"
        )
    )

    connection.commit()

    game_id = cursor.lastrowid

    connection.close()

    return game_id


def save_move(
    game_id,
    player_color,
    piece,
    from_row,
    from_col,
    to_row,
    to_col,
    captured_piece=""
):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO moves (
            game_id,
            player_color,
            piece,
            from_row,
            from_col,
            to_row,
            to_col,
            captured_piece
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            game_id,
            player_color,
            piece,
            from_row,
            from_col,
            to_row,
            to_col,
            captured_piece
        )
    )

    connection.commit()
    connection.close()


def update_game_status(game_id, status):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE games
        SET status = ?
        WHERE id = ?
        """,
        (
            status,
            game_id
        )
    )

    connection.commit()
    connection.close()