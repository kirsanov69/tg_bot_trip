from aiogram import types, F, Router
import kb
from main1 import bot, dp
from aiogram.types import FSInputFile
import text
from excursions.menu_handlers import menu_state_manager as kazan_state_manager
import logging
import importlib

router = Router()
menu_handlers = importlib.import_module('excursions.menu_handlers')
# kazan_state_manager = menu_handlers.state_manager



@router.callback_query(F.data == "Kazan_tour1")
async def kazan_tour1_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice()
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Казани №1', reply_markup=inline_keyboard)
    await kazan_state_manager.set_state(callback.from_user.id, "Kazan_tour1")



@router.callback_query(F.data == "Kazan_tour2")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice()
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Казани №2', reply_markup=inline_keyboard)
    await kazan_state_manager.set_state(callback.from_user.id, "Kazan_tour2")


@router.callback_query(F.data == "Kazan_tour3")
async def red_square_handler(callback: types.CallbackQuery):
    photo = FSInputFile('pictures/moscow_tour.jpg')
    inline_keyboard = await kb.make_choice()
    await bot.send_photo(callback.from_user.id, photo=photo, caption='Маршрут по Казани №3', reply_markup=inline_keyboard)
    await kazan_state_manager.set_state(callback.from_user.id, "Kazan_tour3")

# @router.callback_query(F.data == "back")
# async def back_handler(callback: types.CallbackQuery):
#     await callback.answer()
#     inline_keyboard = await kb.kazan_tours()
#     await bot.send_message(callback.from_user.id, text.kazan_tours, reply_markup=inline_keyboard)
#     await state_manager.set_previous_state(callback.from_user.id)
@router.callback_query(F.data == "back_kazan_handlers")
async def back_kazan_handler(callback: types.CallbackQuery):
    inline_keyboard = await kb.kazan_tours()
    await kazan_state_manager.set_previous_state(callback.from_user.id)
    # if success:
    #     await state_manager.set_state(callback.from_user.id, previous_state)

        # Добавляем логирование после установки предыдущего состояния
    logging.info(f'Back handler: User {callback.from_user.id} set to previous state: , {kazan_state_manager.storage}')


    await bot.send_message(callback.from_user.id, text.kazan_tours, reply_markup=inline_keyboard)
