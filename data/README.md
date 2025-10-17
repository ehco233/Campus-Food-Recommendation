# 📦 数据目录

存储项目的所有数据文件和数据处理工具。

---

## 📂 目录内容

```
data/
├── restaurants.json                      # 餐厅数据（主要数据文件）
├── AI Course Data Collection 2.xlsx      # 原始 Excel 数据
├── convert_to_json.py                    # Excel 转 JSON 工具
└── README.md                             # 本文件
```

---

## 📊 数据文件说明

### restaurants.json

**用途**: 所有系统的主要数据源

**内容**:
- 58家餐厅/档口
- 163个菜单项
- 多语言字段（中英文）

**数据结构**:
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
      "菜品1",
      "菜品2",
      "..."
    ]
  }
]
```

**文件大小**: 42KB  
**格式**: JSON (UTF-8)  
**编码**: Unicode

---

### AI Course Data Collection 2.xlsx

**用途**: 原始数据源

**包含**:
- Stall Name（档口名称）
- Canteen（所属食堂）
- Cuisine（菜系）
- Menu Item（菜品名称）
- Price（价格）

**注意**: 此文件为备份，实际使用 `restaurants.json`

---

### convert_to_json.py

**用途**: Excel 转 JSON 转换工具

**功能**:
- 读取 Excel 文件
- 按档口分组
- 计算价格范围和平均价格
- 生成多语言字段
- 处理缺失数据
- 输出 JSON 文件

**使用方法**:
```bash
cd data
python3 convert_to_json.py
```

**输出**: `restaurants.json`（覆盖现有文件）

---

## 🔄 更新数据流程

### 完整更新

1. **准备新数据**
   ```bash
   # 替换 Excel 文件
   cp "新数据.xlsx" "AI Course Data Collection 2.xlsx"
   ```

2. **运行转换**
   ```bash
   cd data
   python3 convert_to_json.py
   ```

3. **验证数据**
   ```bash
   # 检查生成的 JSON
   cat restaurants.json | jq length  # 查看餐厅数量
   ```

4. **重启系统**
   ```bash
   # Bot 会自动重新加载
   # 报告系统刷新页面即可
   ```

### 手动编辑

直接编辑 `restaurants.json` 后：
- Bot: 重启 `bot.py`
- 报告: 刷新浏览器

---

## 📊 数据统计

| 指标 | 数值 |
|------|------|
| 餐厅总数 | 58 |
| 菜单项目 | 163 |
| 价格范围 | $1 - $30 |
| 平均价格 | ~$10 |
| Halal 餐厅 | 部分 |
| 素食选项 | 部分 |
| 数据语言 | 中文 + 英文 |

---

## 🔍 数据字段说明

### 必需字段
- `id` - 唯一标识符
- `name` - 餐厅名称（多语言）
- `cuisine` - 菜系类型（多语言）
- `price_range` - 价格区间（字符串）
- `avg_price` - 平均价格（数字）

### 可选字段
- `location` - 位置（多语言）
- `halal` - 是否清真（布尔值）
- `vegetarian` - 是否有素食（布尔值）
- `spicy` - 是否辣（布尔值）
- `recommended_dishes` - 推荐菜品（多语言）
- `description` - 描述（多语言）
- `all_menus` - 所有菜单项（数组）

---

## 🛠️ 工具脚本

### convert_to_json.py 功能详解

**主要步骤**:
1. 读取 Excel 文件
2. 按 Stall Name 分组
3. 计算每个档口的：
   - 最低价格
   - 最高价格
   - 平均价格
4. 选择推荐菜品（前3个）
5. 生成多语言字段
6. 处理缺失值
7. 输出 JSON

**错误处理**:
- Excel 文件不存在 → 使用默认数据
- 数据格式错误 → 跳过并警告
- 价格无效 → 使用默认值

---

## 📞 数据问题排查

### 问题1: JSON 文件不存在
```bash
cd data
python3 convert_to_json.py
```

### 问题2: 数据格式错误
检查 JSON 格式：
```bash
cat restaurants.json | jq .
```

### 问题3: Bot 找不到数据
确认路径：
```bash
# 从 bot_system 目录
ls ../data/restaurants.json
```

### 问题4: 报告系统无法加载
确认路径：
```bash
# 从 Vendor 目录
ls ../data/restaurants.json
```

---

## 📝 注意事项

1. **不要手动修改 all_menus**，使用转换工具更新
2. **备份原始 Excel 文件**，以防数据丢失
3. **更新后测试**，确保两个系统都正常
4. **多语言一致性**，中英文应保持对应

---

## 🔗 相关文档

- 项目结构: `../docs/PROJECT_STRUCTURE.md`
- Bot 系统: `../bot_system/README.md`
- 报告系统: `../Vendor/README.md`

---

**数据版本**: v2.0  
**最后更新**: 2025年10月17日  
**数据来源**: AI Course Data Collection

