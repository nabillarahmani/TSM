web: python manage.py runserver
web: gunicorn --pythonpath wsgi:app --log-file -
heroku ps:scale web=1