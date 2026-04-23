import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

WELCOME = (
    "LIGA808 OFFICIAL\n\n"
    "Selamat datang di Liga808!\n\n"
    "Transaksi deposit QRIS proses hanya 1 detik\n"
    "Penarikan berapapun dibayar lunas tanpa ribet\n"
    "Sistem cepat, stabil dan pelayanan terbaik 24 jam\n\n"
    "Link Alternatif: https://cutt.ly/9tTxZXsX\n"
    "Group WhatsApp: https://chat.whatsapp.com/ESnPixSwuY472u9nYgic5i\n"
    "Live Chat 24 Jam: https://direct.lc.chat/17638827\n\n"
    "Bergabunglah sekarang dan rasakan pengalaman terbaik bersama LIGA808!"
)

def keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Link Alternatif", url="https://cutt.ly/9tTxZXsX"),
            InlineKeyboardButton("Group WhatsApp", url="https://chat.whatsapp.com/ESnPixSwuY472u9nYgic5i")
        ],
        [
            InlineKeyboardButton("Live Chat 24 Jam", url="https://direct.lc.chat/17638827"),
            InlineKeyboardButton("Daftar Sekarang", url="https://cutt.ly/9tTxZXsX")
        ]
    ])

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME,
        reply_markup=keyboard(),
        disable_web_page_preview=True
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", reply))
    app.add_handler(CommandHandler("help", reply))
    app.add_handler(CommandHandler("link", reply))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Liga808 Bot aktif!")
    app.run_polling()

if __name__ == "__main__":
    main()
