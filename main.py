import logging
import mysql.connector
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from io import BytesIO
from config import TOKEN


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot(token = TOKEN)

# Функция для обработки команды /get_video
def get_video(update: Update, context: CallbackContext) -> None:
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
        context.bot.send_video(chat_id=update.effective_chat.id, video=BytesIO(video_data))

    except Exception as e:
        logging.error(str(e))
        update.message.reply_text("Произошла ошибка при получении видео.")

    finally:
        cursor.close()
        connection.close()

# Функция для обработки команды /get_audio
def get_audio(update: Update, context: CallbackContext) -> None:
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
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=BytesIO(audio_data))

    except Exception as e:
        logging.error(str(e))
        update.message.reply_text("Произошла ошибка при получении аудио.")

    finally:
        cursor.close()
        connection.close()

def main() -> None:
    updater = Updater(bot = bot, use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд /get_video и /get_audio
    dispatcher.add_handler(CommandHandler("get_video", get_video))
    dispatcher.add_handler(CommandHandler("get_audio", get_audio))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
