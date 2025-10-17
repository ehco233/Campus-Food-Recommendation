# 🎯 System Features Summary

This project contains two independent intelligent systems serving different user groups.

---

## 🤖 System 1: Telegram Restaurant Recommendation Bot

### 📱 Target Users
- Students, faculty, visitors
- People who need to quickly find suitable restaurants
- Users seeking personalized dining recommendations

### ✨ Core Features

#### 1. **Intelligent Restaurant Recommendations**
- Understands user needs through natural language queries and recommends suitable restaurants
- Supports bilingual queries and responses in Chinese and English
- Automatically recognizes user language preference and matches corresponding language responses
- Recommends 1-3 most suitable restaurants per query

#### 2. **Multi-Dimensional Filtering**
- **Price Filtering**: Recommends based on budget range (e.g., "under 10 dollars", "within $15")
- **Taste Filtering**: Spice level preferences (non-spicy, mild, heavy spice)
- **Cuisine Filtering**: Supports Sichuan, Cantonese, Japanese, Korean, Western and more
- **Dietary Restrictions**:
  - Halal food filtering
  - Vegetarian options filtering
- **Location Filtering**: Search by canteen or food court location (North Spine, The Hive, etc.)

#### 3. **Real-Time Information Display**
- **Basic Restaurant Info**: Name, location, cuisine type
- **Pricing Info**: Price range and average cost per person
- **Recommended Dishes**: Signature dishes of each restaurant
- **Queue Time**: Real-time estimated waiting time
- **Special Tags**: Halal certification, vegetarian options, etc.

#### 4. **AI-Powered Personalized Recommendations**
- Uses Deepseek LLM to analyze user needs
- Generates natural, conversational recommendation explanations
- Provides reasoning to help users make decisions
- Considers multiple factors for comprehensive recommendations (price, taste, queue, location)

#### 5. **User-Friendly Interaction**
- `/start` command: Display welcome message and usage guide
- `/help` command: View detailed help documentation and examples
- Natural language interaction, no special commands to learn
- Instant response, second-level recommendation results

#### 6. **Query Examples**

**Chinese Queries:**
- "推荐不辣的餐厅，10块钱以内" (Recommend non-spicy restaurant under 10 dollars)
- "北脊广场有什么好吃的？" (What's good at North Spine Plaza?)
- "想吃清真餐厅，预算15块" (Want halal food, budget 15 dollars)
- "找个排队少的西餐" (Find Western food with short queue)

**English Queries:**
- "I want halal food under 10 dollars"
- "Recommend vegetarian options"
- "What's at The Hive?"
- "Cheap Western food with short queue"

### 🔧 Technical Features

#### Data Support
- Based on **58 restaurants/stalls** with real data
- Contains **163 menu items**
- Covers multiple campus canteens and food courts
- Price range: $1 - $30

#### Intelligent Processing
- Automatically parses user intent (budget, taste, location, etc.)
- Uses regular expressions to extract structured information
- Simulates real-time queue data (0-30 minutes)
- Automatic Markdown format cleaning, plain text output

#### Extensibility
- Easy to add new restaurant data
- Supports multi-language expansion
- Customizable recommendation algorithms
- Modular API interface design

---

## 📊 System 2: Merchant Business Report System

### 👔 Target Users
- Restaurant owners, managers
- Canteen administrators
- Business decision-makers
- Operations personnel requiring data analysis support

### ✨ Core Features

#### 1. **Secure Login System**
- Password-protected access (default password: 111)
- Independent login for each restaurant
- Prevents unauthorized data access
- Logout function to protect privacy

#### 2. **Flexible Time Period Selection**
- **Month Selection**: Covers all 12 months of 2025
  - January 2025 ~ December 2025
- **Week Selection**: 4 weeks per month available
  - Week 1 (1-7)
  - Week 2 (8-14)
  - Week 3 (15-21)
  - Week 4 (22-28)
- Default selection is current month

#### 3. **Comprehensive Business Data Display**

##### 📈 Core Metric Cards
- **Total Sales**: Total sales quantity for the period (units)
- **Total Revenue**: Total income for the period (USD)
- **Average Growth Rate**: Growth percentage compared to last week
- **Best Seller**: Top-selling product

##### 📋 Detailed Sales Data Table
- **Dish Name**: All products on sale
- **This Week's Sales**: Current period sales data
- **Last Week's Sales**: Comparison baseline data
- **Growth Rate**: Percentage change (positive/negative indicator)
- **Revenue**: Revenue contributed by each product
- Color coding: Growth in green, decline in red

#### 4. **AI Business Analysis Report**

##### Report Structure (Markdown Formatted)

**1. Sales Performance Summary**
- Overall performance evaluation
- Key data interpretation
- Year-over-year and month-over-month analysis
- Performance highlights and issues

**2. Dish Performance Analysis**
- **Top Performers**: Excellent performing products
  - Sales data
  - Growth reason analysis
  - Market feedback
- **Underperformers**: Products needing improvement
  - Decline reason analysis
  - Improvement suggestions

**3. Strategic Recommendations (Business Recommendations)**
- **Inventory (Inventory Management)**:
  - Products to increase stock
  - Products to reduce inventory
  - Procurement optimization suggestions
- **Menu (Menu Optimization)**:
  - New item suggestions
  - Elimination suggestions
  - Combo meal suggestions
- **Marketing (Marketing Strategy)**:
  - Promotional activity suggestions
  - Target audience positioning
  - Promotion channel suggestions
- **Pricing (Pricing Strategy)**:
  - Price adjustment suggestions
  - Competitive analysis
  - Profit optimization

**4. Next Period Forecast**
- Sales trend predictions
- Items requiring attention
- Action Items checklist

##### Formatting Features
- **Clear Title Hierarchy**: Uses ## and ### markers
- **Bold Key Information**: Important data and suggestions in **bold**
- **Clear Item Lists**: Uses - list symbols
- **Easy to Read**: Professional yet accessible language

#### 5. **Data Visualization**

##### Statistical Card Visualization
- Gradient background (purple theme)
- Large font numeric display
- Clear label descriptions
- Responsive grid layout

##### Data Table Visualization
- Professional table design
- Hover highlight effect
- Growth rate color coding
- Easy to scan and read

#### 6. **User Experience Optimization**

##### Interface Design
- Modern gradient purple theme
- Responsive design (adapts to various screens)
- Rounded card design
- Shadow effects enhance layering

##### Interaction Design
- Smooth scrolling to report area
- Loading animation prompts
- Button hover animation effects
- One-click report regeneration

##### Information Architecture
- Simple and clear login page
- Clear main control panel functionality
- Segmented report display with clear hierarchy
- Prominent logout button position

#### 7. **Report Generation Process**

1. **Select Restaurant** → Enter password to login
2. **Select Time** → Month + Week
3. **Click Generate** → Trigger data calculation
4. **Display Data** → Statistical cards + data table
5. **AI Analysis** → Call Deepseek API
6. **Formatted Display** → Markdown to HTML
7. **Can Regenerate** → Click refresh button

### 🔧 Technical Features

#### Frontend Technology
- Pure static HTML/CSS/JavaScript
- No backend server deployment needed
- Local HTTP server operation
- Progressive loading experience

#### Data Processing
- Dynamically generates simulated sales data
- Automatically calculates growth rate and revenue
- Intelligent statistical aggregation
- Real-time data refresh

#### AI Integration
- Deepseek API calls
- Professional prompt engineering
- Markdown parsing and rendering
- Error handling and fallback

#### Security
- Password protection mechanism
- API Key not displayed in UI
- Local operation, data not uploaded
- Logout clears state

---

## 📊 System Comparison

| Feature | Telegram Bot | Merchant Report System |
|---------|--------------|------------------------|
| **User Group** | C-side users (consumers) | B-side users (merchants) |
| **Use Case** | Find restaurants, dining decisions | Operations analysis, decision support |
| **Interaction** | Chat conversation | Web interface clicks |
| **Data Type** | Restaurant info, recommendations | Sales data, analysis reports |
| **Response Speed** | Seconds | 2-5 seconds (including AI generation) |
| **Update Frequency** | Real-time | Generated by period |
| **Access Method** | Telegram App | Web browser |
| **Language Support** | Auto-detect Chinese/English | Full English |
| **Data Display** | Concise text | Charts + tables + reports |
| **Personalization** | Query-based customization | Time period-based |

---

## 🎯 Common Features

### 1. **Shared Data Source**
- Both systems use the same `restaurants.json`
- 58 restaurants/stalls data
- 163 menu items
- Unified data structure

### 2. **AI-Driven**
- Both use Deepseek LLM
- Intelligent analysis and generation
- Natural language processing
- Context understanding capability

### 3. **Multi-Language Support**
- Bot: Bilingual Chinese/English
- Report: English interface
- Data: Multi-language fields

### 4. **Easy to Maintain**
- Modular code structure
- Clear documentation
- Separate configuration files
- Easy to extend and upgrade

### 5. **User-Friendly**
- Intuitive interaction design
- Clear information display
- Fast response time
- Comprehensive error handling

---

## 🚀 Usage Scenarios

### Telegram Bot Scenarios

#### Scenario 1: Student Lunch Time
> "我现在在图书馆，想找个近的、便宜的地方吃午饭，不要太辣"
> (I'm at the library now, want to find a nearby cheap place for lunch, not too spicy)

**Bot Response:**
> 推荐你去 North Spine Food Court 的 Student Cafeteria，就在图书馆附近走路5分钟。主要是便宜实惠，6-8块钱就能吃饱，他们家的番茄炒蛋饭和青椒肉丝都不辣，味道清淡适合你。现在排队大概5分钟，直接过去就行。
> 
> (I recommend Student Cafeteria at North Spine Food Court, just a 5-minute walk from the library. It's mainly cheap and affordable, 6-8 dollars to get full. Their tomato scrambled egg rice and green pepper pork shreds are not spicy, light taste suits you well. Queue is about 5 minutes now, you can go directly.)

#### Scenario 2: International Student Looking for Halal
> "I need halal food, budget around 10 dollars"

**Bot Response:**
> I'd recommend The Halal Corner at North Spine Plaza - it's certified halal and perfect for your budget at around $8-10 per person. Try their chicken biryani or lamb kebab, both are really popular. There's about a 10-minute wait right now, which is reasonable for lunch time.

### Merchant Report System Scenarios

#### Scenario 1: Weekly Meeting Data Presentation
Manager logs into the system, selects "October 2025 - Week 2", generates report:

**Data Shown:**
- Weekly Sales: 456 units
- Revenue: $4,230
- Growth Rate: +12.5%
- Best Seller: Chicken Rice (85 units)

**AI Analysis Summary:**
> Strong performance this week, both sales and revenue exceeded expectations. Chicken rice continues to sell well, recommend increasing stock. Curry chicken rice grew 25%, consider increasing promotional efforts. Vegetarian options sales declined, suggest optimizing dish flavor or launching new items...

#### Scenario 2: Quarterly Planning Decision
Manager reviews past 4 weeks data trends:
- Week 1: +5%
- Week 2: +12%
- Week 3: +8%
- Week 4: +15%

**Based on AI Recommendations:**
- Expand capacity for high-growth products
- Adjust pricing strategy
- Launch combo meals
- Increase marketing investment

---

## 💡 Extension Possibilities

### Telegram Bot Future Features
- 📸 Image Recognition: Photo recognition of dishes
- ⭐ User Ratings: Collect user feedback
- 💾 Favorites: Save favorite restaurants
- 📍 Navigation: Map navigation to restaurants
- 🔔 Push Notifications: Promotional activity reminders
- 👥 Social Sharing: Recommend to friends

### Merchant Report System Future Features
- 📧 Email Reports: Automatic weekly report sending
- 📊 Advanced Charts: More visualization options
- 📈 Trend Prediction: Machine learning forecasting
- 💰 Cost Analysis: Profit margin calculation
- 👥 Customer Analysis: User profiling
- 🏆 Competitor Comparison: Market competition analysis
- 📱 Mobile Optimization: Responsive design
- 📄 PDF Export: Download report files

---

## 📞 Technical Support

### Documentation Resources
- `README.md` - Project overview
- `SYSTEM_GUIDE.md` - Dual system usage guide
- `FEATURES.md` - Chinese feature summary document
- `FEATURES_EN.md` - English feature summary document (current file)
- `UPDATE_LOG.md` - Update history log
- `Vendor/README.md` - Merchant system specific documentation

### Configuration Files
- `config.py` - API key configuration
- `requirements.txt` - Python dependencies
- `restaurants.json` - Restaurant data

### Startup Scripts
- `START_BOT.sh` - Start Telegram Bot
- `Vendor/start_report_server.sh` - Start report system

---

**Last Updated**: October 17, 2025  
**System Version**: v2.0  
**Data Version**: 58 restaurants, 163 menu items

