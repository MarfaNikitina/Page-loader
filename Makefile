install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

 publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games

flask-upp:
	export FLASK_APP=hello_world.py

flask-env:
	export FLASK_ENV=development

flask-run:
	python -m flask run