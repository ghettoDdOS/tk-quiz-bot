from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Панель управления")
admin.site.index_title = _("Панель управления")
admin.site.site_title = _("Администрирование")

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns = (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
