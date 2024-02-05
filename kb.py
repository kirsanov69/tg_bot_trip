from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove




start_btn = [
    [InlineKeyboardButton(text = "Choose the tour", callback_data="create_menu")]
]

async def create_main_menu():
    menu_btn = [
        [InlineKeyboardButton(text = "Moscow", callback_data="moscow")],
        [InlineKeyboardButton(text = "Saint Petersburg", callback_data="saint_petersburg")],
        [InlineKeyboardButton(text = "Kazan", callback_data="kazan")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=menu_btn)

start = InlineKeyboardMarkup(inline_keyboard=start_btn)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Exit")]], resize_keyboard=True)

async def moscow_tours():
    moscow_btn = [
        [InlineKeyboardButton(text = "Красная площадь", callback_data="red_square")],
        [InlineKeyboardButton(text = "Собор такой-то матери", callback_data="the_cathedral_of_smth_mother")],
        [InlineKeyboardButton(text = "Метро", callback_data="subway")],
        [InlineKeyboardButton(text = "Назад", callback_data="back_menu_handlers")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=moscow_btn)

async def sptbg_tours():
    sptbg_btn = [
        [InlineKeyboardButton(text = "Храм Спаса на крови", callback_data="bloody_cathedral")],
        [InlineKeyboardButton(text = "Аврора", callback_data="Avrora")],
        [InlineKeyboardButton(text = "Хачапурная", callback_data="Hachapurnaya")],
        [InlineKeyboardButton(text = "Назад", callback_data="back_menu_handlers")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=sptbg_btn)


async def kazan_tours():
    sptbg_btn = [
        [InlineKeyboardButton(text = "Экскурсия 1", callback_data="Kazan_tour1")],
        [InlineKeyboardButton(text = "Экскурсия 2", callback_data="Kazan_tour2")],
        [InlineKeyboardButton(text = "Экскурсия 3", callback_data="Kazan_tour3")],
        [InlineKeyboardButton(text = "Назад", callback_data="back_menu_handlers")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=sptbg_btn)


async def make_choice(module_name = "default", trip_name = "default"):
    back_btn = [
        [InlineKeyboardButton(text = "Назад", callback_data=f'back_{module_name}')],
        [InlineKeyboardButton(text = "Поехали!", callback_data=f"go_{trip_name}")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=back_btn)


async def go_tour(trip_name = "default"):
    go_navigator_button = [InlineKeyboardButton(text = "Нажмите здесь, чтобы поделиться геолокацией с ботом", callback_data=f"go_{trip_name}" )]

    return InlineKeyboardMarkup(inline_keyboard=[go_navigator_button])


async def next_step(trip_name = "default"):
    next_step_button = [InlineKeyboardButton(text = "Перейти к следующему шагу", callback_data=f"go_to_{trip_name}" )]

    return InlineKeyboardMarkup(inline_keyboard=[next_step_button])
