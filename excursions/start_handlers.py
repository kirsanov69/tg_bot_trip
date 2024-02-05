# from aiogram import F, Router, types
# from aiogram.filters import Command
# from aiogram.types import Message
# from aiogram.types import CallbackQuery
# import kb
# import text
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from state_manager import StateManager
# from main1 import bot

# state_manager = StateManager()

# router = Router()

# # Создаем объект StateHistory
# # state_history = StateHistory()

# class Menu(StatesGroup):
#     start = State()
#     menu = State()

# class Tours(StatesGroup):
#     Moscow = State()
#     Saint_Petersburg = State()
#     Kazan = State()

#     @staticmethod
#     @router.callback_query(F.data == "moscow")
#     async def moscow_tours_handler(callback: CallbackQuery, state: FSMContext):
#         await callback.answer()

#         inline_keyboard = await kb.moscow_tours()

#         # Отправка нового сообщения с клавиатурой туров
#         await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
#         await state.set_state(Tours.Moscow)
#         # state_history.add_state(Tours.Moscow, "MoscowTours")



# @router.message(Command("start"))
# async def start_handler(msg: Message):
#     await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
#     await Menu.start.set()


# async def menu_handler(msg: Message, user_id: int, state: FSMContext):
#     inline_keyboard = await kb.menu()

#     await msg.answer(user_id, text.menu, reply_markup=inline_keyboard)
#     await state.set_state(Menu.menu)
#     # state_history.add_state(Menu.menu, "Menu")


# @router.callback_query(F.data == "tours_list")
# async def tours_handler(callback: CallbackQuery):
#     await callback.answer()

#     inline_keyboard = await kb.tours_list()

#     # Отправка нового сообщения с клавиатурой туров
#     await bot.send_message(callback.from_user.id, text.select_tour, reply_markup=inline_keyboard)


# # @router.callback_query(F.data == "moscow")
# # async def moscow_tours_handler(callback: CallbackQuery, state: FSMContext):
# #     await callback.answer()

# #     inline_keyboard = await kb.moscow_tours()

# #     # Отправка нового сообщения с клавиатурой туров
# #     await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
# #     await state.set_state(Tours.Moscow)

# @router.callback_query(F.data == "saint_petersburg")
# async def stpbg_tours_handler(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()

#     inline_keyboard = await kb.sptbg_tours()

#     # Отправка нового сообщения с клавиатурой туров
#     await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
#     await state.set_state(Tours.Moscow)

# @router.callback_query(F.data == "kazan")
# async def stpbg_tours_handler(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()

#     inline_keyboard = await kb.kazan_tours()

#     # Отправка нового сообщения с клавиатурой туров
#     await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
#     await state.set_state(Tours.Kazan)


# @router.callback_query(F.data == "back")
# async def go_back(callback: CallbackQuery, state: FSMContext):
#     success = await state_manager.set_previous_state(callback.from_user.id, state)
#     if success:
#         await callback.answer("Вы вернулись к предыдущему состоянию.")
#     else:
#         await callback.answer("Нет предыдущего состояния.")



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

# @router.callback_query(F.data == "moscow")
# async def moscow_tours_handler(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()

#     inline_keyboard = await kb.moscow_tours()

#     # Отправка нового сообщения с клавиатурой туров
#     await bot.send_message(callback.from_user.id, text.moscow_tours, reply_markup=inline_keyboard)
#     await state.set_state(Tours.Moscow)
