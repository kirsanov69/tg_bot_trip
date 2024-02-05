from aiogram import types, F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from excursions.sptbrg_handler import sptbrg_state_manager as avrora_state_manager
import kb, text
from main1 import bot, dp
from aiogram.types import FSInputFile
import logging
import asyncio

router = Router()

import tracemalloc
# from geopy.distance import distance
# from geopy.distance import geodesic
tracemalloc.start()


@router.callback_query(F.data == "go_Avrora") #высылаем координаты точки назначения
async def send_coordinates(callback: CallbackQuery):
    await callback.answer()
    # Send coordinates to the user
    # latitude = 41.692171
    # longitude = 44.840479
    target_latitude = 45.692665
    target_longitude = 46.840692
    #function to open yandex maps
    # url= f"https://yandex.com/maps/?ll={longitude},{latitude}&z=15"
    # reply_markup = InlineKeyboardMarkup(inline_keyboard=[
    #     [InlineKeyboardButton(text="Go navigator", url=url)]
    # ])
    # await bot.send_message(callback.from_user.id, reply_markup=reply_markup, text="Click the button to open the navigation app")
    inline_keyboard = await kb.go_tour(trip_name="avrora_step_1")


    # function for sending location
    await bot.send_location(callback.from_user.id, target_latitude, target_longitude, reply_markup=inline_keyboard) # bot will open google maps with our coordinates

    await avrora_state_manager.set_state(callback.from_user.id, "go_to_avrora_step_1")

###################################################################################################
users_locations = {}  # Словарь для хранения местоположений пользователей
sent_videos = []  # Список для хранения отправленных видеофайлов
@router.callback_query(F.data == "go_avrora_step_1") #проверяем местоположение пользователя и отправляем видео
async def handle_go_avrora_step_1(callback: types.CallbackQuery):
    # Здесь вы можете обрабатывать коллбек, связанный с кнопкой "Go Avrora Step 1"
    await callback.answer("Вы нажали кнопку!")
    # Если нужно отправить местоположение, запросите его у пользователя
    button = [[types.KeyboardButton(text="Отправить местоположение", request_location=True)]]
    kb = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True, one_time_keyboard=True)

    await callback.message.answer("Пожалуйста, отправьте свое местоположение.", reply_markup=kb)
    user_latitude = callback.message.location.latitude
    user_longitude = callback.message.location.longitude
    logging.info(f"User {callback.from_user.id} location: {user_latitude}, {user_longitude}")
    print(user_latitude, user_longitude)
    if user_latitude == 41.692171  and user_longitude == 44.840479:
        video_file_path = "C:\\Users\\Pavel\\tg_bots\\tg_bot_trip\\video\\video_avrora_step_1.mp4"
        video_file = types.FSInputFile(video_file_path)
        await bot.send_video(callback.from_user.id, video_file)
        logging.info(f"User {callback.from_user.id} location: {user_latitude}, {user_longitude}")


@router.callback_query(F.data == "go_to_avrora_step_2") #высылаем координаты точки назначения
async def send_coordinates(callback: CallbackQuery):
    await callback.answer()
    # Send coordinates to the user
    latitude = 41.705724
    longitude = 44.788053
    inline_keyboard = await kb.go_tour(trip_name="avrora_step_2")

    # function for sending location
    await bot.send_location(callback.from_user.id, latitude, longitude, reply_markup=inline_keyboard) # bot will open google maps with our coordinates

    await avrora_state_manager.set_state(callback.from_user.id, "go_to_avrora_step_2")



@router.callback_query(F.data == "go_avrora_step_2") #проверяем местоположение пользователя и отправляем видео
async def track_user_locations_2(callback: types.CallbackQuery):

  while True:
      # логика проверки местоположения пользователя
    user_latitude_1 = callback.message.location.latitude
    user_longitude_1 = callback.message.location.longitude
    users_locations[callback.from_user.id] = {"latitude": user_latitude_1, "longitude": user_longitude_1}
    logging.info(f"User {callback.from_user.id} location: {user_latitude_1}, {user_longitude_1}")

    target_latitude = 41.705724
    target_longitude = 44.788053
    # target_location = (target_latitude, target_longitude)
    # user_location = (user_latitude_1, user_longitude_1)

    # Calculate the distance between user's location and target location
    # dist = geodesic(user_location, target_location).meters

    # if dist <= 20:
    if user_latitude_1 == target_latitude and user_longitude_1 == target_longitude:
      video_file_path = "C:\\Users\\Pavel\\tg_bots\\tg_bot_trip\\video\\video_avrora_step_1 copy.mp4"
      if video_file_path not in sent_videos:
        video_file = FSInputFile(video_file_path)
        inline_keyboard = await kb.next_step(trip_name="finish_avrora") #переход к следующему шагу

        await bot.send_video(callback.from_user.id, video_file, reply_markup=inline_keyboard)
        await avrora_state_manager.set_state(callback.from_user.id, "start_trip_avrora_step_1")  # Устанавливаем состояние в "avrora_step_2"

        sent_videos.append(video_file_path)  # Добавляем отправленный видеофайл в список
        logging.info(f"User {callback.from_user.id} sent video: {sent_videos}, user locations: {users_locations}")
  # Задержка между проверками местоположения
    await asyncio.sleep(60)  # Проверка раз в минуту


@router.callback_query(F.data == "go_to_finish_avrora")
async def finish_avrora(callback: CallbackQuery):
    await callback.answer()
    inline_keyboard = await kb.create_main_menu()
    await bot.send_message(callback.from_user.id, text=text.finish_avrora, reply_markup=inline_keyboard)
    # await msg.answer(text=text.finish_avrora, reply_markup=kb.exit_kb)
    await avrora_state_manager.set_state(callback.from_user.id, "menu")
