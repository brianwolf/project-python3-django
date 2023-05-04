guniconr g:
	gunicorn \
    	-b localhost:8000 \
    	--workers=1 \
    	--threads=5 \
    	core.wsgi

run r:
	python manage.py runserver


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
	coverage xml


sonar s:
	sonar-scanner \
		-Dsonar.projectKey=python3-django \
		-Dsonar.sources=. \
		-Dsonar.host.url=http://localhost:9000 \
		-Dsonar.login=sqa_cc5ddd2c5530313efdccc5cdd0920ac30a118179 \
		-Dsonar.python.coverage.reportPaths=coverage.xml \
		-Dsonar.exclusions=**/core/*
