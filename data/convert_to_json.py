"""
将Excel文件转换为JSON餐厅数据
"""

import pandas as pd
import json
import random

def excel_to_json():
    """
    读取Excel文件并转换为JSON格式
    """
    try:
        # 读取Excel文件
        df = pd.read_excel('AI Course Data Collection 2.xlsx')
        
        print(f"✅ Successfully read Excel file: {len(df)} rows")
        print(f"Columns: {df.columns.tolist()}\n")
        
        # 按照Stall分组合并菜单
        stalls = {}
        current_canteen = None
        
        for idx, row in df.iterrows():
            canteen = row.get('Canteen/Food Court')
            stall = row.get('Stall')
            
            # 处理合并的单元格
            if pd.notna(canteen):
                current_canteen = str(canteen).strip()
            
            if pd.isna(stall) or str(stall).strip() == '':
                continue
                
            stall = str(stall).strip()
            
            # 创建唯一标识符
            key = f"{current_canteen}_{stall}"
            
            if key not in stalls:
                stalls[key] = {
                    'canteen': current_canteen,
                    'stall': stall,
                    'categories': str(row.get('Categories', 'Mixed')).strip() if pd.notna(row.get('Categories')) else 'Mixed',
                    'halal': bool(row.get('Halal', False)) if pd.notna(row.get('Halal')) else False,
                    'vegetarian': bool(row.get('Vegeterian Option', False)) if pd.notna(row.get('Vegeterian Option')) else False,
                    'menus': [],
                    'prices': []
                }
            
            # 添加菜单和价格
            menu = row.get('Menu')
            price = row.get('Price')
            
            if pd.notna(menu):
                menu_str = str(menu).strip()
                if menu_str:
                    stalls[key]['menus'].append(menu_str)
                    try:
                        stalls[key]['prices'].append(float(price))
                    except:
                        stalls[key]['prices'].append(10.0)
        
        # 转换为餐厅列表
        restaurants = []
        
        for key, data in stalls.items():
            if not data['prices']:
                continue
                
            min_price = min(data['prices'])
            max_price = max(data['prices'])
            avg_price = sum(data['prices']) / len(data['prices'])
            
            # 选择推荐菜品（价格适中的3个）
            menu_price_pairs = list(zip(data['menus'], data['prices']))
            menu_price_pairs.sort(key=lambda x: x[1])
            recommended = [m for m, p in menu_price_pairs[:3]]
            
            restaurant = {
                'name': {
                    'zh': data['stall'],
                    'en': data['stall']
                },
                'location': {
                    'zh': data['canteen'],
                    'en': data['canteen']
                },
                'cuisine': {
                    'zh': data['categories'],
                    'en': data['categories']
                },
                'price_range': f"{int(min_price)}-{int(max_price)}",
                'avg_price': round(avg_price, 1),
                'spicy': random.choice([True, False]),
                'halal': data['halal'],
                'vegetarian': data['vegetarian'],
                'description': {
                    'zh': f"{data['categories']}，位于{data['canteen']}",
                    'en': f"{data['categories']}, located at {data['canteen']}"
                },
                'recommended_dishes': {
                    'zh': ', '.join(recommended),
                    'en': ', '.join(recommended)
                },
                'all_menus': data['menus']
            }
            
            restaurants.append(restaurant)
        
        # 保存为JSON
        with open('restaurants.json', 'w', encoding='utf-8') as f:  # 输出到当前目录
            json.dump(restaurants, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully converted {len(restaurants)} restaurants to restaurants.json")
        print(f"\nSample restaurants:")
        for i, r in enumerate(restaurants[:3], 1):
            print(f"{i}. {r['name']['en']} at {r['location']['en']}")
            print(f"   Categories: {r['cuisine']['en']}")
            print(f"   Price: ${r['price_range']} (Avg: ${r['avg_price']})")
            print(f"   Menus: {len(r['all_menus'])} items")
            print()
        
        return restaurants
        
    except Exception as e:
        print(f"❌ Conversion failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("🔄 Converting Excel to JSON...\n")
    result = excel_to_json()
    if result:
        print("✅ Conversion completed successfully!")
        print(f"📁 File saved: restaurants.json")
    else:
        print("❌ Conversion failed!")

