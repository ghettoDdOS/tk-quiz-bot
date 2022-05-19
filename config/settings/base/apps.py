DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.utils",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
