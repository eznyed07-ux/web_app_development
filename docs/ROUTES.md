# 路由與頁面設計文件 (Routes Design)

本文件根據 PRD、架構文件以及資料庫設計，列出賽特選房系統的所有網頁端點 (Routes)，以及其所對應的視圖模板。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 首頁儀表板 | GET | `/` 或 `/dashboard` | `templates/dashboard.html` | 呈現目前總獲利與自動化腳本運行狀態 |
| 選房分析列表 | GET | `/rooms` | `templates/rooms.html` | 條列系統篩選後的高勝率房間 |
| 選房詳細資料 | GET | `/rooms/<room_id>` | `templates/room_detail.html` | 顯示單一機台進階資料 |
| 參數設定介面 | GET | `/settings` | `templates/settings.html` | 停損與出金金額設定表單 |
| 儲存參數設定 | POST | `/settings/save` | — | 寫入設定至 DB，重導回 `/settings` |
| 啟動/停止腳本 | POST | `/bot/toggle` | — | 控制狀態寫入 DB，重導回原頁面 |
| 歷史紀錄查詢 | GET | `/history` | `templates/history.html` | 顯示每一局的獲利明細 |

## 2. 每個路由的詳細說明

### 首頁儀表板
* **路徑**：`GET /` 或 `GET /dashboard`
* **輸入**：無。
* **處理邏輯**：
  - 呼叫 `BotStatusModel.get_status()` 取得系統連線與執行狀態。
  - 呼叫 `HistoryModel.get_all()` 計算當日或近期總獲利。
* **輸出**：渲染 `dashboard.html`。
* **錯誤處理**：若資料庫尚未初始化，顯示友善提示。

### 選房分析列表
* **路徑**：`GET /rooms`
* **輸入**：無。
* **處理邏輯**：此版本預設呈現靜態或 Mock 的機台推薦資料（未來整合爬蟲後替換）。
* **輸出**：渲染 `rooms.html`。

### 選房詳細資料
* **路徑**：`GET /rooms/<room_id>`
* **輸入**：URL 參數 `room_id`。
* **處理邏輯**：根據 `room_id` 抓取進階的週期數據。
* **輸出**：渲染 `room_detail.html`。
* **錯誤處理**：如果找不到房間，導向 404 或回上一頁。

### 參數設定介面
* **路徑**：`GET /settings`
* **輸入**：無。
* **處理邏輯**：呼叫 `StrategyModel.get_strategy()`，取得設定並帶入表單。
* **輸出**：渲染 `settings.html`。

### 儲存參數設定
* **路徑**：`POST /settings/save`
* **輸入**：表單欄位 `max_loss` (float), `cashout_threshold` (float)。
* **處理邏輯**：驗證欄位是否為有效數字，呼叫 `StrategyModel.update_strategy(...)` 儲存設定。
* **輸出**：儲存後 HTTP 302 重導向（Redirect）至 `/settings`，並附帶 Flash 成功訊息。
* **錯誤處理**：若欄位格式錯誤，導回表單並顯示錯誤。

### 啟動/停止腳本
* **路徑**：`POST /bot/toggle`
* **輸入**：隱藏表單欄位或網址參數 `action` (start/stop) 或直接做 Toggle。
* **處理邏輯**：呼叫 `BotStatusModel.update_status(1 or 0)`。
* **輸出**：重導向至上一個來源頁面（`request.referrer`）或儀表板。

### 歷史紀錄查詢
* **路徑**：`GET /history`
* **輸入**：無。
* **處理邏輯**：呼叫 `HistoryModel.get_all()`。
* **輸出**：渲染 `history.html`。

## 3. Jinja2 模板清單

所有的視圖模板皆繼承自全站共用版型：
* **`base.html`**：共用的 HTML 結構，包含 Header、Sidebar 以及外部 CSS/JS 引入。

其他子模板：
* **`dashboard.html`**：繼承 base，顯示統計圖表或數據。
* **`rooms.html`**：繼承 base，顯示所有房間清單。
* **`room_detail.html`**：繼承 base，單一房間詳情。
* **`settings.html`**：繼承 base，設定表單頁面。
* **`history.html`**：繼承 base，資料表格呈現歷史資料。

## 4. 路由骨架程式碼
實作程式碼將分散在：
* `app/routes/main_routes.py` (首頁/歷史/選房相關)
* `app/routes/setting_routes.py` (策略設定/Bot 開關相關)
