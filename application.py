from flask import Flask

app = Flask(__name__)

@app.route('/app/<variable>')
def hello(variable):
    return f'<h1>Hello {variable}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
