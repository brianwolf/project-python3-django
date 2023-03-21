run r:
	gunicorn \
    	-b localhost:8000 \
    	--workers=1 \
    	--threads=5 \
    	core.wsgi


migrate m:
	python manage.py migrate


makemigrations mm:
	python manage.py makemigrations $(app)


create-user:
	python manage.py createsuperuser


test t:
	python manage.py test


coverage c:
	coverage run --omit=*/env/*,*/migrations/*,*/__init__.py,manage.py,*/core/* manage.py test
	coverage report -m
	coverage html