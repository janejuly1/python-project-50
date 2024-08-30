
setup: install install pyyaml build publish package-install lint gendiff

install:
	poetry install

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
