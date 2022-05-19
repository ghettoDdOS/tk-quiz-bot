# Including commands
run-django-server:
	./.venv/bin/python ./manage.py runserver localhost:8000

run-polling:
	./.venv/bin/python ./manage.py botpolling --username=tk_quiz_test_bot

install-backend:
	./.venv/bin/python -m pip install -U setuptools
	./.venv/bin/python -m pip install -r requirements.txt

.PHONY: venv
venv:
	python -m venv .venv

.PHONY: createadmin
createadmin:
	./.venv/bin/python ./manage.py createsuperuser

.PHONY: migrations
migrations:
	./.venv/bin/python ./manage.py makemigrations

.PHONY: migrate
migrate:
	./.venv/bin/python ./manage.py migrate

# Primary commands
.PHONY: install
install:
	@make install-backend
	./.venv/bin/python ./manage.py initconfig --debug
	@make migrate
	./.venv/bin/python ./manage.py defaultadmin
	./.venv/bin/python ./manage.py defaultfixtures

.PHONY: install-prod
install-prod:
	./.venv/bin/python -m pip install -U pip
	@make install-backend
	./.venv/bin/python ./manage.py initconfig

.PHONY: run
run:
	@make run-django-server

.PHONY: run-bot
run-bot:
	@make run-polling

.PHONY: build
build:
	./.venv/bin/python ./manage.py collectstatic
	@make migrate
	./.venv/bin/python ./manage.py defaultadmin
	./.venv/bin/python ./manage.py defaultfixtures
