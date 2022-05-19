# Django Telegram Bot settings
from config.settings.base import env

TELEGRAM_TOKEN = env("TELEGRAM_TOKEN", default="")

assert TELEGRAM_TOKEN, "Укажите TELEGRAM_TOKEN в env"

DJANGO_TELEGRAMBOT = {
    "MODE": "POLLING",
    "BOTS": [
        {
            "TOKEN": TELEGRAM_TOKEN,
        },
    ],
}
