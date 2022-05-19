from enum import Enum

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class QuestionnaireType(Enum):
    FOR_PARENTS = "Для родителей"
    FOR_KIDS = "Для детей"
    KIDS_TESTS = "Упражнения для развития детей"


class MessageType(TextChoices):
    START_MESSSAGE = "start", _("Приветственное сообщение")
    PARENTS_SCREEN = "parents", _("Экран для родителей")
    KIDS_SCREEN = "kids", _("Экран для детей")
    TEST_FOR_KIDS_SCREEN = "kids_test", _("Упражнения для детей")
