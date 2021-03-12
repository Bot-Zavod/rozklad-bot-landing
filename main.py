from flask import Flask, render_template, request, redirect


app = Flask('rozklad', static_url_path='/public', static_folder='public')





@app.route('/', methods=['GET', 'POST'])
def main_page():

	return render_template('index.html')




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80) # host='0.0.0.0', port=80

# debug=True, use_reloader=True,

