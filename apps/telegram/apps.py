from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TelegramConfig(AppConfig):
    """Default app config"""

    name = "apps.telegram"
    verbose_name = _("Телеграм Бот")
