from django.contrib import admin

from .models import KidsGames, Messages


@admin.register(KidsGames)
class KidsGamesAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = (
        "question_type",
        "text",
        "document",
    )
    list_editable = (
        "text",
        "document",
    )
