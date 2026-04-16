-- 策略設定表
CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    max_loss REAL NOT NULL DEFAULT 0.0,
    cashout_threshold REAL NOT NULL DEFAULT 0.0,
    updated_at TEXT NOT NULL
);

-- 自動化狀態表
CREATE TABLE IF NOT EXISTS bot_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    active INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL
);

-- 遊戲與獲利紀錄表
CREATE TABLE IF NOT EXISTS game_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id TEXT NOT NULL,
    bet_amount REAL NOT NULL,
    profit REAL NOT NULL,
    created_at TEXT NOT NULL
);

-- 爆分預警紀錄表
CREATE TABLE IF NOT EXISTS jackpot_alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id TEXT NOT NULL,
    message TEXT NOT NULL,
    is_read INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

-- 預設一筆設定檔紀錄與狀態紀錄 (針對單一玩家的情境)
INSERT INTO strategies (max_loss, cashout_threshold, updated_at) 
SELECT 5000, 10000, datetime('now') 
WHERE NOT EXISTS (SELECT 1 FROM strategies WHERE id = 1);

INSERT INTO bot_status (active, updated_at) 
SELECT 0, datetime('now') 
WHERE NOT EXISTS (SELECT 1 FROM bot_status WHERE id = 1);
