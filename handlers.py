from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Mahsulot tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("📦 Buyurtma berish")]],
            resize_keyboard=True
        )
    )

def handle_buyurtma(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📱 Telefon raqamingizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("📞 Raqamni yuborish", request_contact=True)],
                [KeyboardButton("Orqaga")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def hand_contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_text(
        f"✅ Raqamingiz qabul qilindi: {contact.phone_number}",
        reply_markup=ReplyKeyboardRemove()
    )
    ask_location(update, context)

def ask_location(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📍 Iltimos, lokatsiyangizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("📍 Lokatsiyani yuborish", request_location=True)],
                [KeyboardButton("Orqaga")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def handle_location(update: Update, context: CallbackContext):
    update.message.reply_text(
        "✅ Lokatsiyangiz qabul qilindi!",
        reply_markup=ReplyKeyboardRemove()
    )
    ask_phone(update, context)

def ask_phone(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📱 Telefon turini tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Iphone"), KeyboardButton("Redmi"), KeyboardButton("Samsung")],
                [KeyboardButton("Orqaga")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def handle_phone(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Tanlovingiz uchun rahmat. Siz bilan tez orada bog'lanamiz.",
        reply_markup=ReplyKeyboardRemove()
    )



def fallback_handler(update: Update, context: CallbackContext):
    update.message.reply_text("⚠️ Iltimos, mavjud tugmalardan foydalaning.")




def orqaga(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Asosiy menyuga qaytdingiz.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("📦 Buyurtma berish")]],
            resize_keyboard=True
        )
    )

