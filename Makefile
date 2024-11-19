
setup: install build lint test

install:
	poetry install

test:
	pip install pytest
	poetry run pytest

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

flake8:
	pip install flake8

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run coverage run -m pytest
