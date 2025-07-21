migrate:  # TODO переделать
	python3 ./manage.py makemigrations ${app}
	python3 ./manage.py migrate
serv:  # TODO переделать
	python3 ./manage.py runserver
lint:
	black --check --diff .
	isort --check-only --diff --recursive .
style:
	black .
	isort .
install:  # TODO переделать
	pip freeze | grep -v "^-e" | xargs pip uninstall -y
	pip3 install -r requirements.txt
