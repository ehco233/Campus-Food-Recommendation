# Restaurant Business Report System - User Guide

## 📋 Feature Overview

This is an AI-powered restaurant business report generation system that helps restaurant merchants:
- 📊 View weekly sales data
- 📈 Analyze dish sales trends
- 🤖 Get AI-driven smart analysis and recommendations
- 💡 Optimize operational decisions

## 🚀 How to Use

### 1. Access the Report System

**Method 1: Cloud Deployment (Recommended)**
Visit the deployed website directly (if deployed to Vercel)

**Method 2: Local Server**
```bash
cd Vendor
./start_report_server.sh
# Then visit: http://localhost:8000/Vendor/business_report.html
```

**Method 3: Direct File Access**
Open `business_report.html` in your browser (may have CORS issues)

### 2. Login

1. **Select Restaurant**: Choose from the dropdown list
2. **Enter Password**: Default is `111` for all restaurants
3. **Click Login**: Enter the dashboard

### 3. Generate Report

1. **Select Month**: October, November, or December 2025
2. **Select Week**: Week 1-4 (with specific dates)
3. **Click "Generate Report"**: System will:
   - Generate mock sales data
   - Calculate statistics
   - Call AI to generate professional analysis report

## 📊 Report Contents

### 1. Business Overview

Four key metric cards:
- **Total Sales**: Total units sold this week
- **Total Revenue**: Total income this week
- **Average Growth Rate**: Average growth compared to last week
- **Best Seller**: Highest selling dish

### 2. Dish Sales Data Table

Detailed display for each dish:
- Dish name
- This week's sales
- Last week's sales
- Growth rate (green for positive, red for negative)
- Revenue

### 3. AI Strategic Analysis Report

Includes:
- ✅ **Sales Trend Analysis**: Overall sales performance evaluation
- ✅ **Dish Performance Analysis**: Identification of best and underperforming dishes
- ✅ **Operational Recommendations**: Inventory, menu, and marketing suggestions
- ✅ **Next Week Forecast**: Data-based trend predictions

## 🎨 System Features

### 1. Modern Interface Design
- Gradient color theme
- Responsive layout
- Smooth animation effects
- Intuitive data visualization

### 2. Smart Data Generation
- Based on real restaurant data
- Simulates realistic sales trends
- Random but reasonable data ranges

### 3. AI Analysis Capabilities

Uses Deepseek API to provide:
- Professional data analysis
- Practical operational suggestions
- Accurate trend forecasting
- Actionable improvement plans

## 🔧 Technical Implementation

### Frontend Technologies
- **HTML5**: Page structure
- **CSS3**: Styling and animations
- **JavaScript**: Interactive logic

### Data Source
- Read real restaurant data from `restaurants.json`
- Dynamically generate weekly sales data
- Calculate growth rates and revenue

### AI Integration
- **Secure API Calls**: Uses Vercel Serverless Function (`/api/deepseek`)
- **API Key Protection**: Hidden from frontend, stored in environment variables
- **Structured Data**: Send formatted data
- **Professional Analysis**: Receive expert reports
- **Real-Time Display**: Show results immediately

## 📝 Data Description

### Mock Data Rules
1. **Sales Range**: 50-150 units/week
2. **Growth Rate**: Calculated based on week-over-week comparison
3. **Revenue**: Sales × Dish Price × Random Coefficient
4. **Dish Quantity**: Maximum 5 dishes displayed

### Real Data
- Restaurant names, locations, cuisines from actual data
- Dish names from real menus
- Price ranges based on actual data

## 🎯 Use Cases

### 1. Weekly Meetings
- Quickly generate this week's business report
- Compare with last week's data
- Discuss improvement measures

### 2. Decision Support
- Inventory procurement decisions
- Menu adjustment decisions
- Marketing activity planning

### 3. Trend Monitoring
- Track dish performance
- Identify sales patterns
- Forecast future trends

## 💡 Usage Tips

### 1. Regular Review
- Generate reports weekly
- Compare data across different weeks
- Track improvement effectiveness

### 2. Combine with Reality
- AI suggestions are for reference only
- Consider actual circumstances
- Account for seasonal and holiday factors

### 3. Data Recording
- Save weekly reports
- Build historical database
- Use for long-term analysis

## 🔐 Security Notes

1. **API Key Protection**
   - Never exposed in frontend code
   - Stored in Vercel environment variables
   - Accessed only through serverless proxy
   - Regular key rotation recommended

2. **Data Privacy**
   - Local processing, data secure
   - Data transmitted only for AI analysis
   - Not saved to external servers
   - Password protection for merchant access

## 🌐 Deployment

### Vercel Deployment (Recommended)

**Why Vercel?**
- ✅ Free hosting
- ✅ Secure API key storage
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Zero configuration

**Deployment Steps**:
1. Push code to GitHub
2. Import project in Vercel
3. Add environment variable: `DEEPSEEK_API_KEY`
4. Deploy automatically

**Configuration Files**:
- `vercel.json`: Deployment configuration (simplified, auto-detection)
- `package.json`: Node.js project info
- `api/deepseek.js`: Serverless function for API proxy

### Local Testing

```bash
# Start local server
cd Vendor
python3 -m http.server 8000

# Visit
http://localhost:8000/Vendor/business_report.html
```

## 🐛 Troubleshooting

### Problem 1: Restaurant List Empty
**Solution**: Ensure `restaurants.json` exists and format is correct
```bash
# Check file
ls ../data/restaurants.json

# Regenerate if needed
cd ../data
python3 convert_to_json.py
```

### Problem 2: AI Report Generation Fails
**Solution**:
- Check if API Key is configured correctly (in Vercel environment variables)
- Confirm network connection is normal
- Check browser console for error messages
- Verify serverless function is deployed

### Problem 3: Login Doesn't Work
**Solution**: 
- Password is `111` (three ones)
- Make sure a restaurant is selected first

### Problem 4: Styling Issues
**Solution**: Use modern browsers (Chrome, Firefox, Safari, Edge)

### Problem 5: CORS Errors (Local File Access)
**Solution**: 
- Use a local server (recommended)
- Or deploy to Vercel (best solution)

## 📞 Technical Support

If you encounter issues, check:
1. Browser console (F12) for error messages
2. Network tab to verify API calls
3. Verify `restaurants.json` file is complete
4. Check Vercel function logs (if deployed)

## 🚀 Future Enhancements

Could consider adding:
- 📊 More data visualization charts (Chart.js, D3.js)
- 📅 Calendar view
- 💾 Export PDF reports
- 📱 Mobile optimization
- 🔄 Real-time data integration
- 📧 Automatic email sending
- 🌍 Multi-restaurant comparison
- 📈 Historical trend analysis

## 🔗 Related Documentation

- Main README: `../README_EN.md`
- Features Guide: `../docs/FEATURES_EN.md`
- Bot System: `../bot_system/README_EN.md`
- Data Documentation: `../data/README_EN.md`

---

## 📊 System Architecture

```
Frontend (HTML/CSS/JS)
    ↓
    ├─→ Load restaurants.json (static data)
    ├─→ Generate mock sales data (client-side)
    └─→ Call /api/deepseek (serverless function)
            ↓
            Vercel Serverless Function
            ├─→ Retrieve DEEPSEEK_API_KEY from env
            ├─→ Proxy request to Deepseek API
            └─→ Return AI analysis
                    ↓
                    Display in browser
```

**Security Layer**:
- ✅ API Key: Stored in Vercel environment variables
- ✅ Proxy: `/api/deepseek.js` handles authentication
- ✅ Frontend: No sensitive information exposed

---

**Development Date**: October 2025  
**Use Case**: Restaurant business data analysis and report generation  
**Target Users**: Restaurant owners, managers, business analysts

**Version**: v2.0  
**Last Updated**: October 21, 2025

