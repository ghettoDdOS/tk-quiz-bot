import logging
import os

from django.conf import settings
from django_telegrambot.apps import DjangoTelegramBot
from python_telegram_bot_django_persistence.persistence import DjangoPersistence
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    Dispatcher,
    Filters,
    MessageHandler,
    Updater,
)

from .enums import MessageType, QuestionnaireType
from .models import KidsGames, Messages

logger = logging.getLogger(__name__)
QUESTIONNAIRE, START_TESTS, START_GAME, IN_GAME = range(4)


def get_or_empty(question_type):
    try:
        return Messages.objects.get(question_type=question_type).text
    except Messages.DoesNotExist:
        return ""


def send_file_if_exist(update: Update, question_type):
    try:
        msg = Messages.objects.get(
            question_type=question_type,
        )
        if msg.document:
            with open(
                os.path.join(settings.MEDIA_ROOT, msg.document.name), "rb"
            ) as file:
                update.message.reply_document(file)
    except Exception as e:
        logger.warn('Update "%s" caused error "%s"' % (update, e))


def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [
        [
            QuestionnaireType.FOR_PARENTS.value,
            QuestionnaireType.FOR_KIDS.value,
        ],
        [QuestionnaireType.KIDS_TESTS.value],
    ]

    update.message.reply_text(
        get_or_empty(MessageType.START_MESSSAGE),
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
        ),
    )
    send_file_if_exist(update, MessageType.START_MESSSAGE)
    return QUESTIONNAIRE


def questionnaire_for_parents(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [["Назад"]]
    update.message.reply_text(
        get_or_empty(MessageType.PARENTS_SCREEN),
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
        ),
    )
    send_file_if_exist(update, MessageType.PARENTS_SCREEN)


def questionnaire_for_kids(update: Update, context: CallbackContext) -> int:
    games = KidsGames.objects.all()
    games_name = [game.name for game in games]
    games_buttons = list(zip(games_name[::2], games_name[1::2]))
    if len(games_name) % 2:
        games_buttons.append(games_name[-1])
    reply_keyboard = [*games_buttons, ["Назад"]]
    update.message.reply_text(
        get_or_empty(MessageType.KIDS_SCREEN),
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
        ),
    )
    send_file_if_exist(update, MessageType.KIDS_SCREEN)

    return START_GAME


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def tests_for_kids(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [["Назад"]]
    update.message.reply_text(
        get_or_empty(MessageType.TEST_FOR_KIDS_SCREEN),
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
        ),
    )
    send_file_if_exist(update, MessageType.TEST_FOR_KIDS_SCREEN)

    return START_TESTS


def get_game(game_data):
    def play_game(update: Update, context: CallbackContext) -> int:
        reply_keyboard = [["Назад"]]
        update.message.reply_text(
            game_data,
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard,
            ),
        )
        return IN_GAME

    return play_game


def main():
    updater: Updater = DjangoTelegramBot.updater
    updater.persistence = DjangoPersistence()
    dp: Dispatcher = updater.dispatcher
    dp.persistence = DjangoPersistence()
    dp.use_context = True

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            QUESTIONNAIRE: [
                MessageHandler(
                    Filters.regex(
                        f"^({QuestionnaireType.FOR_PARENTS.value})$",
                    ),
                    questionnaire_for_parents,
                ),
                MessageHandler(
                    Filters.regex(f"^({QuestionnaireType.FOR_KIDS.value})$"),
                    questionnaire_for_kids,
                ),
                MessageHandler(
                    Filters.regex(f"^({QuestionnaireType.KIDS_TESTS.value})$"),
                    tests_for_kids,
                ),
                MessageHandler(Filters.regex("^Назад$"), start),
            ],
            START_GAME: [
                *[
                    MessageHandler(
                        Filters.regex(f"^{game.name}$"),
                        get_game(game.message),
                    )
                    for game in KidsGames.objects.all()
                ],
                MessageHandler(Filters.regex("^Назад$"), start),
            ],
            IN_GAME: [
                MessageHandler(
                    Filters.regex("^Назад$"),
                    questionnaire_for_kids,
                ),
            ],
            START_TESTS: [
                MessageHandler(Filters.regex("^Назад$"), start),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex("^В главное меню$"), start)],
        persistent=True,
        name="MainQuiz",
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
