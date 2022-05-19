# Including commands
run-django-server:
	./.venv/bin/python ./manage.py runserver localhost:8000

install-backend:
	./.venv/bin/python -m pip install -U setuptools
	./.venv/bin/python -m pip install -r requirements.txt

.PHONY: createadmin
createadmin:
	./.venv/bin/python ./manage.py createsuperuser

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

.PHONY: build
build:
	./.venv/bin/python ./manage.py collectstatic
	@make migrate
	./.venv/bin/python ./manage.py defaultadmin
	./.venv/bin/python ./manage.py defaultfixtures
