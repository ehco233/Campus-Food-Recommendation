# ✅ 部署检查清单

在提交到 Git 和部署之前，请按照此清单检查。

---

## 📋 提交前检查

### 1. 敏感信息检查 ⚠️

- [ ] **检查 config.py 是否被忽略**
  ```bash
  git status | grep config.py
  # 应该不显示 config.py（被 .gitignore 忽略）
  ```

- [ ] **确认 .gitignore 存在**
  ```bash
  cat .gitignore
  # 应该包含 config.py
  ```

- [ ] **搜索代码中的 API Key**
  ```bash
  grep -r "sk-" --exclude-dir=.git --exclude="*.md" .
  # 确认没有硬编码的 API Key
  ```

### 2. 代码完整性检查

- [ ] **Bot 系统文件**
  ```bash
  ls bot_system/
  # 应该有: bot.py, database.py, llm_service.py, config.py, START_BOT.sh
  ```

- [ ] **数据文件**
  ```bash
  ls data/
  # 应该有: restaurants.json, convert_to_json.py, *.xlsx
  ```

- [ ] **商家报告**
  ```bash
  ls Vendor/
  # 应该有: business_report.html, start_report_server.sh
  ```

- [ ] **API 文件**
  ```bash
  ls api/
  # 应该有: deepseek.js
  ```

- [ ] **文档文件**
  ```bash
  ls docs/
  # 应该有: FEATURES.md, FEATURES_EN.md, README.md
  ```

### 3. 路径引用检查

- [ ] **Bot 数据路径**
  ```bash
  grep "restaurants.json" bot_system/database.py
  # 应该显示: ../data/restaurants.json
  ```

- [ ] **报告系统数据路径**
  ```bash
  grep "restaurants.json" Vendor/business_report.html
  # 应该显示: ../data/restaurants.json
  ```

### 4. 配置文件检查

- [ ] **requirements.txt 存在**
  ```bash
  cat requirements.txt
  ```

- [ ] **vercel.json 配置正确**
  ```bash
  cat vercel.json
  ```

### 5. 测试功能（可选）

- [ ] **测试 Bot（本地）**
  ```bash
  cd bot_system && python3 bot.py
  # Ctrl+C 停止
  ```

- [ ] **测试报告系统（本地）**
  ```bash
  cd Vendor && python3 -m http.server 8000
  # 访问 http://localhost:8000/Vendor/business_report.html
  # Ctrl+C 停止
  ```

---

## 🚀 Git 提交步骤

### Step 1: 初始化 Git（如果还没有）

```bash
cd /Users/caro/Mio/PhD/GP8000

# 检查是否已初始化
git status

# 如果未初始化，运行：
git init
```

### Step 2: 添加远程仓库（如果还没有）

```bash
# 方法1: 创建新仓库后添加
git remote add origin https://github.com/你的用户名/GP8000.git

# 方法2: 如果已有仓库，检查
git remote -v
```

### Step 3: 查看待提交文件

```bash
git status
```

**重要**: 确认 `config.py` 没有在列表中！

### Step 4: 添加所有文件

```bash
# 添加所有文件（.gitignore 会自动忽略敏感文件）
git add .

# 再次确认
git status
```

### Step 5: 提交

```bash
git commit -m "feat: restructure project with secure deployment setup

- Organize files into functional directories (docs, bot_system, data, Vendor, api)
- Add Vercel serverless functions to hide API keys
- Update all file paths for new structure
- Add comprehensive documentation
- Prepare for secure cloud deployment"
```

### Step 6: 推送到 GitHub

```bash
# 首次推送（创建 main 分支）
git branch -M main
git push -u origin main

# 后续推送
git push
```

---

## 🌐 Vercel 部署步骤

### Step 1: 注册/登录 Vercel

1. 访问 https://vercel.com/signup
2. 选择 "Continue with GitHub"
3. 授权 Vercel 访问你的 GitHub

### Step 2: 导入项目

1. 在 Vercel Dashboard，点击 **"Add New Project"**
2. 选择 **"Import Git Repository"**
3. 找到并选择 **"GP8000"** 仓库
4. 点击 **"Import"**

### Step 3: 配置项目

**Framework Preset**: 选择 "Other" 或 "Static"

**Root Directory**: 保持 `./`（项目根目录）

**Build Command**: 留空

**Output Directory**: 留空

点击 **"Deploy"** 前，先设置环境变量（重要！）

### Step 4: 设置环境变量 ⚠️

在部署前，点击 **"Environment Variables"**：

```
Name:  DEEPSEEK_API_KEY
Value: sk-0d8c2aa28a154314a87276b28cc3ebeb
Environment: Production (选中)
```

点击 **"Add"**

### Step 5: 部署

点击 **"Deploy"** 按钮

等待 1-2 分钟，Vercel 会：
- ✅ 从 GitHub 拉取代码
- ✅ 构建 Serverless Functions
- ✅ 部署到全球 CDN
- ✅ 生成访问 URL

### Step 6: 获取 URL

部署成功后，你会得到：

```
https://gp8000-你的用户名.vercel.app
```

### Step 7: 测试部署

访问：
```
https://your-project.vercel.app/Vendor/business_report.html
```

测试：
1. ✅ 页面加载正常
2. ✅ 餐厅列表显示
3. ✅ 登录功能正常（密码：111）
4. ✅ 生成报告功能正常
5. ✅ AI 分析能够生成

---

## 🔒 安全验证

部署后进行安全检查：

### 1. 检查源代码

```bash
# 在浏览器中查看页面源代码 (Ctrl+U)
# 搜索 "sk-" 
# 应该找不到 API Key！
```

### 2. 检查 Network 请求

```bash
# F12 打开开发者工具
# Network 标签
# 生成报告时，应该只看到：
# - /api/deepseek (你自己的 API)
# - 没有直接调用 api.deepseek.com
```

### 3. 检查 GitHub 仓库

```bash
# 访问你的 GitHub 仓库
# 搜索 "sk-"
# 应该找不到 API Key！
```

---

## 🎯 后续更新流程

当你修改代码后：

```bash
# 1. 提交更改
git add .
git commit -m "描述你的更改"
git push

# 2. Vercel 自动部署
# 无需任何操作，Vercel 会自动检测并重新部署！
# 查看部署状态：https://vercel.com/dashboard
```

---

## 🐛 常见问题

### Q: config.py 被提交了怎么办？

```bash
# 1. 从 Git 历史中删除
git rm --cached bot_system/config.py

# 2. 确保 .gitignore 包含 config.py
echo "bot_system/config.py" >> .gitignore

# 3. 提交
git commit -m "Remove sensitive config file"
git push

# 4. 立即更换 API Key！
```

### Q: Vercel 部署失败？

1. 检查 vercel.json 格式是否正确
2. 确认 api/deepseek.js 没有语法错误
3. 查看 Vercel 部署日志
4. 确认环境变量 DEEPSEEK_API_KEY 已设置

### Q: AI 报告生成失败？

1. 检查 Vercel 环境变量是否设置
2. 查看浏览器 Console 是否有错误
3. 测试 API endpoint: `https://your-project.vercel.app/api/deepseek`

### Q: 数据文件找不到？

1. 确认 restaurants.json 在 data/ 目录
2. 检查路径是否为 `../data/restaurants.json`
3. 确认 Git 已提交 data/restaurants.json

---

## 📞 需要帮助？

- Vercel 文档: https://vercel.com/docs
- GitHub 文档: https://docs.github.com
- 项目文档: `docs/QUICK_DEPLOY.md`

---

## ✅ 最终检查清单

部署完成后：

- [ ] GitHub 仓库可访问
- [ ] Vercel 项目已部署
- [ ] 网站 URL 可访问
- [ ] 商家报告功能正常
- [ ] AI 分析能够生成
- [ ] 源代码中无 API Key
- [ ] 环境变量已设置
- [ ] .gitignore 保护 config.py

---

**准备就绪？开始部署！** 🚀

按照上面的步骤，你将在 **10 分钟内**完成安全部署！

