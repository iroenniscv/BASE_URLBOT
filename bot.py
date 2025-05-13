#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Bot simple con Pyrogram - Desplegado en Koyeb

from pyrogram import Client, filters
from pyrogram.types import Message

# ༺═══════════════════════════════════༻
# ╔═╗╔═╗╔╦╗  ╔╦╗╔═╗╦ ╦╔═╗╦═╗╔═╗
# ╚═╗║╣  ║║   ║ ║ ║║║║║╣ ╠╦╝╚═╗
# ╚═╝╚═╝═╩╝   ╩ ╚═╝╚╩╝╚═╝╩╚═╚═╝
# ༺═══════════════════════════════════༻

# Configuración del bot
API_ID = 14681595
API_HASH = "a86730aab5c59953c424abb4396d32d5"
BOT_TOKEN = "6239580055:AAEukPjVCokbr__88Cjl_eXpAVQ5HvMCFIo"

# ༺═══════════════════════════════════༻
# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
# ╠═╝║  ║ ║║ ╦║ ║║╣ ╠╦╝
# ╩  ╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═
# ༺═══════════════════════════════════༻

app = Client(
    "mi_bot_pyrogram",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ༺═══════════════════════════════════༻
# ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
# ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
# ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
# ༺═══════════════════════════════════༻

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text(
        "✨ ¡Hola! Soy un bot simple creado con Pyrogram.\n\n"
        "🔹 Usa /help para ver los comandos disponibles."
    )

@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "📌 **Comandos disponibles:**\n\n"
        "/start - Inicia el bot\n"
        "/help - Muestra esta ayuda\n"
        "/info - Muestra información del bot\n"
        "/hola - Te saludo amablemente"
    )

@app.on_message(filters.command("info"))
async def info_command(client: Client, message: Message):
    await message.reply_text(
        "🤖 **Información del bot:**\n\n"
        "▸ Framework: Pyrogram\n"
        "▸ Desplegado en: RAILWAY.COM\n"
        "▸ Creado con ❤️ para demostración"
    )

@app.on_message(filters.command("hola"))
async def hola_command(client: Client, message: Message):
    await message.reply_text(
        f"👋 ¡Hola, {message.from_user.first_name}!\n\n"
        "¿Cómo estás hoy? 😊"
    )

# ༺═══════════════════════════════════༻
# ╔═╗╔═╗╔╦╗╔═╗╦  ╔═╗
# ║ ╦║╣  ║ ║ ║║  ╚═╗
# ╚═╝╚═╝ ╩ ╚═╝╩═╝╚═╝
# ༺═══════════════════════════════════༻

if __name__ == "__main__":
    print("⚡ Bot iniciado...")
    app.run()