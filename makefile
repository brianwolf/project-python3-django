run r:
	python manage.py runserver localhost:8000


migrate m:
	python manage.py migrate


make-makemigrations mm:
	python manage.py makemigrations $(app)


create-user:
	python manage.py createsuperuser

