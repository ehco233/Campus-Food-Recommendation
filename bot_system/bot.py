"""
Telegram机器人主程序 - 智能餐厅推荐系统
"""

import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from database import search_restaurants, format_restaurant_data, detect_language
from llm_service import LLMService


class RecommendationBot:
    def __init__(self, telegram_token, deepseek_api_key):
        """
        初始化机器人
        """
        self.llm_service = LLMService(deepseek_api_key)
        self.application = Application.builder().token(telegram_token).build()
        
        # 注册处理器
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        处理 /start 命令
        """
        welcome_message = """👋 Welcome to the Smart Restaurant Recommendation Bot!

I can recommend suitable restaurants based on your needs.

🔍 How to use:
Just tell me what you want, for example:
- "I want something not spicy, budget 5 dollars"
- "Recommend halal food under 10 dollars"
- "What's at North Spine Plaza?"
- "Cheap Western food"

💡 Tips:
- You can specify budget, taste preferences, cuisine types
- I'll consider real-time queue times for recommendations
- Supports both English and Chinese queries

Type /help for more information."""
        
        await update.message.reply_text(welcome_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        处理 /help 命令
        """
        help_message = """📖 User Guide

🍽️ Example Queries:
1. "I want halal food, budget under 10"
2. "Recommend vegetarian options"
3. "What's at The Hive?"
4. "Cheap Western food with short queue"

✨ Features:
- Real-time restaurant information query
- Considers price, cuisine, queue time
- AI-generated personalized recommendations
- Supports Halal and Vegetarian filtering

❓ Having issues?
- Make sure to describe your needs clearly
- Feel free to ask multiple times to refine
- Supports both English and Chinese

Enjoy your meal! 🎉"""
        
        await update.message.reply_text(help_message)
    
    def clean_markdown(self, text):
        """
        清理Markdown格式符号
        """
        import re
        
        # 移除加粗符号 **text** 或 __text__
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        text = re.sub(r'__(.+?)__', r'\1', text)
        
        # 移除斜体符号 *text* 或 _text_
        text = re.sub(r'\*(.+?)\*', r'\1', text)
        text = re.sub(r'_(.+?)_', r'\1', text)
        
        # 移除标题符号 # ## ### 等
        text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
        
        # 移除行内代码 `code`
        text = re.sub(r'`(.+?)`', r'\1', text)
        
        # 移除链接 [text](url)
        text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
        
        # 移除代码块 ``` ```
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        
        # 移除多余的星号和井号
        text = text.replace('*', '').replace('#', '')
        
        return text.strip()
    
    def parse_user_query(self, query):
        """
        解析用户查询，提取结构化信息
        """
        query_lower = query.lower()
        
        # 提取预算
        max_price = None
        price_patterns = [
            r'(\d+)元以内',
            r'预算\s*(\d+)',
            r'(\d+)块以内',
            r'不超过\s*(\d+)',
            r'under\s*(\d+)',
            r'budget\s*(\d+)',
            r'within\s*(\d+)',
            r'(\d+)\s*dollars?',
            r'(\d+)\s*yuan',
        ]
        for pattern in price_patterns:
            match = re.search(pattern, query, re.IGNORECASE)
            if match:
                max_price = int(match.group(1))
                break
        
        # 检查是否要求不辣
        not_spicy = any(word in query_lower for word in 
                       ['不辣', '不要辣', '清淡', '微辣', 'not spicy', 'mild', 'light'])
        
        # 检查是否要求清真
        halal_only = any(word in query_lower for word in
                        ['清真', 'halal', 'muslim'])
        
        # 检查是否要求素食
        vegetarian_only = any(word in query_lower for word in
                             ['素食', '素菜', 'vegetarian', 'vegan'])
        
        # 提取菜系关键词
        keyword = None
        cuisines = ['川菜', '粤菜', '日', '韩', '面', '快餐', '清真', '西餐',
                   'sichuan', 'cantonese', 'japanese', 'korean', 'noodle', 
                   'fast', 'halal', 'western', 'chinese', 'thai', 'asian',
                   'vegetarian', 'beverages', 'coffee', 'tea']
        
        # 也搜索位置关键词
        locations = ['north spine', 'hive', 'canteen', 'plaza']
        
        for cuisine in cuisines:
            if cuisine in query_lower:
                keyword = cuisine
                break
        
        if not keyword:
            for location in locations:
                if location in query_lower:
                    keyword = location
                    break
        
        return max_price, not_spicy, keyword, halal_only, vegetarian_only
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        处理用户消息
        """
        user_query = update.message.text
        
        # 检测语言
        language = detect_language(user_query)
        
        # 发送"正在处理"的提示
        if language == 'zh':
            processing_msg = await update.message.reply_text("🔍 正在为您查找合适的餐厅...", parse_mode='Markdown')
        else:
            processing_msg = await update.message.reply_text("🔍 Searching for suitable restaurants...", parse_mode='Markdown')
        
        try:
            # 1. 解析用户查询
            max_price, not_spicy, keyword, halal_only, vegetarian_only = self.parse_user_query(user_query)
            
            # 2. 数据检索
            restaurants = search_restaurants(
                max_price=max_price,
                not_spicy=not_spicy,
                keyword=keyword,
                language=language,
                halal_only=halal_only,
                vegetarian_only=vegetarian_only
            )
            
            # 3. 格式化餐厅数据
            restaurant_data = format_restaurant_data(restaurants, language=language)
            
            # 4. 使用LLM生成推荐
            recommendation = self.llm_service.generate_recommendation(user_query, restaurant_data, language=language)
            
            # 5. 清理Markdown符号
            recommendation = self.clean_markdown(recommendation)
            
            # 6. 发送结果
            await processing_msg.edit_text(recommendation)
        
        except Exception as e:
            # 转义特殊字符以避免 Markdown 解析错误
            error_str = str(e).replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace('`', '\\`')
            
            if language == 'zh':
                error_message = f"❌ 处理请求时出错了：{error_str}\n\n请稍后重试或输入 /help 查看使用说明。"
            else:
                error_message = f"❌ Error processing request: {error_str}\n\nPlease try again later or type /help for usage instructions."
            
            try:
                await processing_msg.edit_text(error_message, parse_mode='Markdown')
            except:
                # 如果 Markdown 还是失败，用纯文本
                await processing_msg.edit_text(error_message)
    
    def run(self):
        """
        启动机器人
        """
        print("🤖 Bot starting...")
        print("✅ Bot is running and listening for messages...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """
    主函数
    """
    # 导入配置
    try:
        from config import TELEGRAM_BOT_TOKEN, DEEPSEEK_API_KEY
    except ImportError:
        print("❌ Error: config.py file not found!")
        print("Please make sure config.py exists with your API keys.")
        return
    
    # 检查配置
    if "your_" in TELEGRAM_BOT_TOKEN or "your_" in DEEPSEEK_API_KEY:
        print("❌ Error: Please fill in your real API keys in config.py!")
        return
    
    # 创建并启动机器人
    bot = RecommendationBot(TELEGRAM_BOT_TOKEN, DEEPSEEK_API_KEY)
    bot.run()


if __name__ == "__main__":
    main()

