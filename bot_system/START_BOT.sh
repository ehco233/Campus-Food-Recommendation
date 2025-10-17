#!/bin/bash

# 启动 Telegram 餐厅推荐机器人

echo "🤖 Starting Telegram Restaurant Recommendation Bot..."
echo ""
echo "📋 System Information:"
echo "   - Total Restaurants: 58"
echo "   - Supports: English & Chinese"
echo "   - Features: AI recommendations, Price filtering, Halal/Vegetarian options"
echo ""
echo "⚙️  Make sure you have configured config.py with:"
echo "   - TELEGRAM_BOT_TOKEN"
echo "   - DEEPSEEK_API_KEY"
echo ""
echo "🚀 Starting bot..."
echo ""

python3 bot.py

