# Restaurant Business Report System

## 📊 System Overview

This is a comprehensive restaurant business reporting system that provides:
- Weekly sales analysis
- AI-powered insights and recommendations
- Performance tracking across different time periods

## 📁 Data Source

**Current Data:** `AI Course Data Collection 2.xlsx`
- **Total Restaurants:** 58 food stalls/restaurants
- **Data Points:** 163 menu items across various canteens
- **Converted to:** `restaurants.json` (automatically generated)

### Data Structure

Each restaurant entry includes:
- **Name & Location:** Restaurant name and canteen location
- **Cuisine Type:** Category of food (Western, Chinese, Japanese, etc.)
- **Price Information:** Price range and average price
- **Special Features:** Halal certification, Vegetarian options
- **Menu Items:** Complete list of available dishes with prices
- **Recommended Dishes:** Top 3 menu items

## 🚀 Quick Start

### 1. Start the Server

```bash
cd Vendor
./start_report_server.sh
```

Or manually:
```bash
cd /path/to/GP8000
python3 -m http.server 8000
```

### 2. Access the System

Open in browser: **http://localhost:8000/Vendor/business_report.html**

### 3. Login

- **Password:** `111` (default for all restaurants)

### 4. Generate Reports

1. Select a restaurant
2. Choose month (October/November/December 2024)
3. Select week (Week 1-4)
4. Click "Generate Report"

## 📊 Report Contents

### Business Overview
- Total Sales
- Total Revenue
- Average Growth Rate
- Top Selling Dish

### Sales Data Table
Detailed breakdown showing:
- Current week vs last week sales
- Growth percentage
- Revenue by dish

### AI Strategic Analysis
Comprehensive analysis including:
- **Sales Performance Summary**
- **Dish Performance Analysis**
- **Strategic Recommendations**
- **Next Period Forecast**

## 🔄 Updating Data

To update restaurant data from a new Excel file:

```bash
# 1. Replace the Excel file
cp "new_data.xlsx" "AI Course Data Collection 2.xlsx"

# 2. Run conversion script
python3 convert_to_json.py

# 3. Verify the output
# Check restaurants.json is updated

# 4. Restart the server (if running)
```

## 📝 File Structure

```
GP8000/
├── AI Course Data Collection 2.xlsx  # Source data
├── restaurants.json                  # Generated restaurant data (58 restaurants)
├── convert_to_json.py               # Conversion script
└── Vendor/
    ├── business_report.html         # Main system page
    ├── start_report_server.sh       # Quick start script
    └── README.md                     # This file
```

## 🔐 Security

- **Password:** Default is `111` for all restaurants
- **API Key:** Hidden in code (not visible to users)
- **Data:** All processing happens locally in browser

## 🎯 Features

### Current Features
✅ Login system with password protection
✅ Month and week selection
✅ Mock sales data generation
✅ AI-powered analysis using Deepseek API
✅ Clean, English interface
✅ Responsive design

### Data Features
✅ 58 restaurants from multiple canteens
✅ Price range: $1 - $30
✅ Multiple cuisine types
✅ Halal and vegetarian options marked
✅ Complete menu listings

## 📍 Restaurant Locations

Data covers multiple food courts:
- North Spine Plaza
- The Hive
- Canteen 4
- Canteen 9
- And more...

## 💡 Tips

1. **Password**: Default is `111` - same for all restaurants
2. **Month Selection**: Choose from October, November, or December 2024
3. **Week Selection**: Weeks are automatically dated (1-7, 8-14, etc.)
4. **AI Report**: Takes a few seconds to generate - be patient
5. **Data Refresh**: Click "Regenerate Report" for new mock data

## 🛠️ Troubleshooting

### Problem: Can't access the page
**Solution:** Make sure you're running a local server (not opening file directly)

### Problem: No restaurants showing
**Solution:** Check that `restaurants.json` exists in the parent directory

### Problem: AI report fails
**Solution:** Check internet connection and try again

### Problem: Login doesn't work
**Solution:** Password is `111` (three ones)

## 📊 Sample Restaurants

Here are some examples from the current data:

1. **Pen & Inc** (North Spine Plaza)
   - Western cuisine
   - Average price: $25.9
   - Halal certified

2. **The Crowded Bowl Salad** (North Spine Plaza)
   - Vegetarian
   - Average price: $4.9
   - Halal certified

3. **Each a Cup** (North Spine Plaza)
   - Beverages
   - Average price: $3.3
   - Halal certified

And 55 more restaurants...

## 🔄 Data Updates

Last updated: Generated from `AI Course Data Collection 2.xlsx`
Total restaurants: 58
Total menu items: 163

---

**For detailed technical documentation, see `REPORT_README.md`**

