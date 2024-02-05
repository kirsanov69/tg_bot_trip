# import logging
# import asyncio
# import os
# import importlib

# import sys
# import mysql.connector
# from aiogram import Bot, Dispatcher
# from aiogram.enums import ParseMode
# from aiogram.fsm.storage.memory import MemoryStorage

# from config import TOKEN

# # Настройка логирования
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# bot = Bot(token=TOKEN)
# dp = Dispatcher()



# async def main():
#     bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
#     dp = Dispatcher(storage=MemoryStorage())

#     # Путь к каталогу с модулями обработчиков экскурсий
#     excursions_dir = 'excursions'

#     # Динамический поиск и импорт модулей
#     for file_name in os.listdir(excursions_dir):
#         if file_name.endswith('.py') and not file_name.startswith('_'):
#             module_name = file_name[:-3]  # Удаление расширения .py
#             module_path = f'{excursions_dir}.{module_name}'
#             module = importlib.import_module(module_path)
#             dp.include_router(module.router)

#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

# if __name__ == "__main__":
#     import asyncio
#     loop = asyncio.get_event_loop()
#     try:
#         loop.create_task(dp.start_polling())
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         loop.close()


# if __name__ == '__main__':
#     import asyncio
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

'''
@dp.message_handler(commands=['get_video'])
async def get_video(message: types.Message):
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()

        # Запрос на получение видео из базы данных
        query = "SELECT video_data FROM video_table WHERE video_id = %s"
        video_id = (1,)  # пример идентификатора видео; замени на фактический идентификатор
        cursor.execute(query, video_id)
        video_data = cursor.fetchone()[0]

        # Отправка видео пользователю в Telegram
        video_stream = BytesIO(video_data)
        await bot.send_video(message.chat.id, video_stream)

    except Exception as e:
        logging.error(str(e))
        await message.answer("Произошла ошибка при получении видео.")

    finally:
        cursor.close()
        connection.close()

# Функция для обработки команды /get_audio
@dp.message_handler(commands=['get_audio'])
async def get_audio(message: types.Message):
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()

        # Запрос на получение аудио из базы данных
        query = "SELECT audio_data FROM audio_table WHERE audio_id = %s"
        audio_id = (1,)  # пример идентификатора аудио; замени на фактический идентификатор
        cursor.execute(query, audio_id)
        audio_data = cursor.fetchone()[0]

        # Отправка аудио пользователю в Telegram
        audio_stream = BytesIO(audio_data)
        await bot.send_audio(message.chat.id, audio_stream)

    except Exception as e:
        logging.error(str(e))
        await message.answer("Произошла ошибка при получении аудио.")

    finally:
        cursor.close()
        connection.close()
'''

# if __name__ == '__main__':
#     aiogram.start_polling(dp)

# async def main() -> None:
#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     # And the run events dispatching
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     asyncio.run(main())



import logging
import asyncio
import os
import importlib
import sys
import mysql.connector
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from state_manager import StateManager
from config import TOKEN

# Настройка логирования
logging.basicConfig(filename = 'tours_app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher()
# Menu.dp = dp


async def main():
    # Путь к каталогу с модулями обработчиков экскурсий
    excursions_dir = 'excursions'
    # Создание экземпляра StateManager
    your_state_manager_instance = StateManager()

    # Динамический поиск и импорт модулей
    for file_name in os.listdir(excursions_dir):
        if file_name.endswith('.py') and not file_name.startswith('_'):
            module_name = file_name[:-3]  # Удаление расширения .py
            module_path = f'{excursions_dir}.{module_name}'
            module = importlib.import_module(module_path)
            dp.include_router(module.router)
            # Регистрация обработчиков состояний

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr) and hasattr(attr, '__router_state__'):
                    dp.register_callback_query_handler(
                        attr,
                        state_manager=your_state_manager_instance
        )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

# async def main():

#     # Путь к каталогу с модулями обработчиков экскурсий
#     excursions_dir = 'excursions'

#     # Динамический поиск и импорт модулей
#     for file_name in os.listdir(excursions_dir):
#         if file_name.endswith('.py') and not file_name.startswith('_'):
#             module_name = file_name[:-3]  # Удаление расширения .py
#             module_path = f'{excursions_dir}.{module_name}'
#             module = importlib.import_module(module_path)
#             dp.include_router(module.router)

#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

# if __name__ == "__main__":
#     import asyncio
#     loop = asyncio.get_event_loop()
#     try:
#         loop.create_task(dp.start_polling())
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     finally:
        # loop.close()


# if __name__ == '__main__':
#     import asyncio
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

'''

@dp.message_handler(commands=['get_video'])
async def get_video(message: types.Message):
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()

        # Запрос на получение видео из базы данных
        query = "SELECT video_data FROM video_table WHERE video_id = %s"
        video_id = (1,)  # пример идентификатора видео; замени на фактический идентификатор
        cursor.execute(query, video_id)
        video_data = cursor.fetchone()[0]

        # Отправка видео пользователю в Telegram
        video_stream = BytesIO(video_data)
        await bot.send_video(message.chat.id, video_stream)

    except Exception as e:
        logging.error(str(e))
        await message.answer("Произошла ошибка при получении видео.")

    finally:
        cursor.close()
        connection.close()

# Функция для обработки команды /get_audio
@dp.message_handler(commands=['get_audio'])
async def get_audio(message: types.Message):
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()

        # Запрос на получение аудио из базы данных
        query = "SELECT audio_data FROM audio_table WHERE audio_id = %s"
        audio_id = (1,)  # пример идентификатора аудио; замени на фактический идентификатор
        cursor.execute(query, audio_id)
        audio_data = cursor.fetchone()[0]

        # Отправка аудио пользователю в Telegram
        audio_stream = BytesIO(audio_data)
        await bot.send_audio(message.chat.id, audio_stream)

    except Exception as e:
        logging.error(str(e))
        await message.answer("Произошла ошибка при получении аудио.")

    finally:
        cursor.close()
        connection.close()
'''



# if __name__ == '__main__':
#     dp.start_polling(dp)

# async def main() -> None:
#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     # And the run events dispatching
#     await dp.start_polling(bot)



if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
