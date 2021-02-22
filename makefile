.DEFAULT_GOAL := build

install:
	poetry install

build:
	rm -rf ./dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl
