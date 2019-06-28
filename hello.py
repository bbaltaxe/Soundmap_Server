from flask import Flask, url_for, render_template
import json

app = Flask(__name__)

#making several pages
@app.route('/')
def index(): 
    return 'welcome to a webpage'

@app.route('/hello')
def hello(): 
    return 'Hey its bre'

#making a map page
@app.route('/map')
def map():
    #generate map here, and then send it to a file named /templates/map.html
    return render_template('map.html')

#json endpoint 
@app.route('/authors')
def authors():
    madeby = ['bre', 'davin', 'joy']
    return json.dumps(madeby)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
