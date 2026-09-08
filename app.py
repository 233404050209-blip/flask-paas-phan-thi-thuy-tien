import os
import datetime
import platform
from flask import Flask
app = Flask(__name__)
# Bien dem luu trong RAM cua container
visit_count = 0
@app.route("/api/counter")
def counter():
    global visit_count
    visit_count += 1
    return {
        "so_lan_truy_cap": visit_count,
        "ghi_chu": "So nay se MAT khi container khoi dong lai!"
    }
@app.route("/api/info")
def info():
    ten_sinh_vien = os.environ.get(
        "STUDENT_NAME",
        "Chua dat bien moi truong"
    )
    return {
        "sinh_vien": ten_sinh_vien,
        "thoi_gian": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "he_dieu_hanh": platform.system(),
        "nguon_du_lieu": "Environment Variable tren Render, KHONG hardcode trong code"
    }
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)