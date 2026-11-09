import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

LINK_RESMI = "https://newserver.ink/kita-bisa/loginliga808/"
LIVE_CHAT = "https://text.at/caf87d43-cc6e-4e7b-a441-84efd48bc9f9"
BANNER_PATH = os.path.join("assets", "liga808-banner.png")

WELCOME = """<b>LIGA808 OFFICIAL</b>

Selamat datang di Liga808!

Transaksi deposit QRIS diproses hanya 1 detik.
Penarikan dibayar tuntas tanpa ribet.
Sistem cepat, stabil, dan pelayanan terbaik 24 jam.
Bonus Rollingan Mingguan 10%

Bergabunglah sekarang dan rasakan pengalaman terbaik bersama LIGA808!"""


def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 LINK RESMI LIGA808", url=LINK_RESMI)],
        [InlineKeyboardButton("💬 LIVE CHAT 24 JAM", url=LIVE_CHAT)],
    ])


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_message:
        return

    markup = keyboard()

    if os.path.isfile(BANNER_PATH):
        with open(BANNER_PATH, "rb") as banner:
            await update.effective_message.reply_photo(
                photo=banner,
                caption=WELCOME,
                parse_mode="HTML",
                reply_markup=markup,
            )
    else:
        logging.warning("Banner tidak ditemukan: %s", BANNER_PATH)
        await update.effective_message.reply_text(
            WELCOME,
            parse_mode="HTML",
            reply_markup=markup,
            disable_web_page_preview=True,
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler(["start", "help", "link"], reply))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    logging.info("Liga808 Bot aktif!")
    app.run_polling()


if __name__ == "__main__":
    main()
