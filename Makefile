run:
	python manage.py runserver 0.0.0.0:8000

test:
	python manage.py test

deploy:
	docker-compose build && docker-compose up -d
