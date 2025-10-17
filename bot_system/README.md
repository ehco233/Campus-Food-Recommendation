# 🤖 Telegram Bot 系统

智能餐厅推荐机器人 - 为消费者提供个性化餐厅推荐。

---

## 📂 目录结构

```
bot_system/
├── bot.py           # 机器人主程序（258行）
├── database.py      # 数据库接口（167行）
├── llm_service.py   # AI 服务（90行）
├── config.py        # 配置文件（包含 API Keys）
├── START_BOT.sh     # 启动脚本
└── README.md        # 本文件
```

---

## 🚀 快速启动

### 1. 配置 API Keys

编辑 `config.py`：

```python
# Telegram Bot Token (从 @BotFather 获取)
TELEGRAM_BOT_TOKEN = "your_bot_token_here"

# Deepseek API Key
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

### 2. 启动 Bot

```bash
# 方法1: 使用启动脚本
./START_BOT.sh

# 方法2: 直接运行
python3 bot.py
```

### 3. 测试

在 Telegram 中：
1. 搜索你的 Bot
2. 发送 `/start`
3. 发送查询，如 "I want cheap food"

---

## 📝 文件说明

### bot.py
- **功能**: 机器人主程序
- **类**: `RecommendationBot`
- **主要方法**:
  - `start_command()` - 处理 /start
  - `help_command()` - 处理 /help
  - `handle_message()` - 处理用户查询
  - `parse_user_query()` - 解析查询意图

### database.py
- **功能**: 数据接口
- **主要函数**:
  - `load_restaurants()` - 加载餐厅数据
  - `search_restaurants()` - 搜索餐厅
  - `format_restaurant_data()` - 格式化输出
  - `detect_language()` - 语言检测

### llm_service.py
- **功能**: AI 推荐生成
- **类**: `LLMService`
- **方法**:
  - `generate_recommendation()` - 生成推荐文本

### config.py
- **功能**: 存储 API Keys
- **重要**: 不要提交到 Git！

---

## 🔧 依赖

```bash
pip install python-telegram-bot==20.7
pip install openai==1.12.0
```

或在项目根目录：
```bash
pip install -r requirements.txt
```

---

## 🎯 功能特性

- ✅ 中英文双语支持
- ✅ 智能意图解析
- ✅ 多维度筛选（价格、口味、菜系）
- ✅ Halal / Vegetarian 支持
- ✅ 实时排队时间
- ✅ AI 驱动的推荐理由

---

## 📊 数据来源

Bot 从 `../data/restaurants.json` 读取数据：
- 58家餐厅
- 163个菜单项
- 多语言支持（中英文）

---

## 🐛 故障排查

### Bot 不响应
1. 检查 `config.py` 中的 Token 是否正确
2. 确认网络连接正常
3. 查看终端错误信息

### 找不到餐厅数据
```bash
# 确认数据文件存在
ls ../data/restaurants.json

# 重新生成数据
cd ../data
python3 convert_to_json.py
```

### Import 错误
```bash
# 检查是否在正确目录
pwd  # 应该显示 .../bot_system

# 确认依赖已安装
pip list | grep telegram
```

---

## 🔄 开发流程

1. **修改代码** - 编辑 Python 文件
2. **重启 Bot** - `Ctrl+C` 然后重新运行
3. **测试** - 在 Telegram 中测试
4. **调试** - 查看终端输出

---

## 📞 更多信息

- 功能详情: `../docs/FEATURES.md`
- 使用指南: `../docs/SYSTEM_GUIDE.md`
- 项目主页: `../README.md`

---

**代码行数**: ~515 行  
**语言**: Python 3.10+  
**依赖**: 2个主要包

