# 赵博凯的个人网站

[![GitHub stars](https://img.shields.io/github/stars/zhaobokai341/zhaobokai341.github.io)](https://github.com/zhaobokai341/zhaobokai341.github.io/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/zhaobokai341/zhaobokai341.github.io)](https://github.com/zhaobokai341/zhaobokai341.github.io/network)
[![GitHub issues](https://img.shields.io/github/issues/zhaobokai341/zhaobokai341.github.io)](https://github.com/zhaobokai341/zhaobokai341.github.io/issues)

## 项目简介

这是一个基于纯原生技术栈（HTML、CSS、JavaScript）开发的个人网站，用于展示个人作品、分享日常心得和提供实用工具。网站采用响应式设计，支持多主题切换，并集成了Markdown解析功能，为访问者提供良好的阅读体验。

🌐 [立即访问](https://zhaobokai341.github.io/verify.html)

## 主要功能

- 📝 **日记系统**：支持Markdown格式的日记内容展示与管理
- 🎨 **多主题切换**：提供暗色、亮色、彩虹和个性化等多种主题，满足不同用户的视觉偏好
- 🎯 **作品展示与下载**：展示个人开发的各类项目作品，并提供在线下载功能
- 🛠️ **实用工具集**：整合常用工具和资源链接，提供便捷的一站式访问
- 💬 **评论系统**：集成Giscus评论功能，支持用户互动
- 📱 **响应式设计**：自适应不同设备屏幕尺寸，提供一致的用户体验
- 📋 **更新日志**：详细记录网站的更新历史和变更内容
- 🔗 **外部资源链接**：提供丰富的外部资源和工具链接

## 技术特点

- 🔧 **原生技术栈**：采用纯`HTML, CSS和JavaScript`开发，无框架依赖，确保高性能和快速加载
- 📖 **Markdown解析**：使用`marked.js`解析引擎，支持丰富的Markdown语法，便于内容创作和阅读
- 🎭 **多主题动态切换**：支持实时切换多种视觉主题：
  - 🌙 暗色主题：适合夜间阅读，减少眼睛疲劳
  - ☀️ 亮色主题：清爽简洁，适合日常浏览
  - 🌈 彩虹主题：缤纷多彩，活泼生动
  - 🖼️ 赵\*\*主题：\*\*\*\*\*\*，知道为什么打"*"号吗，有点搞笑（bushi），提前告诉你们不是丧失了对主题的探索？😂😂😂
- 📂 **模块化结构**：清晰的目录组织和功能模块划分，便于维护和扩展
- 📊 **静态部署**：主要采用静态部署方式，评论功能通过Giscus后端支持
- 🚀 **简便部署**：主要功能仅需基本Web服务器环境，无需复杂的后端配置

## 使用指南

### 访问网站

1. 通过GitHub Pages直接访问：[https://zhaobokai341.github.io/verify.html](https://zhaobokai341.github.io/verify.html)
2. 进入并通过验证，验证页面我不告诉你验证什么
3. 在首页可以浏览各种功能区块和导航链接

### 切换主题

1. 在网页顶部找到主题切换选项
2. 选择喜欢的主题（暗色、亮色、彩虹或个性化）
3. 主题会立即应用偏好设置

### 浏览日记和作品

1. 点击导航菜单中的"日记"或"作品"链接
2. 在相应页面浏览内容列表
3. 点击具体项目查看详细内容

### 使用工具

1. 访问"工具"页面查看可用工具列表
2. 选择需要的工具点击进入
3. 按照工具页面的指引操作

## 项目结构

### zhaobokai341.github.io/
#### 根目录文件
- home.html - 网站首页
- my_diary.html - 日记主页面
- my_opus.html - 作品展示页面
- tool.html - 工具链接页面
- update.html - 更新历史页面
- notice.html - 公告页面
- question.html - 常见问题页面
- zhaobokai.html - 个人介绍页面
- verify.html - 网站验证页面
- favicon.ico - 网站图标
- robots.txt - 搜索引擎爬虫配置
- package.json - 项目配置文件
- README.md - 项目说明文档
- CONTRIBUTING.md - 贡献指南
- LICENSE - 许可证文件
- SECURITY.md - 安全政策

#### style/ - 样式文件目录
- beautify.css - 美化样式
- dark.css - 暗色主题
- white.css - 亮色主题
- rainbow.css - 彩虹主题
- zhaobokai.css - 赵博凯主题
- comments.css - 评论区样式
- css_select_options.css - CSS选择器样式

#### js/ - JavaScript文件目录
- main.js - 核心功能实现
- marked.js - Markdown解析引擎
- css_select.js - 主题切换功能
- diary_api.js - 日记API处理

#### diary/ - 日记系统目录
- content/ - Markdown格式日记内容
- media/ - 日记相关多媒体资源
- diary.html - 日记展示页面
- diary_title.html - 日记标题页面

#### opus/ - 作品展示目录
- 210.html, 211.html - 作品展示页面
- 21.zip, 22.zip - 作品下载文件
- 其他作品文件 - 各类作品资源

#### img/ - 图片资源目录
- my_photo.jpg - 个人照片
- my_photo2.jpg - 个人照片（比较搞笑）
- my_photo.cur - 自定义鼠标样式（没什么好讲的）
- my_qrcode.png - 网站二维码

#### json/ - JSON数据目录
- diary_json.json - 日记数据文件

## 联系方式

- 📧 网易邮箱：13935190240@163.com
- 📺 B站账号：[编程博凯](https://space.bilibili.com/1458747461)
- 🐱 Github：[zhaobokai341](https://github.com/zhaobokai341)

## 快速访问

扫描下方二维码，即可访问个人网站：

![个人网站二维码](img/my_qrcode.png)

🌐 网站链接[https://zhaobokai341.github.io/verify.html](https://zhaobokai341.github.io/verify.html)

---
球球点个Star⭐，谢谢啦！
