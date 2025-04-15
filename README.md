# A-Mario 考勤机器人

## 🚀 Railway 部署步骤

1. 点击 Railway 的一键部署按钮
2. 设置以下环境变量：
   - BOT_TOKEN：你的 Telegram Bot Token
   - WEBHOOK_URL：你的 Railway 项目的 URL，结尾加 `/webhook`

3. 设置 webhook：

```bash
curl -F "url=https://your-app-name.up.railway.app/webhook" https://api.telegram.org/bot<BOT_TOKEN>/setWebhook
```
