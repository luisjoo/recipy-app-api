# builds the docker image
docker build .

# runs docker compose
docker-compose build

# creates the Django project
docker-compose run app sh -c "django-admin.py startproject app ."

# runs the tests
docker-compose run app sh -c "python manage.py test"