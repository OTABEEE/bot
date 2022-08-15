import logging

from aiogram import Bot, Dispatcher, executor, types
from config import token
from aiogram.dispatcher import FSMContext

from translate import Translator

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(
        text="Xush kelibsz"
    )

@dp.message_handler(commands=["Yordam"])
async def help_command(message: types.Message):
    await message.answer(
        text="Bizning botda hali kamandalar mavjud emas"
    )

@dp.message_handler(commands=['click'])
async def cmd_start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # proxy = FSMContextProxy(state); await proxy.load()
        proxy.setdefault('counter', 0)
        proxy['counter'] += 1
        return await message.reply(f"Counter: {proxy['counter']}")




tugmalar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

tugma1 = types.KeyboardButton("Uzbek ga 🇺🇿")
tugma2 = types.KeyboardButton("English ga 🇺🇸")
tugma3 = types.KeyboardButton("Russian ga 🇷🇺")
tugma4 = types.KeyboardButton("Turkchaga ga 🇹🇷")
tugmalar.add(tugma1,tugma2,tugma3,tugma4)

repl = types.ForceReply(selective=False)


if message.text == "Uzbek ga 🇺🇿":
    bot.reply_to(message, "Uzbek tiliga tarjima qilish uchun matnni yuboring", reply_markup=repl)
elif message.text == "English ga 🇺🇸":
    bot.reply_to(message, "Ingliz tiliga tarjima qilish uchun matnni yuboring", reply_markup=repl)
elif message.text == "Turkchaga ga 🇹🇷":
    bot.reply_to(message, "Turk tiliga tarjima qilish uchun matnni yuboring", reply_markup=repl)
elif message.text == "Russian ga 🇷🇺":
    bot.reply_to(message, "Rus tiliga tarjima qilish uchun matnni yuboring", reply_markup=repl)
elif message.reply_to_message.text == "Uzbek tiliga tarjima qilish uchun matnni yuboring":
    translator = Translator(to_lang='uz')
    translation = translator.translate(message.text)
    bot.reply_to(message, translation, reply_markup=tugmalar)

elif message.reply_to_message.text == "Rus tiliga tarjima qilish uchun matnni yuboring":

    translator = Translator(to_lang='ru', from_lang="uz")
    translation = translator.translate(message.text)
    bot.reply_to(message, translation, reply_markup=tugmalar)
elif message.reply_to_message.text == "Turk tiliga tarjima qilish uchun matnni yuboring":

    translator = Translator(to_lang='tr', from_lang="uz")
    translation = translator.translate(message.text)
    bot.reply_to(message, translation, reply_markup=tugmalar)

elif message.reply_to_message.text == "Ingliz tiliga tarjima qilish uchun matnni yuboring":

    translator = Translator(to_lang='EN', from_lang='uz')
    translation = translator.translate(message.text)
    bot.reply_to(message, translation, reply_markup=tugmalar)
elif message.reply_to_message.text == "Ingliz tiliga tarjima qilish uchun matnni yuboring":

    translator = Translator(to_lang='Tr')
    translation = translator.translate(message.text)
    bot.reply_to(message, translation, reply_markup=tugmalar)

else:
    bot.reply_to(message, "Xatolik yuzaga keldi")

bot.polling()

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
