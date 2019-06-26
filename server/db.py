import sqlite3
import os
from contextlib import suppress
from config import config


def init_db():
    with suppress(FileNotFoundError):
        os.remove(config["database"])
    conn = sqlite3.connect(config["database"])
    c = conn.cursor()
    for table in config["tables"]:
        print(f"CREATE TABLE {table} ({', '.join(column for column in config[f'{table}_columns'])})")
        c.execute(f"CREATE TABLE {table} ({', '.join(column for column in config[f'{table}_columns'])})")
        conn.commit()
    conn.close()


def save_user(user_data: dict):
    conn = sqlite3.connect(config["database"])
    c = conn.cursor()
    c.execute(f"INSERT INTO users VALUES ({user_data['id']}, \'{user_data['name']}\')")
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect(config["database"])
    c = conn.cursor()
    c.execute(f"SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users
