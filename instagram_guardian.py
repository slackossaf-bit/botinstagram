#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🛡️ الخادم B - الحارس
- يراقب الخادم A ويمنعه من السبات
- لا ينشر أي شيء، فقط يبقي الخادم A نشطاً
"""

import time
import threading
import requests
from flask import Flask

# ============================================================
# 🌐 رابط الخادم الآخر (الخادم A)
# ============================================================
OTHER_SERVER_URL = "https://instagram-bot-a.onrender.com/keepalive"  # رابط الخادم A
# ============================================================

# ============================================================
# 🌐 خادم Flask للـ Keep-Alive
# ============================================================
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ الخادم B (الحارس) يعمل!", 200

@app.route('/keepalive')
def keepalive():
    return "✅ أنا مستيقظ!", 200

def run_web_server():
    app.run(host='0.0.0.0', port=8080, debug=False)

# ============================================================
# 📤 إرسال طلبات Keep-Alive إلى الخادم A
# ============================================================
def send_keepalive():
    """إرسال طلب إلى الخادم A كل 5 دقائق"""
    while True:
        try:
            response = requests.get(OTHER_SERVER_URL, timeout=10)
            print(f"✅ تم إرسال طلب إلى الخادم A: {response.status_code}")
        except Exception as e:
            print(f"❌ فشل الاتصال بالخادم A: {e}")
        
        time.sleep(300)  # 5 دقائق

# ============================================================
# 🚀 التشغيل الرئيسي
# ============================================================
if __name__ == "__main__":
    print("="*60)
    print("🛡️ الخادم B - الحارس")
    print("📡 يراقب الخادم A ويمنعه من السبات")
    print("="*60)
    
    # تشغيل خادم الويب
    print("\n🌐 جاري تشغيل خادم Keep-Alive...")
    threading.Thread(target=run_web_server, daemon=True).start()
    print("✅ خادم Keep-Alive يعمل على المنفذ 8080")
    
    # بدء مهمة إرسال الطلبات
    print("🔄 جاري تشغيل مهمة إرسال الطلبات إلى الخادم A...")
    threading.Thread(target=send_keepalive, daemon=True).start()
    print("✅ سيتم إرسال طلبات إلى الخادم A كل 5 دقائق")
    
    print("\n🛑 للإيقاف: Ctrl+C")
    print("="*60 + "\n")
    
    # البقاء في وضع التشغيل
    while True:
        time.sleep(60)
