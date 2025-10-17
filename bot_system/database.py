"""
餐厅数据库 - 从JSON文件读取
"""

import json
import random
import os


def load_restaurants():
    """
    从JSON文件加载餐厅数据
    """
    # 使用绝对路径，确保无论从哪个目录运行都能找到文件
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    json_file = os.path.join(project_root, 'data', 'restaurants.json')
    
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print(f"⚠️  找不到 {json_file}")
        print(f"   当前脚本位置: {current_dir}")
        print(f"   项目根目录: {project_root}")
        print(f"   请确保文件存在: {json_file}")
        return []


# 加载餐厅数据
RESTAURANTS = load_restaurants()


def detect_language(query):
    """
    检测查询语言（简单规则）
    """
    # 检查是否包含中文字符
    for char in query:
        if '\u4e00' <= char <= '\u9fff':
            return 'zh'
    return 'en'


def search_restaurants(max_price=None, not_spicy=None, keyword=None, language='en', halal_only=False, vegetarian_only=False):
    """
    根据条件搜索餐厅
    :param max_price: 最高价格
    :param not_spicy: 是否要求不辣
    :param keyword: 关键词（菜系、名称等）
    :param language: 语言 ('zh' 或 'en')
    :param halal_only: 只显示清真餐厅
    :param vegetarian_only: 只显示素食餐厅
    :return: 符合条件的餐厅列表
    """
    results = []
    
    for restaurant in RESTAURANTS:
        # Halal筛选
        if halal_only and not restaurant.get('halal', False):
            continue
        
        # 素食筛选
        if vegetarian_only and not restaurant.get('vegetarian', False):
            continue
        
        # 价格筛选
        if max_price is not None:
            avg_price = restaurant.get('avg_price', 15)
            if avg_price > max_price:
                continue
        
        # 辣度筛选（这个数据是模拟的，因为Excel里没有）
        if not_spicy and restaurant.get('spicy', False):
            continue
        
        # 关键词筛选
        if keyword:
            keyword_lower = keyword.lower()
            
            # 在名称、菜系、描述、位置中搜索
            search_in = [
                restaurant['name'].get(language, '').lower(),
                restaurant['cuisine'].get(language, '').lower(),
                restaurant['description'].get(language, '').lower(),
                restaurant.get('location', {}).get(language, '').lower() if isinstance(restaurant.get('location'), dict) else ''
            ]
            
            if not any(keyword_lower in text for text in search_in):
                continue
        
        # 添加实时排队时间（模拟）
        restaurant_copy = restaurant.copy()
        restaurant_copy["queue_time"] = random.randint(0, 30)
        results.append(restaurant_copy)
    
    # 如果结果太多，随机选择最多10个
    if len(results) > 10:
        results = random.sample(results, 10)
    
    return results


def format_restaurant_data(restaurants, language='en'):
    """
    格式化餐厅数据为文本（使用Markdown格式加粗关键信息）
    :param restaurants: 餐厅列表
    :param language: 语言 ('zh' 或 'en')
    """
    if not restaurants:
        if language == 'zh':
            return "没有找到符合条件的餐厅。"
        else:
            return "No restaurants found matching your criteria."
    
    if language == 'zh':
        formatted = "找到以下餐厅信息：\n\n"
        for i, r in enumerate(restaurants, 1):
            formatted += f"{i}. **{r['name']['zh']}**\n"
            
            # 位置（加粗）
            if 'location' in r and isinstance(r['location'], dict):
                location = r['location']['zh']
                if location != 'nan':
                    formatted += f"   📍 **位置**: **{location}**\n"
            
            formatted += f"   🍽️ 菜系: {r['cuisine']['zh']}\n"
            
            # 价格（加粗）
            formatted += f"   💰 **价格**: **${r['price_range']}** (平均: **${r.get('avg_price', 'N/A')}**)\n"
            
            if r.get('halal'):
                formatted += f"   ☪️ 清真: 是\n"
            if r.get('vegetarian'):
                formatted += f"   🥗 素食选项: 有\n"
            
            # 等待时长（加粗）
            formatted += f"   ⏰ **排队时间**: **约{r['queue_time']}分钟**\n"
            
            # 推荐菜品（加粗）
            formatted += f"   ⭐ **推荐菜品**: **{r['recommended_dishes']['zh']}**\n"
            formatted += f"   📝 简介: {r['description']['zh']}\n\n"
    else:
        formatted = "Found the following restaurants:\n\n"
        for i, r in enumerate(restaurants, 1):
            formatted += f"{i}. **{r['name']['en']}**\n"
            
            # 位置（加粗）
            if 'location' in r and isinstance(r['location'], dict):
                location = r['location']['en']
                if location != 'nan':
                    formatted += f"   📍 **Location**: **{location}**\n"
            
            formatted += f"   🍽️ Cuisine: {r['cuisine']['en']}\n"
            
            # 价格（加粗）
            formatted += f"   💰 **Price**: **${r['price_range']}** (Avg: **${r.get('avg_price', 'N/A')}**)\n"
            
            if r.get('halal'):
                formatted += f"   ☪️ Halal: Yes\n"
            if r.get('vegetarian'):
                formatted += f"   🥗 Vegetarian: Available\n"
            
            # 等待时长（加粗）
            formatted += f"   ⏰ **Queue Time**: **~{r['queue_time']} mins**\n"
            
            # 推荐菜品（加粗）
            formatted += f"   ⭐ **Recommended**: **{r['recommended_dishes']['en']}**\n"
            formatted += f"   📝 Info: {r['description']['en']}\n\n"
    
    return formatted

