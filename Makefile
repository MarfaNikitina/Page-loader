install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page-loader --cov-report xml

