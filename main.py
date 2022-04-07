from flask import Flask
from aiogram import executor, types
from bot_app import dp

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Пошёл нахер, не пиши сюда больше!')

if __name__ == '__main__':
    app.run(debug=True)
    executor.start_polling(dp, skip_updates=True)
