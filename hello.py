from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    return 'welcome to a webpage'

@app.route('/hello')
def hello(): 
    return 'Hey its bre'

@app.route('/map')
def map(): 
    return render_template('map.html')

if __name__ == '__main__':
    app.run()
