from aiogram import F, Router, types
from aiogram.types import CallbackQuery
import kb
import text
from main1 import bot
import logging
from excursions.start_handlers import state_manager as menu_state_manager


router = Router()


@router.callback_query(F.data == "moscow")
async def moscow_tours_handler(callback: CallbackQuery):

    await callback.answer()

    inline_keyboard = await kb.moscow_tours()

    # Отправка нового сообщения с клавиатурой туров
    await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
    await menu_state_manager.set_state(callback.from_user.id, 'moscow_tours')



@router.callback_query(F.data == "saint_petersburg")
async def stpbg_tours_handler(callback: CallbackQuery):
    await callback.answer()

    inline_keyboard = await kb.sptbg_tours()

    # Отправка нового сообщения с клавиатурой туров
    await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
    await menu_state_manager.set_state(callback.from_user.id, "saint_petersburg")

@router.callback_query(F.data == "kazan")
async def kazan_tours_handler(callback: CallbackQuery):
    await callback.answer()

    inline_keyboard = await kb.kazan_tours()

    # Отправка нового сообщения с клавиатурой туров
    await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
    await menu_state_manager.set_state(callback.from_user.id, "kazan")


@router.callback_query(F.data == "back_menu_handlers")
async def back_menu_handler(callback: types.CallbackQuery):

    inline_keyboard = await kb.create_main_menu()
    await menu_state_manager.set_previous_state(callback.from_user.id)
    # logging.info(f'Back handler: User {callback.from_user.id} set to previous state: , {menu_state_manager.storage}')

    await bot.send_message(callback.from_user.id, text.select_tour, reply_markup=inline_keyboard)
    # except Exception as e:
    #     logging.exception(f'Error in back_menu_handler: {e}')
    # logging.debug("Exiting back_menu_handler")
