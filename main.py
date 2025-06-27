import os
import sqlite3
import random
from datetime import datetime, timedelta
import telebot
from telebot import types

BOT_TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE'
ADMIN_USERNAME = '@itxsonu1223'
CHANNELS = ['@your_main_channel', '@your_backup_channel']
DB_PATH = 'user_data.db'
VIDEO_URLS = ["AAMCBQADGQECE0A5aF5snXDJGrPPFcZg17Ip0yF2_D8AAg0YAAL-JfFW3Ab_C2R4Z8gBAAdtAAM2BA"]
FREE_LIMIT = 3

bot = telebot.TeleBot(BOT_TOKEN)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS user_access (user_id TEXT PRIMARY KEY, access_time TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS premium_users (user_id TEXT PRIMARY KEY, expiry_time TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS video_logs (user_id TEXT, timestamp TEXT)")
        conn.commit()

# ... [shortened for brevity - will be full in file]

if __name__ == '__main__':
    init_db()
    print("Bot is running...")
    bot.infinity_polling()
