# TSM

## Notes for citra!

TSM TO DO LIST

Citra's to do list for TSM : 

1. Cloning your git application from Heroku
 - Clone your application on desktop in terminal using `heroku git:clone -a trisinergimitra` command [X]
 - cd into 'trisinergimitra' 
 - Create a new virtual environment using command `virtualenv environment_citra` [X] 
 - Change your .gitignore list by using command `nano .gitginore` [ ]
  - add 'environment_citra' on the last line of your .gitignore files (gitignore will determine which folders or files that will not be push onto remote)
 - Activate your virtual environment using `source env/bin/activate` command [ ]
 - Install all requirements using `pip install -r requirements.txt` [ ]
 - Once you have completed all the installation, then create a new branch from current branch master to work on your environment!
  - Use command 'git checkout -b f_<namafeature>' [ ]
 - Now you are ready to work!!

2. Running your application
 - Simple things is just simple! 
  - Make changes within your application [ ]
  - running your application under local host port 5000! With `python tsm.py` command [ ]

3. Deploying your application on Heroku! (Actually also pushing changes onto master)
 - Add every changes that you add with using `git add .` command [ ]
 - Commit your change using `git commit -m "commit_message"`
 - Push your changes into github remote and deploy into heroku using `git push heroku master` [ ]

=== Citra's todo list ===

1. Implement Home section
 - Add logo
 - Add punchline di home wkwk
 - Use some 'wow.js' (search it on google) 

2. Implement about section (mandatory)
 - add explanation
 - Use some 'wow.js' (search it on google) 


3. Implement Our service section (mandatory)
 - Baca dari comprof

4. Implement Gallery section (optional)

=== Nabey's todo list ===

1. Ngebenerin preloading [X]
2. Implement form section and integrating form using jinja [ ]
3. Ngejelasin ke citra soal: 

 1. Getting started with Flask environment
  - it will take for about 2 hours to understand how flask works
   - Flask structure [ ]
   - Dependency on flask packages and how to use it [ ]
   - Flask configuration / The use of .env instead of config.py [ ]
   - Flask routing [ ] 
   - Flask jinja2 template [ ]
   - Werkzeug / wsgi based application [ ]

 2. How heroku's work
  - Pre deployment 
   - Procfile [ ]
   - wsgi.py [ ]
   - gunicorn [ ]
   - slug [ ]
   - requirements.txt [ ]
  -  When deploy
   - Dyno [ ]