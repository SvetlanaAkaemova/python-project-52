MANAGE := poetry run python manage.py

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	poetry install

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

make-migration:
	@$(MANAGE) makemigrations

migrate: make-migration
	@$(MANAGE) migrate

.PHONY: build
build:
	install migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

test-coverage:
	@poetry run coverage run manage.py test
	@poetry run coverage xml
	@poetry run coverage report
