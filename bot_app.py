from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token="451380299:AAEKNNeyRfYlPhkh0apvhk5kftI94lg-I9s")
dp = Dispatcher(bot, storage=storage)

key1 = 1