from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'hello , ashiq'

if __name__=='__main__':
    app.run(debug=True)
