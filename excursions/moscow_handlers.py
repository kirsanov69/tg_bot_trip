from aiogram import types, F, Router
import kb
from main1 import bot
from aiogram.types import FSInputFile
import text, logging
from excursions.menu_handlers import menu_state_manager as moscow_state_manager
import importlib


router = Router()
# menu_handlers = importlib.import_module('excursions.menu_handlers')
# moscow_state_manager = menu_handlers.state_manager


@router.callback_query(F.data == "red_square")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="moscow_tours")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Красной площади', reply_markup=inline_keyboard)
    await moscow_state_manager.set_state(callback.from_user.id, "red_square")



@router.callback_query(F.data == "the_cathedral_of_smth_mother")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="moscow_tours")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Собору такой-то растакой прям матери', reply_markup=inline_keyboard)
    await moscow_state_manager.set_state(callback.from_user.id, "the_cathedral_of_smth_mother")


@router.callback_query(F.data == "subway")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="moscow_tours")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут метро. Давно ли вы катались на метре?)))', reply_markup=inline_keyboard)
    await moscow_state_manager.set_state(callback.from_user.id, "subway")

@router.callback_query(F.data == "back_moscow_tours")
async def back_moscow_handler(callback: types.CallbackQuery):
    inline_keyboard = await kb.moscow_tours()
    await moscow_state_manager.set_previous_state(callback.from_user.id)

        # Добавляем логирование после установки предыдущего состояния
    # logging.info(f'Back handler: User {callback.from_user.id} set to previous state: , {moscow_state_manager.storage}')


    await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
