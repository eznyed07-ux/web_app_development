from flask import Blueprint, render_template, request, redirect, url_for, flash

setting_bp = Blueprint('setting', __name__)

@setting_bp.route('/settings')
def settings():
    """
    HTTP GET: /settings
    
    功能: 參數設定介面
    邏輯:
      1. 呼叫 StrategyModel.get_strategy() 獲取資料。
      2. 帶入模板變數，渲染 'settings.html' 呈現表單。
    """
    pass

@setting_bp.route('/settings/save', methods=['POST'])
def save_settings():
    """
    HTTP POST: /settings/save
    
    功能: 儲存參數設定
    邏輯:
      1. 接收表單傳入的 max_loss 與 cashout_threshold。
      2. 進行格式驗證。
      3. 呼叫 StrategyModel.update_strategy() 更新到資料庫。
      4. 產生 Flash 提示訊息，重導回 /settings 頁面。
    """
    pass

@setting_bp.route('/bot/toggle', methods=['POST'])
def toggle_bot():
    """
    HTTP POST: /bot/toggle
    
    功能: 啟動或停止掛機腳本
    邏輯:
      1. 根據傳入的 action，判定切換為開啟(1) 或 關閉(0)。
      2. 呼叫 BotStatusModel.update_status()。
      3. 重導向回 request.referrer 來源頁面帶上 Flash 通知。
    """
    pass
