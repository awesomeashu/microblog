from app import app
@app.route('/')
@app.route('/index')
def index():
	return 'i am awesome this is my first website created using python'

