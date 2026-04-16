from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/dashboard')
def dashboard():
    """
    HTTP GET: / 或是 /dashboard
    
    功能: 顯示首頁儀表板
    邏輯:
      1. 從 BotStatusModel 取得自動化腳本開啟與否。
      2. 從 HistoryModel 取得近期獲利，計算總收益。
      3. 渲染 'dashboard.html'
    """
    pass

@main_bp.route('/rooms')
def rooms():
    """
    HTTP GET: /rooms
    
    功能: 選房分析列表
    邏輯:
      1. 取得演算法或爬蟲推薦的高勝率房間。
      2. 渲染 'rooms.html' 顯示房間卡片。
    """
    pass

@main_bp.route('/rooms/<room_id>')
def room_detail(room_id):
    """
    HTTP GET: /rooms/<room_id>
    
    功能: 選房詳細資料
    邏輯:
      1. 驗證該 room_id 是否存在。
      2. 取出該房間的歷史爆分週期資訊。
      3. 渲染 'room_detail.html'
    """
    pass

@main_bp.route('/history')
def history():
    """
    HTTP GET: /history
    
    功能: 歷史紀錄查詢頁
    邏輯:
      1. 從 HistoryModel 抓回所有已結算的下注與獲利資料。
      2. 渲染 'history.html'，以表格呈現清單。
    """
    pass
