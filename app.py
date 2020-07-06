from flask import Flask, request, render_template
app = Flask(__name__, static_folder='templates/stylesheets')

@app.route('/')
def render_index_page():
    return render_template('/index.html')

@app.route('/t2b', methods=['POST', 'GET'])
def render_t2b():
    return render_template('/t2b.html')

def encode_message():
	return
	
@app.route('/b2t', methods=['POST', 'GET']) 
def render_b2t():
    return render_template('/b2t.html')   

def decode_message():
	return

if __name__ == "__main__":      
    app.run() 
