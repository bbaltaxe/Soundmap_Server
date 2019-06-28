from flask import Flask, url_for, render_template
import json
import yaml

app = Flask(__name__)
with open('secrets.yaml','r') as api_file:
	gkey = yaml.load(api_file)['api_keys']['google']


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
