
setup: install install_pyyaml build lint test

install:
	poetry install

test:
	poetry run pytest

install_pyyaml:
	pip install pyyaml

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
