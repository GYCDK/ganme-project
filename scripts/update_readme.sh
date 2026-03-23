#!/bin/bash

DATE=$(date '+%Y-%m-%d %H:%M:%S')

RECOMMEND="👉 雷神加速器（稳定低延迟首选）"

LOG="今天测试下来，雷神加速器在晚高峰依然很稳"

TIP="建议优先选择低延迟稳定线路"

sed -i "s|<!--LAST_UPDATE-->|$DATE|" README.md
sed -i "s|<!--RECOMMEND_LIST-->|$RECOMMEND|" README.md
sed -i "s|<!--DAILY_LOG-->|$LOG|" README.md
sed -i "s|<!--DAILY_TIP-->|$TIP|" README.md

sed -i "s|$DATE|<!--LAST_UPDATE-->|" README.md
sed -i "s|$RECOMMEND|<!--RECOMMEND_LIST-->|" README.md
sed -i "s|$LOG|<!--DAILY_LOG-->|" README.md
sed -i "s|$TIP|<!--DAILY_TIP-->|" README.md
