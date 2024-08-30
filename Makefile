
setup: install test lint selfcheck check build

install:
	poetry install

test:
	poetry run pytest

install pyyaml:
	pip install pyyaml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 --extend-ignore=C901 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
