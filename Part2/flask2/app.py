from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is flask 2 \n -xavier'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')