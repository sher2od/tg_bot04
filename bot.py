import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start, handle_buyurtma, hand_contact,handle_location,orqaga,handle_phone,fallback_handler

# Tokenni olish
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN topilmadi!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & Filters.regex("^📦 Buyurtma berish$"), handle_buyurtma))
    dp.add_handler(MessageHandler(Filters.contact, hand_contact))
    dp.add_handler(MessageHandler(Filters.location, handle_location))
    dp.add_handler(MessageHandler(Filters.text("Orqaga"), orqaga))
    dp.add_handler(MessageHandler(Filters.text & Filters.regex("^(Iphone|Redmi|Samsung)$"), handle_phone))

    # Noto‘g‘ri matnlarga javob
    dp.add_handler(MessageHandler(Filters.text, fallback_handler))

    updater.start_polling()
    updater.idle()


    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
