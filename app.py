from flask import Flask, request, render_template, flash, Markup
app = Flask(__name__, static_folder='templates/stylesheets')
app.secret_key = "lubalunilayilasnama"

@app.route('/')
def render_index_page():
    return render_template('/index.html')

@app.route('/t2b', methods=['POST', 'GET'])
def render_t2b():
	if request.method == 'GET':
		return render_template('/t2b.html',change='', placeholder='Input the message to be encoded here!')
	if request.method == 'POST':
		message, converted_message = convert('t2b')
		if converted_message is None:
			return render_template('/t2b.html',change='change', placeholder='Invalid Input! Try again :(')
		else:
			return render_template("/t2b-solve.html", input=message, output=converted_message)
		
@app.route('/b2t', methods=['POST', 'GET'])
def render_b2t():
	if request.method == 'GET':
		return render_template('/b2t.html', change = '', placeholder='Input the message to be decoded here!')
	if request.method == 'POST':
		message, converted_message = convert('b2t')
		if converted_message is None:
			return render_template('/b2t.html', change = 'change', placeholder='Invalid Input! Try again :(')
		else:
			return render_template("/b2t-solve.html", input=message, output=converted_message)
		
def convert(dir):
		message=request.form['message']
		converted_message=None
		if message:
			if dir =='b2t' and isbinary(message):
				converted_message = BinaryToASCII(message)
			elif dir == 't2b' and (not isbinary(message)) and message.isascii():
				converted_message = ASCIIToBinary(message)
		return message, converted_message
		

def isbinary(message):
	message_set = set(message)-{' '}
	if  message_set.issubset({'0', '1'}):
		return True
	else:
		return False

def BinaryToASCII(message):
	return ''.join([chr(int(letter,2)) for letter in message.split()])

def ASCIIToBinary(message):
	encoded_message = [bin(ord(letter))[2:] for letter in message]
	return ' '.join(['0'*(8-len(letter))+letter for letter in encoded_message])
			
if __name__ == "__main__":
	app.debug=True
	app.run()
