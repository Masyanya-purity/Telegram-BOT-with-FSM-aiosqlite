import asyncio
import aiosqlite
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove

bot = Bot(token="")
dp = Dispatcher()

DB = "user_data.db"

class ups(StatesGroup):
    nickname = State()
    password = State()
    site = State()

class all(StatesGroup):
    main = State()
    over = State()

async def init_db_tables():
    async with aiosqlite.connect(DB) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS log (username TEXT, password INTEGER, site TEXT)")
        await db.commit()

@dp.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет я бот менеджер поролей!")
    await message.answer("Напиши мне логин: ")
    await state.set_state(ups.nickname)

@dp.message(ups.nickname)
async def nicknamek(message: types.Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    await message.answer(f"Отлично! {message.text} сохранен в базе данных")
    await message.answer("Напиши мне пароль:")
    await state.set_state(ups.password)

@dp.message(ups.password)
async def passwordek(message: types.Message, state: FSMContext):
    try:
        await state.update_data(password=message.text)
        await message.answer(f"Отлично! {message.text} сохранен в базе данных")
        await message.answer("Напиши мне сайт, пример: vk.com")
        await state.set_state(ups.site)

    except ValueError:
        await message.answer("Вводи цифры а не буквы!")


@dp.message(ups.site)
async def sitek(message: types.Message, state: FSMContext):
    await state.update_data(site=message.text)
    await message.answer(f"Отлично! {message.text} сохранен в базе данных")
    
  
    user_all = await state.get_data()
    username = user_all.get("nickname")
    password = user_all.get("password")
    site = user_all.get("site")

   
    await message.answer(
        f"👤 Твой никнейм: {username}\n"
        f"🔑 Твой пароль: {password}\n"
        f"🌐 Твой сайт: {site}\n\n"
        "Напиши слово **конец**, если ты удовлетворен результатом."
    )
    
    
    await state.set_state(all.main)


@dp.message(all.main)
async def alld(message: types.Message, state: FSMContext):

    if message.text.lower() in ["закончили", "закончить", "конец"]:
        
        await state.set_state(all.over)
        await over(message, state) 
    else:
        
        await message.answer("Ты чем то недоволен? увы пока ничего не поменять добавлю позже! Напиши слово конец.")

    

@dp.message(all.over)
async def over(message: types.Message, state: FSMContext):
    await message.answer("Сохраняю в базу данных...")
    user_all = await state.get_data()
    username = user_all.get("nickname")
    password = user_all.get("password")
    site = user_all.get("site")

    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT INTO log (username, password, site) VALUES (?, ?, ?)", (username, password, site))
        await db.commit()

    await message.answer("Все данные сохранены")
    await state.clear()

async def start_telegram_BOT():
    await init_db_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    await start_telegram_BOT()
