from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import MessageType


class Messages(models.Model):
    """Сообщения бота"""

    question_type = models.CharField(
        _("Тип сообщения"),
        max_length=50,
        choices=MessageType.choices,
        unique=True,
        null=True,
    )

    text = models.TextField(
        _("Сообщение"),
        null=True,
    )
    document = models.FileField(
        _("Файл с упражнениями (необязательный)"),
        help_text=_("Будет прикреплен к сообщению."),
        upload_to="telegram/tests",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.question_type

    class Meta:
        verbose_name = _("Сообщение")
        verbose_name_plural = _("Сообщения")


class KidsGames(models.Model):
    """Развивающие игры для детей"""

    name = models.CharField(
        _("Название"),
        max_length=50,
        unique=True,
        null=True,
    )
    message = models.TextField(_("Сообщение"), null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Игра")
        verbose_name_plural = _("Игры")
