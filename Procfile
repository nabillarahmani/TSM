web: python tsm.py
web: gunicorn --pythonpath wsgi:application --log-file -
heroku ps:scale web=1