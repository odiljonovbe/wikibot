import logging

import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5226278169:AAFJ05ztSsdZQPyBYScw88i2HU-BnAC5eZg'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    await message.reply(f'Assalomu Alaykum <b><a href="tg://user?id={message.forward_from}">{message.from_user.first_name}</a></b> !'
                        f"\n\n<b>Ushbu bot orqali Wikipediadan ma'lumotlarni tez va oson topishingiz mumkin!</b>"
                        f"\n\nO'zingiz uchun kerakli ma'lumot matinini yuboring:",
                        parse_mode="HTML")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(f'Hurmatli <b><a href="tg://user?id={message.forward_from}">{message.from_user.first_name}</a></b> !'
                        f"\n\n<b>Botga wikipediadan qidirmoqchi bo'lgan ma'lumot matinini lotin harflarida yuborasiz,agarda ma'lumot mavjud bo'sa bot sizga javob qaytaradi</b>"
                        f"\n\nAgar mavjud bo'lmasa yana harakat qilib ko'ring\n\nMurojat uchun👉 @odiljonovofficial",
                        parse_mode="HTML")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi☹")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)