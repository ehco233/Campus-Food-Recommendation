# 🤖 Telegram Bot System

Smart Restaurant Recommendation Bot - Providing personalized restaurant recommendations for consumers.

---

## 📂 Directory Structure

```
bot_system/
├── bot.py           # Bot Main Program (258 lines)
├── database.py      # Database Interface (173 lines)
├── llm_service.py   # AI Service (90 lines)
├── config.py        # Configuration (Contains API Keys)
├── START_BOT.sh     # Startup Script
├── README.md        # Chinese Documentation
└── README_EN.md     # This File (English)
```

---

## 🚀 Quick Start

### 1. Configure API Keys

Edit `config.py`:

```python
# Telegram Bot Token (Get from @BotFather)
TELEGRAM_BOT_TOKEN = "your_bot_token_here"

# Deepseek API Key
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

### 2. Start Bot

```bash
# Method 1: Use startup script
./START_BOT.sh

# Method 2: Run directly
python3 bot.py
```

### 3. Test

In Telegram:
1. Search for your Bot
2. Send `/start`
3. Send a query, like "I want cheap food"

---

## 📝 File Descriptions

### bot.py
- **Function**: Bot main program
- **Class**: `RecommendationBot`
- **Main Methods**:
  - `start_command()` - Handle /start
  - `help_command()` - Handle /help
  - `handle_message()` - Handle user queries
  - `parse_user_query()` - Parse query intent
  - `clean_markdown()` - Remove Markdown symbols

### database.py
- **Function**: Data interface
- **Main Functions**:
  - `load_restaurants()` - Load restaurant data (smart path detection)
  - `search_restaurants()` - Search restaurants
  - `format_restaurant_data()` - Format output
  - `detect_language()` - Language detection

### llm_service.py
- **Function**: AI recommendation generation
- **Class**: `LLMService`
- **Methods**:
  - `generate_recommendation()` - Generate recommendation text (bilingual support)

### config.py
- **Function**: Store API Keys
- **Important**: Don't commit to Git!

---

## 🔧 Dependencies

```bash
pip install python-telegram-bot==20.7
pip install openai==1.12.0
```

Or in project root:
```bash
pip install -r requirements.txt
```

---

## 🎯 Features

- ✅ Bilingual Support (Chinese & English)
- ✅ Smart Intent Parsing
- ✅ Multi-Dimensional Filtering (Price, Taste, Cuisine)
- ✅ Halal / Vegetarian Support
- ✅ Real-Time Queue Time
- ✅ AI-Driven Recommendation Reasoning

---

## 📊 Data Source

Bot reads data from `../data/restaurants.json`:
- 58 Restaurants
- 163 Menu Items
- Multilingual Support (Chinese & English)

**Path Resolution**: Uses absolute paths, works from any directory.

---

## 🐛 Troubleshooting

### Bot Not Responding
1. Check if Token in `config.py` is correct
2. Verify network connection
3. Check terminal error messages

### Can't Find Restaurant Data
```bash
# Verify data file exists
ls ../data/restaurants.json

# Regenerate data
cd ../data
python3 convert_to_json.py
```

### Import Errors
```bash
# Check if in correct directory
pwd  # Should show .../bot_system

# Verify dependencies installed
pip list | grep telegram
```

### "No Restaurants Found" Issue
**Common Causes**:
- Keyword conflict (e.g., "halal" treated as both keyword and filter)
- Database path issues (already fixed with absolute paths)

**Solution**: Already implemented in latest version:
- Dedicated boolean filters for `halal_only` and `vegetarian_only`
- Removed these terms from general cuisine keywords
- Smart path resolution for `restaurants.json`

---

## 🔄 Development Workflow

1. **Modify Code** - Edit Python files
2. **Restart Bot** - `Ctrl+C` then re-run
3. **Test** - Test in Telegram
4. **Debug** - Check terminal output

---

## 🌟 Key Features

### Intelligent Query Parsing
The bot understands natural language queries and extracts:
- **Budget**: "under 10 dollars", "便宜的" → max_price filter
- **Taste**: "not spicy", "不辣" → not_spicy filter
- **Dietary**: "halal", "vegetarian" → dedicated boolean filters
- **Cuisine**: "korean", "japanese", "川菜" → keyword search
- **Location**: "north spine", "hive" → location search

### Example Queries
```
✅ "I want halal food under 10 dollars"
✅ "推荐不辣的餐厅，预算15块"
✅ "korean food near hive"
✅ "vegetarian options with budget 8 dollars"
```

### Bilingual Output
The bot automatically detects the user's language:
- Chinese query → Chinese response
- English query → English response

Output includes:
- 📍 **Location** (bolded)
- 💰 **Price Range** (bolded)
- ⏰ **Queue Time** (bolded)
- ⭐ **Recommended Dishes** (bolded)

---

## 📞 More Information

- Feature Details: `../docs/FEATURES_EN.md`
- Project Home: `../README_EN.md`
- Data Documentation: `../data/README_EN.md`

---

**Total Lines**: ~521 lines  
**Language**: Python 3.10+  
**Dependencies**: 2 main packages

**Last Updated**: October 21, 2025  
**Version**: v2.0

