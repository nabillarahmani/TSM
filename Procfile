web: python manage.py runserver
web: gunicorn --pythonpath wsgi --log-file -
heroku ps:scale web=1