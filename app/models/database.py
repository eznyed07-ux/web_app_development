import sqlite3
import os
from datetime import datetime

# 預設開發用 SQLite DB 位置
DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__dirname__)), '..', 'instance', 'database.db')

def get_db_connection():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema_path = os.path.join(os.path.abspath(os.path.dirname(__dirname__)), '..', 'database', 'schema.sql')
    if os.path.exists(schema_path):
        with get_db_connection() as conn:
            with open(schema_path, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())

class StrategyModel:
    @staticmethod
    def get_strategy():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM strategies WHERE id = 1').fetchone()

    @staticmethod
    def update_strategy(max_loss, cashout_threshold):
        with get_db_connection() as conn:
            now = datetime.now().isoformat()
            conn.execute(
                'UPDATE strategies SET max_loss = ?, cashout_threshold = ?, updated_at = ? WHERE id = 1',
                (max_loss, cashout_threshold, now)
            )
            conn.commit()

class BotStatusModel:
    @staticmethod
    def get_status():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM bot_status WHERE id = 1').fetchone()

    @staticmethod
    def update_status(active: int):
        with get_db_connection() as conn:
            now = datetime.now().isoformat()
            conn.execute(
                'UPDATE bot_status SET active = ?, updated_at = ? WHERE id = 1',
                (active, now)
            )
            conn.commit()

class HistoryModel:
    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM game_history ORDER BY created_at DESC').fetchall()
            
    @staticmethod
    def create(room_id: str, bet_amount: float, profit: float):
        with get_db_connection() as conn:
            now = datetime.now().isoformat()
            conn.execute(
                'INSERT INTO game_history (room_id, bet_amount, profit, created_at) VALUES (?, ?, ?, ?)',
                (room_id, bet_amount, profit, now)
            )
            conn.commit()

class JackpotAlertModel:
    @staticmethod
    def get_unread_alerts():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM jackpot_alerts WHERE is_read = 0 ORDER BY created_at ASC').fetchall()
            
    @staticmethod
    def create(room_id: str, message: str):
        with get_db_connection() as conn:
            now = datetime.now().isoformat()
            conn.execute(
                'INSERT INTO jackpot_alerts (room_id, message, is_read, created_at) VALUES (?, ?, 0, ?)',
                (room_id, message, now)
            )
            conn.commit()

    @staticmethod
    def mark_as_read(alert_id: int):
        with get_db_connection() as conn:
            conn.execute('UPDATE jackpot_alerts SET is_read = 1 WHERE id = ?', (alert_id,))
            conn.commit()
