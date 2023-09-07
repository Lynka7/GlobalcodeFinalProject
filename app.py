from flask import Flask
from flask import render_template
from pprint import pprint

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    try:
        #x = 10/0
        return render_template('index.html')

    except Exception as e:
        return f'{type(e)}'
        
@app.post('/welcome')
def welcome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')