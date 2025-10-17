"""
LLM服务：与Deepseek API交互
"""

from openai import OpenAI


class LLMService:
    def __init__(self, api_key):
        """
        初始化LLM服务
        :param api_key: Deepseek API密钥
        """
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
    
    def generate_recommendation(self, user_query, restaurant_data, language='en'):
        """
        生成推荐结果
        :param user_query: 用户原始查询
        :param restaurant_data: 检索到的餐厅数据
        :param language: 语言 ('zh' 或 'en')
        :return: LLM生成的推荐文本
        """
        # 根据语言构建系统提示词
        if language == 'zh':
            system_prompt = """你是一个餐厅推荐助手。根据用户需求和餐厅信息，用口语化的一段话给出推荐。

要求：
1. 输出一段话（3-5句话），不要分点列表
2. 语气要像朋友聊天一样自然、轻松
3. 必须包含：餐厅名称、位置、推荐理由、推荐菜品、预计花费、排队情况
4. 对关键信息使用加粗（但不要用星号，直接说）
5. 信息要完整但不啰嗦，语言流畅自然

示例：
"推荐你去学生快餐，主要是便宜实惠，6-8块钱就能吃饱。他们家的红烧肉饭和番茄炒蛋都不错，份量挺足的。现在不用排队，直接过去就行。"

"粤式茶餐厅位于North Spine Plaza，清淡不辣刚好符合你的要求。可以试试他们的虾饺和肠粉，人均15块左右。现在排队大概10分钟，还可以接受。"
"""
            user_message = f"""用户需求: {user_query}

检索到的餐厅信息:
{restaurant_data}

请根据以上信息，为用户提供个性化的餐厅推荐。用中文回复，不要使用Markdown格式。"""
        else:
            system_prompt = """You are a restaurant recommendation assistant. Based on user needs and restaurant information, provide recommendations in a casual, conversational paragraph in English.

Requirements:
1. Output one paragraph (3-5 sentences), no bullet points or lists
2. Tone should be natural and friendly, like chatting with a friend
3. Must include: restaurant name, location, reason for recommendation, suggested dishes, estimated cost, queue time
4. Keep it complete but concise, fluent and natural
5. Do NOT use Markdown formatting (no asterisks, brackets, etc.)

Examples:
"I'd recommend the Student Cafeteria - it's super affordable and you can get full for just 6-8 dollars. Their braised pork rice and tomato scrambled eggs are pretty good, and the portions are generous. No queue right now, you can head straight there."

"The Cantonese Tea House at North Spine Plaza would be perfect for you since it's light and not spicy, just what you asked for. Try their shrimp dumplings or rice noodle rolls, around 15 dollars per person. There's about a 10-minute wait right now, which is reasonable."
"""
            user_message = f"""User request: {user_query}

Retrieved restaurant information:
{restaurant_data}

Please provide a personalized restaurant recommendation based on the above information. Respond in English and do NOT use Markdown formatting."""

        # 调用API
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            if language == 'zh':
                return f"抱歉，生成推荐时出错了：{str(e)}"
            else:
                return f"Sorry, recommendation generation failed: {str(e)}"
