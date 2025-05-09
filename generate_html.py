import hashlib

from datetime import datetime, timedelta
import hashlib
import os

# 한국 시간으로 오늘 날짜
today = (datetime.utcnow() + timedelta(hours=9)).strftime("%Y-%m-%d")
token = hashlib.sha256(("secretkey" + today).encode()).hexdigest()[:8]
filename = f"board_{token}.html"

# HTML 템플릿 내용
html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>전광판</title>
  <style>
    html, body {{
      margin: 0;
      padding: 0;
      height: 100%;
      background: black;
      overflow: hidden;
    }}
    iframe {{
      width: 100vw;
      height: 100vh;
      border: none;
    }}
  </style>
  <script>
    setInterval(() => location.reload(), 30000); // 30초마다 새로고침
  </script>
</head>
<body>
  <iframe
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTvfx5eFL1CTC-hG6Ovhunf44oj7aQ8W2NeCMgx9jLOFFNtyrF2RurcBrr9uJVzlJBJ_HMguOQsd_lY/pubhtml?gid=894608935&single=true&widget=true&headers=false&range=C8:E34">
  </iframe>
</body>
</html>
"""

# site 폴더 비우고 새 파일만 생성
site_path = "site"
if not os.path.exists(site_path):
    os.makedirs(site_path)
else:
    for f in os.listdir(site_path):
        os.remove(os.path.join(site_path, f))

with open(os.path.join(site_path, filename), "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 생성 완료: {filename}")
