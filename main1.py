import logging
import asyncio
import os
import importlib
from aiogram import Bot, Dispatcher
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



if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
