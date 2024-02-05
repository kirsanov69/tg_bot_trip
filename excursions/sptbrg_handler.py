from aiogram import types, F, Router
from excursions.menu_handlers import menu_state_manager as sptbrg_state_manager
import kb, text
from main1 import bot, dp
from aiogram.types import FSInputFile
import importlib
import logging
import tracemalloc
tracemalloc.start()



router = Router()
# menu_handlers = importlib.import_module('excursions.menu_handlers')
# sptbrg_state_manager = menu_handlers.state_manager


@router.callback_query(F.data == "bloody_cathedral")
async def bloody_cathedral_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="sptbg_tours")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Собору спаса на крови', reply_markup=inline_keyboard)
    await sptbrg_state_manager.set_state(callback.from_user.id, "bloody_cathedral")


@router.callback_query(F.data == "Avrora")
async def bloody_cathedral_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="sptbg_tours", trip_name="Avrora")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Авроре (эт крейсер такой, если не знали)))', reply_markup=inline_keyboard)
    await sptbrg_state_manager.set_state(callback.from_user.id, "Avrora")


@router.callback_query(F.data == "Hachapurnaya")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice(module_name="sptbg_tours", trip_name="Hachapurnaya")
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Прошвырнемся по дристательным местам', reply_markup=inline_keyboard)
    await sptbrg_state_manager.set_state(callback.from_user.id, "Hachapurnaya")


@router.callback_query(F.data == "back_sptbg_tours")
async def back_sptbg_handler(callback: types.CallbackQuery):
    inline_keyboard = await kb.sptbg_tours()
    await sptbrg_state_manager.set_previous_state(callback.from_user.id)

        # Добавляем логирование после установки предыдущего состояния
    logging.info(f'Back handler: User {callback.from_user.id} set to previous state: , {sptbrg_state_manager.storage}')


    await bot.send_message(callback.from_user.id, text.sptbg_tours, reply_markup=inline_keyboard)
