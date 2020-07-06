from flask import Flask, request, render_template, flash, Markup
app = Flask(__name__, static_folder='templates/stylesheets')
app.secret_key = "super secret key"

@app.route('/')
def render_index_page():
    return render_template('/index.html')

@app.route('/t2b', methods=['POST', 'GET'])
def render_t2b():
	if request.method == 'GET':
		return render_template('/t2b.html')
	if request.method == 'POST':
		message=request.form['encodedMessage']
		if message:
			converted_message="Testing"
			return render_template("/t2b-solve.html", input=message, output=converted_message)
		else:
			return render_template('/t2b.html')

@app.route('/b2t', methods=['POST', 'GET']) 
def render_b2t():
    return render_template('/b2t.html')   

if __name__ == "__main__":   
	app.debug=True
	app.run()
