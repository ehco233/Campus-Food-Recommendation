# 🎯 GP8000 - Smart Restaurant Recommendation & Business Report System

This project contains two independent intelligent systems serving both consumers and merchants.

---

## 🚀 Quick Start

### 📱 Telegram Bot (Consumer Side)

```bash
cd bot_system
python3 bot.py
```

### 📊 Business Report System (Merchant Side)

**Local Development:**
```bash
cd Vendor
./start_report_server.sh
# Visit http://localhost:8000/Vendor/business_report.html
```

**Deploy to Vercel:**
```bash
# See docs/QUICK_DEPLOY.md
```

---

## 📂 Project Structure

```
GP8000/
├── index.html                   # 🌐 Website Homepage (Business Report System)
├── package.json                 # 📦 Node.js Config (Required for Vercel)
├── vercel.json                  # ⚙️  Vercel Configuration
├── requirements.txt             # 🐍 Python Dependencies
├── README.md                    # 📖 Chinese Version
├── README_EN.md                 # 📖 This File (English Version)
├── .gitignore                   # 🔒 Git Ignore Rules
├── .vercelignore                # 🔒 Vercel Ignore Rules
│
├── 📚 docs/                     # Documentation Directory
│   ├── FEATURES.md              # Feature Documentation (Chinese) ⭐
│   └── FEATURES_EN.md           # Feature Documentation (English) ⭐
│
├── 🤖 bot_system/               # Telegram Bot System
│   ├── bot.py                   # Bot Main Program
│   ├── database.py              # Database Interface
│   ├── llm_service.py           # AI Service
│   ├── config.py                # Configuration (API Keys) ⚠️
│   ├── START_BOT.sh             # Startup Script
│   ├── README.md                # Bot System Guide (Chinese)
│   └── README_EN.md             # Bot System Guide (English)
│
├── 📊 Vendor/                   # Business Report System (Backup)
│   ├── business_report.html     # Report Page
│   ├── start_report_server.sh   # Local Startup Script
│   ├── README.md                # Documentation (English)
│   ├── REPORT_README.md         # Detailed Guide (Chinese)
│   └── REPORT_README_EN.md      # Detailed Guide (English)
│
├── ⚙️  api/                     # Serverless Functions
│   └── deepseek.js              # Deepseek API Proxy (Hides API Key)
│
└── 📦 data/                     # Data Files
    ├── restaurants.json         # 58 Restaurant Data (Main Data Source)
    ├── AI Course Data Collection 2.xlsx # Raw Excel Data
    ├── convert_to_json.py       # Excel → JSON Converter
    ├── README.md                # Data Documentation (Chinese)
    └── README_EN.md             # Data Documentation (English)
```

**Note**: 
- `index.html` is in the root directory as the website homepage, directly displaying the business report system
- `config.py` contains API Keys, protected by `.gitignore`
- `package.json` is essential for Vercel deployment

---

## 📖 Documentation Navigator

| Document | Purpose | Priority |
|----------|---------|----------|
| [FEATURES.md](docs/FEATURES.md) | Detailed Features (Chinese) | ⭐⭐⭐⭐⭐ |
| [FEATURES_EN.md](docs/FEATURES_EN.md) | Detailed Features (English) | ⭐⭐⭐⭐⭐ |
| [README_EN.md](README_EN.md) | This File | ⭐⭐⭐⭐⭐ |

---

## 🎯 Two Systems

### 🤖 System 1: Telegram Restaurant Recommendation Bot

**Target Users**: Students, Faculty, Visitors

**Core Features**:
- ✅ Smart Restaurant Recommendations (AI-Powered)
- ✅ Bilingual Support (Chinese & English)
- ✅ Multi-Dimensional Filtering (Price, Cuisine, Halal, Vegetarian)
- ✅ Real-Time Queue Time
- ✅ Based on 58 Restaurant Database

**Query Examples**:
```
"I want halal food under 10 dollars"
"推荐不辣的餐厅，预算15块"
```

### 📊 System 2: Business Report System

**Target Users**: Restaurant Owners, Managers

**Core Features**:
- ✅ Password-Protected Login
- ✅ Periodic Report Generation (By Month/Week)
- ✅ Sales Data Visualization
- ✅ AI Strategic Analysis
- ✅ Markdown Format Reports

**Highlights**:
- Full Year 2025 Data
- Real-Time Data Refresh
- Professional Business Reports
- Secure Deployment (API Key Hidden)

---

## 💻 Tech Stack

| Component | Technology |
|-----------|------------|
| **Bot Backend** | Python 3.10+, python-telegram-bot |
| **AI Service** | Deepseek API |
| **Data Processing** | Pandas, JSON |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend API** | Vercel Serverless Functions |
| **Deployment** | Vercel (Recommended), GitHub Pages |

---

## 📊 System Architecture & Code Flow

### RAG (Retrieval-Augmented Generation) - How It Works

**What is RAG?**  
Think of RAG as a smart librarian + writer combo:
- 📚 **Librarian (Retrieval)**: First, find relevant books (restaurant data)
- ✍️ **Writer (Generation)**: Then, write a personalized answer using those books

**Why RAG?**  
Without RAG, AI might "hallucinate" - recommend restaurants that don't exist or get prices wrong.  
With RAG, AI only recommends from **real, filtered data** = accurate & reliable! ✅

---

```mermaid
flowchart TD
    Start[👤 User asks:<br/>'I want halal food under $10'] --> Step1[🔍 Step 1: Understand<br/>What user wants:<br/>• Budget: $10<br/>• Dietary: Halal]
    
    Step1 --> Step2[📚 Step 2: Search Database<br/>Look through 58 restaurants<br/>in our system]
    
    Step2 --> Step3[🔎 Step 3: Filter Results<br/>Find matching restaurants:<br/>✓ Price ≤ $10<br/>✓ Halal certified<br/>→ Found 5 restaurants!]
    
    Step3 --> Step4[📝 Step 4: Prepare Information<br/>Collect details for each:<br/>• Restaurant name & location<br/>• Exact prices<br/>• Popular dishes<br/>• Queue time]
    
    Step4 --> Step5[🤖 Step 5: Ask AI to Help<br/>Give AI the 5 restaurants<br/>and ask it to write a<br/>friendly recommendation]
    
    Step5 --> Step6[💬 Step 6: AI Writes Response<br/>'I recommend The Crowded Bowl<br/>at North Spine Plaza. It serves<br/>halal food for $5-8. Try their<br/>Nasi Lemak! Only 5 min wait.']
    
    Step6 --> Send[📱 Send to User]
    
    style Start fill:#e3f2fd
    style Step3 fill:#c8e6c9
    style Step4 fill:#fff9c4
    style Step5 fill:#f8bbd0
    style Step6 fill:#f3e5f5
    style Send fill:#c8e6c9
```

**The Magic of RAG in 3 Simple Steps:**

1️⃣ **FIND** (Retrieval)  
   User says: "halal food under $10"  
   System searches: 58 restaurants → filters → finds 5 matches

2️⃣ **GIVE** (Context)  
   System gives AI these 5 real restaurants with all their details

3️⃣ **WRITE** (Generation)  
   AI writes a natural, friendly recommendation using ONLY those 5 restaurants

**Result:** Accurate, personalized, trustworthy recommendations! 🎯

---

**Why This Matters:**

| Without RAG ❌ | With RAG ✅ |
|----------------|-------------|
| AI might recommend "ABC Restaurant" that doesn't exist | AI only recommends from 58 real restaurants |
| Price might be wrong: "$5" but actually $15 | Exact prices from database: "$5-8" |
| "Not spicy" but actually very spicy | Filtered by actual criteria |
| Generic answer for everyone | Personalized based on YOUR requirements |

---

### Overall System Architecture

```mermaid
graph LR
    subgraph Consumer["🤖 Consumer Side - Telegram Bot"]
        U1[User Query] --> B1[bot.py]
        B1 --> D1[database.py]
        D1 --> L1[llm_service.py]
        L1 --> T1[Telegram Response]
    end

    subgraph Merchant["📊 Merchant Side - Business Report"]
        U2[Browser] --> H1[index.html]
        H1 --> A1[api/deepseek.js]
        A1 --> R1[Report Display]
    end

    subgraph Data["📦 Shared Data Layer"]
        E1[Excel] --> C1[convert_to_json.py]
        C1 --> J1[(restaurants.json<br/>58 restaurants)]
    end

    subgraph AI["🧠 AI Service"]
        DS[Deepseek API]
    end

    D1 <--> J1
    H1 <--> J1
    L1 <--> DS
    A1 <--> DS

    style Consumer fill:#e3f2fd
    style Merchant fill:#fff3e0
    style Data fill:#e8f5e9
    style AI fill:#f3e5f5
```

### Telegram Bot Detailed Flow

```mermaid
sequenceDiagram
    participant User as 👤 User (Telegram)
    participant Bot as bot.py
    participant Parser as parse_user_query()
    participant DB as database.py
    participant JSON as restaurants.json
    participant LLM as llm_service.py
    participant API as Deepseek API

    User->>Bot: Send query<br/>"I want halal food under $10"
    Bot->>Bot: detect_language()<br/>→ English
    Bot->>Parser: Parse query
    Parser->>Parser: Extract filters:<br/>max_price=10<br/>halal_only=True
    Parser-->>Bot: Return filters
    
    Bot->>DB: search_restaurants(max_price=10, halal_only=True)
    DB->>JSON: Load data
    JSON-->>DB: 58 restaurants
    DB->>DB: Filter by criteria
    DB-->>Bot: 5 matching restaurants
    
    Bot->>DB: format_restaurant_data(restaurants, language='en')
    DB-->>Bot: Formatted text with **bold**
    
    Bot->>LLM: generate_recommendation(query, data, language='en')
    LLM->>API: POST chat/completions<br/>(Plain text prompt)
    API-->>LLM: AI response
    LLM-->>Bot: Recommendation text
    
    Bot->>Bot: clean_markdown()<br/>Remove ** ## symbols
    Bot->>User: Send final message
```

### Business Report System Detailed Flow

```mermaid
sequenceDiagram
    participant User as 🏢 Merchant
    participant HTML as index.html
    participant JS as JavaScript
    participant SF as /api/deepseek.js<br/>(Serverless)
    participant ENV as Vercel Env Vars
    participant API as Deepseek API
    participant JSON as restaurants.json

    User->>HTML: Open website
    HTML->>JSON: fetch('/data/restaurants.json')
    JSON-->>HTML: 58 restaurants
    HTML->>User: Show login form
    
    User->>HTML: Select restaurant + Enter password
    HTML->>HTML: Validate password === "111"
    HTML->>User: Show dashboard
    
    User->>HTML: Select month + week
    User->>HTML: Click "Generate Report"
    
    HTML->>JS: generateSalesData()
    JS->>JS: Create mock sales<br/>for 5 dishes
    JS-->>HTML: Sales table + stats
    
    HTML->>SF: POST /api/deepseek<br/>{messages, temperature, max_tokens}
    SF->>ENV: Get DEEPSEEK_API_KEY
    ENV-->>SF: API Key
    SF->>API: POST with Authorization header
    API-->>SF: AI analysis response
    SF-->>HTML: Return data
    
    HTML->>JS: parseMarkdown(aiReport)
    JS->>JS: Convert ** to <strong><br/>Convert ## to <h3>
    JS-->>HTML: HTML formatted report
    HTML->>User: Display complete report
```

### Data Update Flow

```mermaid
flowchart LR
    A[📄 Excel File<br/>AI Course Data Collection 2.xlsx] --> B[🐍 convert_to_json.py]
    B --> C{Processing}
    C --> D[Group by Stall]
    C --> E[Calculate Prices]
    C --> F[Generate Multilingual Fields]
    C --> G[Handle Missing Data]
    D --> H
    E --> H
    F --> H
    G --> H
    H[📦 restaurants.json<br/>58 restaurants] --> I[🤖 Bot System<br/>database.py]
    H --> J[📊 Report System<br/>index.html]
    
    style A fill:#fff3cd
    style H fill:#d1ecf1
    style I fill:#d4edda
    style J fill:#f8d7da
```

### Key Components Interaction

```mermaid
graph LR
    subgraph "bot_system/"
        B1[bot.py<br/>258 lines] --> B2[database.py<br/>173 lines]
        B1 --> B3[llm_service.py<br/>90 lines]
        B1 --> B4[config.py<br/>API Keys]
    end
    
    subgraph "data/"
        D1[restaurants.json<br/>42KB]
    end
    
    subgraph "api/"
        A1[deepseek.js<br/>Serverless Proxy]
    end
    
    subgraph "Frontend"
        F1[index.html<br/>Business Report UI]
    end
    
    B2 --> D1
    B3 --> E1[Deepseek API]
    F1 --> D1
    F1 --> A1
    A1 --> E1
    
    style B1 fill:#bbdefb
    style D1 fill:#c8e6c9
    style A1 fill:#ffccbc
    style F1 fill:#f8bbd0
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies:
- `python-telegram-bot==20.7`
- `openai==1.12.0`
- `pandas==2.0.3`
- `openpyxl==3.1.2`

---

## 🔑 Configuration

Create `bot_system/config.py`:

```python
# Telegram Bot Token (Get from @BotFather)
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"

# Deepseek API Key
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

---

## 🚀 Deployment

### Local Development

1. **Start Telegram Bot**:
   ```bash
   cd bot_system
   python3 bot.py
   ```

2. **Start Business Report**:
   ```bash
   cd Vendor
   python3 -m http.server 8000
   ```

### Production Deployment

**Recommended: Vercel (Free + Secure)**

See: [docs/FEATURES_EN.md](docs/FEATURES_EN.md)

---

## 📊 Data Overview

- **Total Restaurants**: 58
- **Menu Items**: 163
- **Price Range**: $1 - $30
- **Locations**: Multiple campus canteens and food courts
- **Features**: Halal, Vegetarian options marked

### Update Data

```bash
cd data
# 1. Replace Excel file
# 2. Run conversion
python3 convert_to_json.py
```

---

## 🔒 Security

- ✅ API Keys not in frontend code
- ✅ Environment variables for secrets
- ✅ Serverless Functions proxy API calls
- ✅ Password-protected business reports
- ✅ .gitignore protects sensitive files

---

## 📞 Support

- 📖 Documentation: [docs/FEATURES_EN.md](docs/FEATURES_EN.md)
- 🤖 Bot Guide: [bot_system/README_EN.md](bot_system/README_EN.md)
- 📊 Report Guide: [Vendor/README.md](Vendor/README.md)

---

## 📄 License

MIT License

---

**Last Updated**: October 17, 2025  
**Version**: v2.0  
**Data Version**: 58 Restaurants, 163 Menu Items

