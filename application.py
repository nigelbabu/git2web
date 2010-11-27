import ConfigParser, os
from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    config = ConfigParser.ConfigParser()
    config.read('gitosis.conf')
    return render_template('index.html', config=config)

if __name__ == '__main__':
    app.run(debug=True)
