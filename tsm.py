from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_dotenv import DotEnv

def create_app():
	env = DotEnv()
	app = Flask(__name__)
	env.init_app(app)
	env.eval(keys={
		'DEBUG': bool,
		'TESTING': bool
	})

	@app.route("/")
	def index():
		"""
			Render the view of index page.
		"""
		return render_template('index.html', title='Tri Sinergi Mitra', current_page='TSM')

	@app.errorhandler(404)
	def page_not_found_error(err):
		"""
		Render the view of error 404 page
		"""
		return render_template('404.html', title='TSM not found', current_page='404')

	@app.errorhandler(500)
	def internal_server_error(err):
		"""
		Render the view of error 500 page
		"""
		return render_template('500.html', title='TSM internal server error', current_page='500')

	return app


if __name__ == "__main__":
	application = create_app()
	application.run(host=application.config['HOST'], port=int(application.config['PORT']))