import os

from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
