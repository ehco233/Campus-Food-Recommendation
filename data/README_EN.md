# 📦 Data Directory

Stores all data files and data processing tools for the project.

---

## 📂 Directory Contents

```
data/
├── restaurants.json                      # Restaurant Data (Main Data File)
├── AI Course Data Collection 2.xlsx      # Raw Excel Data
├── convert_to_json.py                    # Excel to JSON Converter
├── README.md                             # Chinese Documentation
└── README_EN.md                          # This File (English)
```

---

## 📊 Data File Description

### restaurants.json

**Purpose**: Main data source for all systems

**Contents**:
- 58 Restaurants/Stalls
- 163 Menu Items
- Multilingual Fields (Chinese & English)

**Data Structure**:
```json
[
  {
    "id": 1,
    "name": {
      "zh": "餐厅中文名",
      "en": "Restaurant English Name"
    },
    "location": {
      "zh": "位置中文",
      "en": "Location English"
    },
    "cuisine": {
      "zh": "菜系中文",
      "en": "Cuisine English"
    },
    "price_range": "5-10",
    "avg_price": 7.5,
    "halal": false,
    "vegetarian": true,
    "spicy": false,
    "recommended_dishes": {
      "zh": "推荐菜品中文",
      "en": "Recommended Dishes English"
    },
    "description": {
      "zh": "描述中文",
      "en": "Description English"
    },
    "all_menus": [
      "Dish 1",
      "Dish 2",
      "..."
    ]
  }
]
```

**File Size**: 42KB  
**Format**: JSON (UTF-8)  
**Encoding**: Unicode

---

### AI Course Data Collection 2.xlsx

**Purpose**: Original data source

**Contains**:
- Stall Name
- Canteen Location
- Cuisine Type
- Menu Items
- Prices

**Note**: This file is a backup; actual usage relies on `restaurants.json`

---

### convert_to_json.py

**Purpose**: Excel to JSON conversion tool

**Functions**:
- Read Excel file
- Group by stall
- Calculate price range and average price
- Generate multilingual fields
- Handle missing data
- Output JSON file

**Usage**:
```bash
cd data
python3 convert_to_json.py
```

**Output**: `restaurants.json` (overwrites existing file)

---

## 🔄 Data Update Process

### Complete Update

1. **Prepare New Data**
   ```bash
   # Replace Excel file
   cp "new_data.xlsx" "AI Course Data Collection 2.xlsx"
   ```

2. **Run Conversion**
   ```bash
   cd data
   python3 convert_to_json.py
   ```

3. **Verify Data**
   ```bash
   # Check generated JSON
   cat restaurants.json | jq length  # Check restaurant count
   ```

4. **Restart Systems**
   ```bash
   # Bot will automatically reload
   # Report system: refresh page
   ```

### Manual Editing

After directly editing `restaurants.json`:
- Bot: Restart `bot.py`
- Report: Refresh browser

---

## 📊 Data Statistics

| Metric | Value |
|--------|-------|
| Total Restaurants | 58 |
| Menu Items | 163 |
| Price Range | $1 - $30 |
| Average Price | ~$10 |
| Halal Restaurants | Some |
| Vegetarian Options | Some |
| Data Languages | Chinese + English |

---

## 🔍 Data Field Descriptions

### Required Fields
- `id` - Unique identifier
- `name` - Restaurant name (multilingual)
- `cuisine` - Cuisine type (multilingual)
- `price_range` - Price range (string)
- `avg_price` - Average price (number)

### Optional Fields
- `location` - Location (multilingual)
- `halal` - Halal certified (boolean)
- `vegetarian` - Vegetarian options available (boolean)
- `spicy` - Spicy dishes (boolean)
- `recommended_dishes` - Recommended dishes (multilingual)
- `description` - Description (multilingual)
- `all_menus` - All menu items (array)

---

## 🛠️ Utility Scripts

### convert_to_json.py Details

**Main Steps**:
1. Read Excel file
2. Group by Stall Name
3. Calculate for each stall:
   - Minimum price
   - Maximum price
   - Average price
4. Select recommended dishes (top 3)
5. Generate multilingual fields
6. Handle missing values
7. Output JSON

**Error Handling**:
- Excel file not found → Use default data
- Data format error → Skip and warn
- Invalid price → Use default value

---

## 📞 Data Troubleshooting

### Problem 1: JSON file doesn't exist
```bash
cd data
python3 convert_to_json.py
```

### Problem 2: Data format error
Check JSON format:
```bash
cat restaurants.json | jq .
```

### Problem 3: Bot can't find data
Verify path:
```bash
# From bot_system directory
ls ../data/restaurants.json
```

### Problem 4: Report system can't load
Verify path:
```bash
# From Vendor directory
ls ../data/restaurants.json
```

---

## 📝 Notes

1. **Don't manually modify all_menus**, use the conversion tool to update
2. **Backup original Excel file** to prevent data loss
3. **Test after updates** to ensure both systems work properly
4. **Maintain multilingual consistency**, Chinese and English should correspond

---

## 🔗 Related Documentation

- Project Structure: `../docs/PROJECT_STRUCTURE.md`
- Bot System: `../bot_system/README_EN.md`
- Report System: `../Vendor/README.md`

---

**Data Version**: v2.0  
**Last Updated**: October 17, 2025  
**Data Source**: AI Course Data Collection

