run r:
	gunicorn \
    	-b localhost:8000 \
    	--workers=1 \
    	--threads=5 \
    	core.wsgi


migrate m:
	python manage.py migrate


make-makemigrations mm:
	python manage.py makemigrations $(app)


create-user:
	python manage.py createsuperuser
