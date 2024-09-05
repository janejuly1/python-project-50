
setup: install test build lint

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
	poetry run flake8 gendiff
