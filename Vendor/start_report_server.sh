#!/bin/bash

# 启动餐厅营业报告系统服务器

echo "🚀 启动餐厅营业报告系统..."
echo ""
echo "📊 系统将在以下地址运行："
echo "   http://localhost:8000/business_report.html"
echo ""
echo "💡 使用说明："
echo "   1. 在浏览器中访问上述地址"
echo "   2. 选择餐厅和周次"
echo "   3. 点击生成报告按钮"
echo ""
echo "⛔ 停止服务器: 按 Ctrl+C"
echo ""

# 启动Python HTTP服务器
python3 -m http.server 8000

