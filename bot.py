import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import F
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
TOKEN = os.getenv("6239580055:AAEukPjVCokbr__88Cjl_eXpAVQ5HvMCFIo")  # Corregido: Usar nombre estándar para la variable

# Inicialización del bot
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Configuración de logging mejorada
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Teclado principal mejorado
def main_keyboard():
    builder = ReplyKeyboardBuilder()
    buttons = [
        "Hola", "Ayuda", "Foto", "Audio",
        "Sticker", "Documento", "Ubicación",
        "Contacto", "Video"
    ]
    
    for button in buttons:
        builder.button(text=button)
    
    builder.adjust(2)  # 2 botones por fila
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Elige una opción..."
    )

# Manejadores de comandos
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    try:
        await message.answer(
            f"👋 ¡Hola, {hbold(message.from_user.first_name)}!\n\n"
            "Soy un bot de demostración. ¿En qué puedo ayudarte?",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error en start_handler: {e}")

@dp.message(F.text.lower() == "hola")
async def hello_handler(message: Message):
    await message.answer("¡Hola de nuevo! 😊 ¿Qué necesitas?")

@dp.message(F.text.lower() == "ayuda")
async def help_handler(message: Message):
    help_text = (
        "🆘 <b>Ayuda</b>\n\n"
        "Puedes interactuar conmigo usando estos comandos:\n"
        "- <b>Hola</b>: Saludo inicial\n"
        "- <b>Foto</b>: Te enviaré una imagen\n"
        "- <b>Audio</b>: Te enviaré un sonido\n"
        "- <b>Sticker</b>: Te enviaré un sticker\n"
        "- <b>Documento</b>: Te enviaré un archivo PDF\n"
        "- <b>Ubicación</b>: Te enviaré una ubicación\n"
        "- <b>Contacto</b>: Te enviaré un contacto\n"
        "- <b>Video</b>: Te enviaré un video corto"
    )
    await message.answer(help_text)

# Manejadores de contenido multimedia
@dp.message(F.text.lower() == "foto")
async def photo_handler(message: Message):
    try:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo="https://placekitten.com/400/300",
            caption="🐱 ¡Aquí tienes un lindo gatito!",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando foto: {e}")
        await message.answer("⚠️ No pude enviar la foto. Intenta más tarde.")

@dp.message(F.text.lower() == "audio")
async def audio_handler(message: Message):
    try:
        await bot.send_audio(
            chat_id=message.chat.id,
            audio="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            caption="🎵 Audio de ejemplo",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando audio: {e}")
        await message.answer("⚠️ No pude enviar el audio. Intenta más tarde.")

@dp.message(F.text.lower() == "sticker")
async def sticker_handler(message: Message):
    try:
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker="CAACAgIAAxkBAAEB0QJkZUSRAAGnZ0d6ZTujN6PvTeyx_gAC7AIAArVx2Uos37UEVXsEOi8E",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando sticker: {e}")
        await message.answer("⚠️ No pude enviar el sticker. Intenta más tarde.")

@dp.message(F.text.lower() == "documento")
async def document_handler(message: Message):
    try:
        await bot.send_document(
            chat_id=message.chat.id,
            document="https://file-examples.com/storage/fec0c01b3fd91c1e0f4b4bd/2017/10/file-sample_150kB.pdf",
            caption="📄 Documento PDF de ejemplo",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando documento: {e}")
        await message.answer("⚠️ No pude enviar el documento. Intenta más tarde.")

@dp.message(F.text.lower() == "ubicación")
async def location_handler(message: Message):
    try:
        await bot.send_location(
            chat_id=message.chat.id,
            latitude=19.4326,  # Ciudad de México
            longitude=-99.1332,
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando ubicación: {e}")
        await message.answer("⚠️ No pude enviar la ubicación. Intenta más tarde.")

@dp.message(F.text.lower() == "contacto")
async def contact_handler(message: Message):
    try:
        await bot.send_contact(
            chat_id=message.chat.id,
            phone_number="+525512345678",
            first_name="Ejemplo",
            last_name="Bot",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando contacto: {e}")
        await message.answer("⚠️ No pude enviar el contacto. Intenta más tarde.")

@dp.message(F.text.lower() == "video")
async def video_handler(message: Message):
    try:
        await bot.send_video(
            chat_id=message.chat.id,
            video="http://techslides.com/demos/sample-videos/small.mp4",
            caption="🎥 Video de ejemplo",
            reply_markup=main_keyboard()
        )
    except Exception as e:
        logger.error(f"Error enviando video: {e}")
        await message.answer("⚠️ No pude enviar el video. Intenta más tarde.")

# Manejador para mensajes no reconocidos
@dp.message()
async def unknown_handler(message: Message):
    await message.answer(
        "No entendí tu mensaje. Usa el teclado o escribe /start para comenzar.",
        reply_markup=main_keyboard()
    )

# Función principal
async def main():
    try:
        logger.info("Iniciando bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error en el bot: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())