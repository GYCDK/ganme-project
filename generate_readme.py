import random
from datetime import datetime

titles = [
    "🚀 游戏加速器推荐（2026最新｜稳定低延迟）",
    "🔥 免费游戏加速器推荐｜延迟降低50%",
    "🎮 Steam/LOL加速器推荐（新手必看）",
    "⚡ 游戏延迟高？最强加速器推荐",
]

descriptions = [
    "实测低延迟，稳定不掉线",
    "支持Steam/LOL/PUBG/Apex",
    "一键加速，小白也能用",
    "海外游戏专线优化",
]

games = ["Steam", "LOL", "PUBG", "Apex", "原神"]

latency_data = [
    ("Steam", "180ms", "60ms"),
    ("LOL", "120ms", "40ms"),
    ("PUBG", "200ms", "70ms"),
    ("Apex", "220ms", "80ms"),
]

title = random.choice(titles)
desc = random.choice(descriptions)

content = f"""# {title}

> 🎮 {desc}
> 💡 持续更新中（自动生成）

---

## 🔥 为什么你需要游戏加速器？

- ❌ 延迟高
- ❌ 游戏卡顿
- ❌ 掉线严重

👉 使用加速器可以明显改善体验

---

## 🏆 主流加速器对比

| 加速器 | 推荐指数 |
|--------|--------|
| 雷神加速器 | ⭐⭐⭐⭐⭐ |
| UU加速器 | ⭐⭐⭐⭐ |
| 奇游加速器 | ⭐⭐⭐⭐ |

---

## 🎁 免费兑换码

---

## 📊 延迟对比

| 游戏 | 未加速 | 加速后 |
|------|------|------|
"""

for g, before, after in latency_data:
    content += f"| {g} | {before} | {after} |\n"

content += f"""

---

## 📢 总结

👉 推荐使用：雷神加速器 + GYCDK

⏰ 更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
