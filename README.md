# 🎯 GP8000 - 智能餐厅推荐与商家报告系统

本项目包含两个独立的智能系统，分别服务于消费者和商家。

---

## 🚀 快速开始

### 📱 Telegram Bot（消费者端）

```bash
cd bot_system
python3 bot.py
```

### 📊 商家报告系统（商家端）

**本地运行：**
```bash
cd Vendor
./start_report_server.sh
# 访问 http://localhost:8000/Vendor/business_report.html
```

**部署到 Vercel：**
```bash
# 见 docs/QUICK_DEPLOY.md
```

---

## 📂 项目结构

```
GP8000/
├── README.md                    # 本文件
├── requirements.txt             # Python 依赖
├── vercel.json                  # Vercel 配置
│
├── 📚 docs/                     # 所有文档
│   ├── README.md                # 项目总览（中文版）
│   ├── FEATURES.md              # 功能说明（中文）
│   ├── FEATURES_EN.md           # 功能说明（英文）
│   ├── SYSTEM_GUIDE.md          # 使用指南
│   ├── DEPLOYMENT_GUIDE.md      # 详细部署教程
│   ├── QUICK_DEPLOY.md          # 快速部署（5分钟）
│   ├── PROJECT_STRUCTURE.md     # 项目结构说明
│   └── UPDATE_LOG.md            # 更新日志
│
├── 🤖 bot_system/               # Telegram Bot 系统
│   ├── bot.py                   # 机器人主程序
│   ├── database.py              # 数据库接口
│   ├── llm_service.py           # AI 服务
│   ├── config.py                # 配置（API Keys）
│   └── START_BOT.sh             # 启动脚本
│
├── 📊 Vendor/                   # 商家报告系统（前端）
│   ├── business_report.html     # 报告页面
│   ├── start_report_server.sh   # 启动脚本
│   └── README.md                # 说明文档
│
├── ⚙️  api/                     # 后端 API（Serverless）
│   └── deepseek.js              # Deepseek API 代理
│
└── 📦 data/                     # 数据文件
    ├── restaurants.json         # 58家餐厅数据
    ├── AI Course Data Collection 2.xlsx
    └── convert_to_json.py       # Excel 转 JSON 工具
```

---

## 📖 文档导航

| 文档 | 用途 | 推荐度 |
|------|------|--------|
| [FEATURES.md](docs/FEATURES.md) | 详细功能说明（中文） | ⭐⭐⭐⭐⭐ |
| [FEATURES_EN.md](docs/FEATURES_EN.md) | 详细功能说明（英文） | ⭐⭐⭐⭐⭐ |
| [QUICK_DEPLOY.md](docs/QUICK_DEPLOY.md) | 5分钟快速部署 | ⭐⭐⭐⭐⭐ |
| [SYSTEM_GUIDE.md](docs/SYSTEM_GUIDE.md) | 完整使用指南 | ⭐⭐⭐⭐ |
| [DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) | 详细部署方案 | ⭐⭐⭐⭐ |
| [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) | 项目结构说明 | ⭐⭐⭐ |

---

## 🎯 两大系统

### 🤖 系统1：Telegram 餐厅推荐机器人

**目标用户**：学生、教职工、访客

**核心功能**：
- ✅ 智能餐厅推荐（AI 驱动）
- ✅ 中英文双语支持
- ✅ 多维度筛选（价格、菜系、Halal、素食）
- ✅ 实时排队时间
- ✅ 基于58家餐厅数据

**查询示例**：
```
"I want halal food under 10 dollars"
"推荐不辣的餐厅，预算15块"
```

### 📊 系统2：商家营业报告系统

**目标用户**：餐厅老板、经理、管理者

**核心功能**：
- ✅ 密码保护登录
- ✅ 周期报告生成（按月/周）
- ✅ 销售数据可视化
- ✅ AI 战略分析
- ✅ Markdown 格式报告

**特点**：
- 2025年全年数据
- 实时数据刷新
- 专业商业报告
- 安全部署（API Key 隐藏）

---

## 💻 技术栈

| 组件 | 技术 |
|------|------|
| **Bot 后端** | Python 3.10+, python-telegram-bot |
| **AI 服务** | Deepseek API |
| **数据处理** | Pandas, JSON |
| **前端** | HTML5, CSS3, JavaScript |
| **后端 API** | Vercel Serverless Functions |
| **部署** | Vercel (推荐), GitHub Pages |

---

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

依赖包：
- `python-telegram-bot==20.7`
- `openai==1.12.0`
- `pandas==2.0.3`
- `openpyxl==3.1.2`

---

## 🔑 配置

创建 `bot_system/config.py`：

```python
# Telegram Bot Token (从 @BotFather 获取)
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"

# Deepseek API Key
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

---

## 🚀 部署

### 本地开发

1. **启动 Telegram Bot**：
   ```bash
   cd bot_system
   python3 bot.py
   ```

2. **启动商家报告**：
   ```bash
   cd Vendor
   python3 -m http.server 8000
   ```

### 生产部署

**推荐：Vercel（免费 + 安全）**

详见：[docs/QUICK_DEPLOY.md](docs/QUICK_DEPLOY.md)

---

## 📊 数据说明

- **餐厅数量**：58家
- **菜单项目**：163个
- **价格范围**：$1 - $30
- **位置**：校园多个食堂和美食广场
- **特色**：支持 Halal、Vegetarian 标注

### 更新数据

```bash
cd data
# 1. 替换 AI Course Data Collection 2.xlsx
# 2. 运行转换
python3 convert_to_json.py
```

---

## 🔒 安全性

- ✅ API Key 不在前端代码中
- ✅ 使用环境变量存储密钥
- ✅ Serverless Functions 代理 API 调用
- ✅ 密码保护商家报告
- ✅ .gitignore 保护敏感文件

---

## 📞 支持

- 📖 查看 [docs/SYSTEM_GUIDE.md](docs/SYSTEM_GUIDE.md)
- 🚀 快速部署 [docs/QUICK_DEPLOY.md](docs/QUICK_DEPLOY.md)
- 📝 功能说明 [docs/FEATURES.md](docs/FEATURES.md)

---

## 📄 License

MIT License

---

**最后更新**: 2025年10月17日  
**版本**: v2.0  
**数据版本**: 58家餐厅，163个菜单项

