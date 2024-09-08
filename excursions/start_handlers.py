


from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery
import kb
import text
from aiogram.fsm.context import FSMContext
from state_manager import StateManager
from main1 import bot
import logging
state_manager = StateManager()

router = Router()



# Создаем объект StateHistory
# state_history = StateHistory()




@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.start)
    await state_manager.reset_state(msg.from_user.id)


async def menu_handler(msg: Message, user_id: int):
    inline_keyboard = await kb.create_menu()

    await msg.answer(user_id, text.menu, reply_markup=inline_keyboard)
    await state_manager.set_state('menu')
    # state_history.add_state(Menu.menu, "Menu")


@router.callback_query(F.data == "create_menu")
async def tours_handler(callback: CallbackQuery):
    await callback.answer()

    inline_keyboard = await kb.create_main_menu()

    # Отправка нового сообщения с клавиатурой туров
    await bot.send_message(callback.from_user.id, text.select_tour, reply_markup=inline_keyboard)
    await state_manager.set_state(callback.from_user.id, "create_menu")


#     inline_keyboard = await kb.moscow_tours()

#     # Отправка нового сообщения с клавиатурой туров
#     await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
#     await state.set_state(Tours.Moscow)
