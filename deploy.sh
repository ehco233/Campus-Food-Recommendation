#!/bin/bash

# GP8000 项目部署脚本
# 自动化 Git 提交和部署准备

echo "🚀 GP8000 项目部署脚本"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. 检查是否在项目根目录
if [ ! -f "README.md" ] || [ ! -d "bot_system" ]; then
    echo -e "${RED}❌ 错误: 请在项目根目录运行此脚本${NC}"
    exit 1
fi

echo "📂 当前目录: $(pwd)"
echo ""

# 2. 检查 Git 状态
echo "🔍 检查 Git 状态..."
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Git 未初始化，正在初始化...${NC}"
    git init
    echo -e "${GREEN}✅ Git 初始化完成${NC}"
else
    echo -e "${GREEN}✅ Git 已初始化${NC}"
fi
echo ""

# 3. 检查敏感文件
echo "🔒 检查敏感文件保护..."

if git status | grep -q "bot_system/config.py"; then
    echo -e "${RED}❌ 警告: config.py 将被提交！请检查 .gitignore${NC}"
    echo "建议运行: echo 'bot_system/config.py' >> .gitignore"
    exit 1
else
    echo -e "${GREEN}✅ config.py 已被保护${NC}"
fi

# 搜索硬编码的 API Key
if grep -r "sk-0d8c2aa28a154314a87276b28cc3ebeb" \
    --exclude-dir=.git \
    --exclude="*.md" \
    --exclude="config.py" \
    --exclude="deploy.sh" \
    . > /dev/null 2>&1; then
    echo -e "${RED}❌ 警告: 发现硬编码的 API Key！${NC}"
    echo "请检查代码并移除 API Key"
    exit 1
else
    echo -e "${GREEN}✅ 未发现硬编码的 API Key${NC}"
fi
echo ""

# 4. 查看待提交文件
echo "📝 待提交的文件:"
git status --short
echo ""

# 5. 添加文件
echo "➕ 添加文件到 Git..."
git add .
echo -e "${GREEN}✅ 文件已添加${NC}"
echo ""

# 6. 显示将要提交的文件
echo "📋 将要提交的文件列表:"
git status --short
echo ""

# 7. 确认提交
read -p "是否继续提交? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}⚠️  已取消提交${NC}"
    exit 0
fi

# 8. 创建提交
echo ""
echo "💾 创建 Git commit..."
git commit -m "feat: restructure project with secure deployment setup

- Organize files into functional directories (docs, bot_system, data, Vendor, api)
- Add Vercel serverless functions to hide API keys
- Update all file paths for new structure
- Add comprehensive documentation in Chinese and English
- Prepare for secure cloud deployment
- Configure .gitignore to protect sensitive files

Components:
- Bot system: Telegram restaurant recommendation bot
- Vendor system: Business analytics report system
- Data: 58 restaurants with 163 menu items
- API: Serverless functions for secure Deepseek API calls
- Docs: Complete documentation (CN + EN)

Ready for Vercel deployment!"

echo -e "${GREEN}✅ 提交成功${NC}"
echo ""

# 9. 显示提交信息
echo "📊 提交统计:"
git log --oneline -1
echo ""

# 10. 检查远程仓库
echo "🌐 检查远程仓库..."
if git remote -v | grep -q "origin"; then
    echo -e "${GREEN}✅ 远程仓库已配置:${NC}"
    git remote -v
    echo ""
    
    # 询问是否推送
    read -p "是否推送到 GitHub? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "⬆️  推送到 GitHub..."
        git branch -M main
        git push -u origin main
        echo -e "${GREEN}✅ 推送成功！${NC}"
    else
        echo -e "${YELLOW}⚠️  跳过推送，稍后可手动运行:${NC}"
        echo "   git branch -M main"
        echo "   git push -u origin main"
    fi
else
    echo -e "${YELLOW}⚠️  未配置远程仓库${NC}"
    echo ""
    echo "请先添加远程仓库:"
    echo "  git remote add origin https://github.com/你的用户名/GP8000.git"
    echo ""
    echo "然后推送:"
    echo "  git branch -M main"
    echo "  git push -u origin main"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ Git 提交完成！${NC}"
echo ""
echo "📚 下一步:"
echo "1. 如果还没推送，请推送到 GitHub"
echo "2. 访问 https://vercel.com 部署项目"
echo "3. 设置环境变量: DEEPSEEK_API_KEY"
echo "4. 查看部署指南: cat DEPLOY_CHECKLIST.md"
echo ""
echo "🎉 祝部署顺利！"

