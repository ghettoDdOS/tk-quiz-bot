"""Paths settings"""

import os

# Base
CONFIG_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
PROJECT_DIR = os.path.dirname(CONFIG_DIR)
ENV_FILE = os.path.join(PROJECT_DIR, ".env")
ENV_FILE_EXAMPLE = os.path.join(PROJECT_DIR, ".env.example")

PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
PRIVATE_DIR = os.path.join(PROJECT_DIR, "private")
PUBLIC_MEDIA_DIR = os.path.join(PUBLIC_DIR, "media")
PUBLIC_STATIC_DIR = os.path.join(PUBLIC_DIR, "static")
STATIC_DIR = os.path.join(PRIVATE_DIR, "static")
TEMPLATES_DIR = os.path.join(PRIVATE_DIR, "templates")

# Backend
FIXTURES_DIR = os.path.join(PROJECT_DIR, "fixtures")
DEV_DATABASE_FILE = os.path.join(PRIVATE_DIR, "db.sqlite3")
TEST_DATABASE_FILE = os.path.join(PRIVATE_DIR, "test_db.sqlite3")
FIXTURE_DIRS = [
    FIXTURES_DIR,
]
