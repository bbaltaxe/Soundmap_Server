from flask import Flask, url_for, render_template
import json
import yaml
from joy import gen_map as gm
import os.path


app = Flask(__name__)

DIR = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(DIR,'../UCSC_Sound_Map.csv')
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
@app.route('/joy/map')
def map():
	#generate map here, and then send it to a file named /templates/map.html
	maploc = os.path.join(DIR,gm.generate_map(CSV,gkey))
	return render_template(maploc)

#json endpoint 
@app.route('/authors')
def authors():
    madeby = ['bre', 'davin', 'joy']
    return json.dumps(madeby)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
