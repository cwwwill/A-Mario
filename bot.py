import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

main_menu = ReplyKeyboardMarkup([
    ["🏢 内勤打卡", "📱 外勤打卡"],
    ["🆕 新用户注册", "📊 查看打卡记录"],
    ["🔐 管理员操作"]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 欢迎使用 *A-Mario* 考勤系统\n\n请选择服务👇",
        reply_markup=main_menu,
        parse_mode='Markdown'
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        webhook_url=os.environ.get("WEBHOOK_URL")
    )
